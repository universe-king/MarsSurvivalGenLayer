# v0.2.20
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json


class MarsSurvivalGame(gl.Contract):

    user_scenarios: TreeMap[str, str]
    user_judgments: TreeMap[str, str]

    user_survival_count: TreeMap[str, u32]
    user_death_count: TreeMap[str, u32]
    leaderboard_addresses: DynArray[str]

    def __init__(self):
        pass

    @gl.public.write
    def generate_scenario(self) -> str:
        user_address = str(gl.message.sender_address).lower()

        def leader_fn() -> str:
            prompt = f"""
            You are a master storyteller for a hard sci-fi survival game.
            Generate a unique survival scenario on Mars for Astronaut ID: {user_address}.
            The user has 48 hours of oxygen.

            HARD OUTPUT REQUIREMENTS:
            - Write entirely in English.
            - Stay under 150 words.
            - Include exactly 3 tactical survival questions.
            - The questions must be relevant to the Mars survival situation.
            - Output only the scenario and its 3 questions.
            """
            return gl.nondet.exec_prompt(prompt)

        def validator_fn(leader_result) -> bool:
            if not isinstance(leader_result, gl.vm.Return):
                return False

            raw = leader_result.calldata

            if not raw or len(raw.strip()) < 20:
                return False

            word_count = len(raw.split())
            if word_count >= 150:
                return False

            question_count = raw.count("?")
            if question_count != 3:
                return False

            latin_letters = sum(
                1 for ch in raw
                if ("A" <= ch <= "Z") or ("a" <= ch <= "z")
            )
            total_letters = sum(1 for ch in raw if ch.isalpha())

            if total_letters == 0:
                return False

            if latin_letters / total_letters < 0.90:
                return False

            check_prompt = f"""
            Validate the following generated Mars survival scenario.

            It MUST satisfy ALL of these requirements:
            1. It is a Mars survival scenario.
            2. It contains exactly 3 tactical survival questions.
            3. It is written entirely in English.
            4. It is under 150 words.
            5. The three questions are relevant to the survival situation.

            Reply ONLY with YES if every requirement is satisfied.
            Reply ONLY with NO if even one requirement is not satisfied.

            Text:
            {raw}
            """

            approval = gl.nondet.exec_prompt(check_prompt).strip().upper()

            return approval == "YES"

        scenario = gl.vm.run_nondet_unsafe(
            leader_fn,
            validator_fn
        )

        self.user_scenarios[user_address] = scenario

        return scenario

    @gl.public.view
    def get_scenario(self, user: str) -> str:
        try:
            return self.user_scenarios[user.lower()]
        except:
            return ""

    @gl.public.write
    def judge_survival(self, user_answers: str) -> str:
        user_address = str(gl.message.sender_address).lower()

        try:
            scenario = self.user_scenarios[user_address]
        except Exception:
            scenario = ""

        if not scenario:
            raise gl.vm.UserError(
                "No scenario found for this address. Call generate_scenario first."
            )

        def leader_fn() -> str:
            prompt = f"""
            Scenario: {scenario}
            Answers: {user_answers}
            Is this survivor: SURVIVED or DIED? Output ONLY the word SURVIVED or DIED.
            """

            return gl.nondet.exec_prompt(prompt).strip().upper()

        def validator_fn(leader_result) -> bool:
            if not isinstance(leader_result, gl.vm.Return):
                return False

            leader_verdict = leader_result.calldata.strip().upper()

            if leader_verdict not in ("SURVIVED", "DIED"):
                return False

            val_prompt = f"""
            Scenario: {scenario}
            Answers: {user_answers}
            Based on logic, does the user SURVIVED or DIED?
            Output ONLY the word SURVIVED or DIED.
            """

            val_verdict = gl.nondet.exec_prompt(val_prompt).strip().upper()

            return leader_verdict == val_verdict

        raw_judgment = gl.vm.run_nondet_unsafe(
            leader_fn,
            validator_fn
        )

        if user_address not in self.leaderboard_addresses:
            self.leaderboard_addresses.append(user_address)

        if raw_judgment == "SURVIVED":
            try:
                current = self.user_survival_count[user_address]
            except Exception:
                current = 0

            self.user_survival_count[user_address] = u32(
                int(current) + 1
            )

        elif raw_judgment == "DIED":
            try:
                current = self.user_death_count[user_address]
            except Exception:
                current = 0

            self.user_death_count[user_address] = u32(
                int(current) + 1
            )

        verdict = {
            "status": raw_judgment,
            "explanation": "Judged securely by GenLayer AI Consensus Protocol."
        }

        verdict_str = json.dumps(verdict)

        self.user_judgments[user_address] = verdict_str

        return verdict_str

    @gl.public.view
    def get_judgment(self, user: str) -> str:
        try:
            return self.user_judgments[user.lower()]
        except:
            return ""

    @gl.public.view
    def get_survival_count(self, user: str) -> int:
        try:
            return int(self.user_survival_count[user.lower()])
        except:
            return 0

    @gl.public.view
    def get_death_count(self, user: str) -> int:
        try:
            return int(self.user_death_count[user.lower()])
        except:
            return 0

    @gl.public.view
    def get_leaderboard(self) -> str:
        rows = []

        for addr in self.leaderboard_addresses:
            try:
                survived = int(self.user_survival_count[addr])
            except Exception:
                survived = 0

            try:
                died = int(self.user_death_count[addr])
            except Exception:
                died = 0

            total = survived + died

            if total > 0:
                rate = round((survived / total) * 100, 1)
            else:
                rate = 0.0

            rows.append({
                "address": addr,
                "survived": survived,
                "died": died,
                "total": total,
                "survival_rate": rate
            })

        rows.sort(
            key=lambda row: (
                -row["survived"],
                -row["survival_rate"]
            )
        )

        return json.dumps(rows)
