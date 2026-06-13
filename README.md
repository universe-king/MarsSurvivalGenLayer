# Mars Survival Game GenLayer Intelligent Contract

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GenLayer](https://img.shields.io/badge/Network-GenLayer%20Testnet-blueviolet)](https://genlayer.com)
[![AI-Consensus](https://img.shields.io/badge/Architecture-AI%20Consensus%20Protocol-blue)](https://docs.genlayer.com)

An advanced, decentralized hard sci fi survival game built using **GenLayer Intelligent Contracts**. This project leverages decentralized Large Language Models (LLMs) to create a dynamic, high stakes storytelling experience on Mars where every player decision is evaluated rigorously through a multi node cryptographic and semantic consensus mechanism.

---

## Architectural Overview & The Equivalence Principle

Unlike traditional smart contracts that rely on deterministic math, GenLayer allows execution of non-deterministic AI prompts. To prevent "AI hallucination" or malicious node behavior, this contract strictly enforces the **Equivalence Principle**.

    [ Player Request ] ──> [ Leader Node ] ──> Generates Scenario / Verdict
                                 │
                                 ▼
                        [ Validator Node ] ──> Independently Evaluates Logic
                                 │
                                 ▼
                        [ Equivalence Check ] ─( Matches? )─> Yes ──> Write to State
                                                                No  ──> Reject Tx


### 1. Semantic Equivalence (`generate_scenario`)
When an astronaut triggers a new mission, the **Leader Node** crafts a unique 150 word Mars survival scenario. The **Validator Node** does not blindly sign this text; instead, it executes a secondary semantic evaluation prompt to ensure the output conforms strictly to game rules (i.e., contains a valid Martian survival theme and exactly 3 tactical questions).

### 2. Inferential Equivalence (`judge_survival`)
When a player submits their answers, the **Leader Node** proposes a state change (`SURVIVED` or `DIED`). The **Validator Node** independently processes the scenario and the player's choices. The transaction only achieves consensus and updates the ledger if both nodes arrive at the **exact same logical conclusion**.

---

## Intelligent Contract API Reference

The contract exposes the following public methods:

### Write Methods (State-Changing)
* **`generate_scenario() -> str`**
    * Generates a unique, high-stakes scenario tailored to the sender's wallet address.
    * Enforces a strict 150 word constraint to optimize processing speed and gas efficiency.
* **`judge_survival(scenario: str, user_answers: str) -> str`**
    * Submits the player's tactical decisions to the AI consensus engine.
    * Processes the result natively as an atomic string to completely eliminate JSON parsing failures.

### View Methods (Read Only)
* **`get_scenario(user: str) -> str`**
    * Retrieves the stored scenario for a specific astronaut address.
* **`get_judgment(user: str) -> str`**
    * Fetches the finalized cryptographic verdict and explanation for a given user.

---

## Technical Specifications

* **Language:** Python (GenLayer Smart Contract Dialect Framework v0.2.20)
* **Storage Architecture:** `TreeMap[str, str]` for gas efficient, transactional state storage maps.
* **Output Optimization:** Pure string matching (`.strip().upper()`) to ensure absolute consensus determinism across heterogeneous LLM nodes.

---

## How to Run & Interact

This project includes a fully functional frontend (dApp) to interact with the Intelligent Contract seamlessly.

### 1. Smart Contract Deployment
You can deploy the contract (`contract.py`) to the GenLayer testnet using the GenLayer Studio or via the GenLayer CLI:

    npm install -g genlayer-cli
    genlayer deploy contract.py

### 2. Running the Frontend (dApp)
To play the Mars Survival Game via the user interface:
1. Navigate to the frontend directory in your terminal.
2. Install the necessary dependencies:
   
       npm install

3. Start the local development server:
   
       npm run dev

4. Open your browser and navigate to `http://localhost:3000` (or the port specified in your terminal) to start your Mars survival mission!

---

## 📄 License

This project is licensed under the MIT License  see the [LICENSE](LICENSE) file for details.

![Mars Survival](/public/images/img1.png)
![Mars Survival](/public/images/img2.png)
![Mars Survival](/public/images/img3.png)