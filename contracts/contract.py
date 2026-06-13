# v0.2.20
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json

class MarsSurvivalGame(gl.Contract):
    
    user_scenarios: TreeMap[str, str]
    user_judgments: TreeMap[str, str]

    def __init__(self):
        self.user_scenarios = TreeMap()
        self.user_judgments = TreeMap()

    @gl.public.write
    def generate_scenario(self) -> str:
        """Generate a scenario with true and secure consensus."""
        user_address = str(gl.message.sender_address).lower()
        
        def leader_fn() -> str:
            prompt = f"""
            You are a master storyteller for a hard sci-fi survival game.
            Generate a unique survival scenario on Mars for Astronaut ID: {user_address}.
            The user has 48 hours of oxygen. Provide exactly 3 difficult tactical questions.
            CRITICAL: Keep the output under 150 words. Be concise. Output in English only.
            """
            return gl.nondet.exec_prompt(prompt)

        def validator_fn(leader_result) -> bool:
            if not isinstance(leader_result, gl.vm.Return): return False
            raw = leader_result.calldata
            if not raw or len(raw.strip()) < 20: return False
            
            
            check_prompt = f"""
            Does the following text describe a Mars survival scenario containing tactical questions? 
            Reply ONLY with 'YES' or 'NO'.
            Text: {raw}
            """
            approval = gl.nondet.exec_prompt(check_prompt).strip().upper()
            return "YES" in approval

        scenario = gl.vm.run_nondet_unsafe(leader_fn, validator_fn)
        self.user_scenarios[user_address] = scenario
        return scenario

    @gl.public.view
    def get_scenario(self, user: str) -> str:
        try:
            return self.user_scenarios[user.lower()]
        except:
            return ""

    @gl.public.write
    def judge_survival(self, scenario: str, user_answers: str) -> str:
        """Judge the survival outcome strictly adhering to the equivalence principle."""
        user_address = str(gl.message.sender_address).lower()
        
        def leader_fn() -> str:
            prompt = f"""
            Scenario: {scenario}
            Answers: {user_answers}
            Is this survivor: SURVIVED or DIED? Output ONLY the word SURVIVED or DIED.
            """
            return gl.nondet.exec_prompt(prompt).strip().upper()

        def validator_fn(leader_result) -> bool:
            if not isinstance(leader_result, gl.vm.Return): return False
            leader_verdict = leader_result.calldata.strip().upper()
            if leader_verdict not in ("SURVIVED", "DIED"): return False
            
            
            val_prompt = f"""
            Scenario: {scenario}
            Answers: {user_answers}
            Based on logic, does the user SURVIVED or DIED? Output ONLY the word SURVIVED or DIED.
            """
            val_verdict = gl.nondet.exec_prompt(val_prompt).strip().upper()
            
            
            return leader_verdict == val_verdict

        raw_judgment = gl.vm.run_nondet_unsafe(leader_fn, validator_fn)
        
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