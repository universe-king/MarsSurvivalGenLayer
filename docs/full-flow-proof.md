# Full Flow Execution Proof

This document records the complete end to end execution flow of the Mars Survival application and the corresponding contract interactions

## 1. Wallet Connection

The user connects their wallet to the Mars Survival application

## 2. Scenario Generation

The user clicks **Generate Scenario**

The wallet opens and requests confirmation for the `generate_scenario` transaction

After the user confirms the transaction is submitted to the network

The contract generates a Mars survival scenario using GenLayer nondeterministic execution and stores the generated scenario for the user's address

The frontend then reads the generated scenario from the network and displays it to the user

## 3. Survival Strategy Submission

The user reads the generated scenario and writes their survival strategy and answers to the tactical questions

The user submits their answers

The wallet opens again and requests confirmation for the `judge_survival` transaction

After confirmation, the transaction is submitted to the network

## 4. GenLayer AI Consensus

The `judge_survival` contract function evaluates the submitted answers against the generated scenario

GenLayer's nondeterministic execution is used to obtain and validate the survival judgment

The accepted result is either:

`SURVIVED`

or

`DIED`

## 5. Result Readback

After the judgment is completed the result is stored by the contract

The frontend reads the judgment from the network and displays the final result to the user

The contract also records the user's survival and death counts

## 6. Leaderboard

The leaderboard reads the user's recorded results from the contract

For each address the contract calculates and returns:

* Number of survivals
* Number of deaths
* Survival percentage

## End to End Flow

The complete application flow is:

`Wallet Connection → Generate Scenario → Transaction Confirmation → Scenario Generation → Network Readback → Strategy Submission → Transaction Confirmation → GenLayer Consensus → Judgment Readback → Result Display → Leaderboard Statistics`

## Execution Video

A video recording demonstrating the complete execution flow is available here:

[Full Flow Execution Video](https://drive.google.com/file/d/1suruKmHeP4V26O7kO3dER_7oOl_T2d0y/)

## Deployed Contract

Contract address:

`https://studio.genlayer.com/?import-contract=0x86b811b139924dD49E6259A9329456C97e08783B`

Explorer:

`https://explorer-studio.genlayer.com/address/0x86b811b139924dD49E6259A9329456C97e08783B`

## Repository Evidence

The contract implementation supporting this flow is contained in the Mars Survival contract

Relevant contract functions include:

* `generate_scenario()` — generates and stores the scenario
* `get_scenario()` — reads the generated scenario
* `judge_survival()` — submits the user's answers and performs the GenLayer judgment
* `get_judgment()` — reads the completed judgment
* `get_survival_count()` — reads survival statistics
* `get_death_count()` — reads death statistics
* `get_leaderboard()` — returns leaderboard statistics including total attempts and survival percentage
