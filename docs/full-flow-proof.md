# Full Flow Execution Proof

This document provides concrete execution evidence for the complete end-to-end flow of the Mars Survival application running on the **GenLayer Studio Network**.

The evidence below is based on actual finalized blockchain transactions executed against the deployed Mars Survival contract on **September 15, 2026**.

The execution demonstrates:

* Wallet connection
* Scenario generation
* Scenario readback
* Survival strategy submission
* GenLayer consensus execution
* Final judgment
* Application result readback
* Leaderboard state

---

## 1. Deployment Information

**Network:**
GenLayer Studio Network

**Deployed Contract:**
`0x86b811b139924dD49E6259A9329456C97e08783B`

**Contract Explorer:**
https://explorer-studio.genlayer.com/address/0x86b811b139924dD49E6259A9329456C97e08783B

**Execution Date:**
September 15, 2026

---

# 2. Wallet Connection

The Mars Survival application successfully detected and connected to the user's Rabby wallet.

**Wallet Provider:**
Rabby

**Connected Wallet:**
`0x5e5eF11f49B0139F6cdBd0D324dcec97f4762ea6`

**Network:**
GenLayer Studio Network

The application confirmed the wallet connection before executing the scenario generation and survival judgment transactions.

### Wallet Connection Evidence

![Wallet Connection](docs/images/wallet-connected.png)
![Wallet Connection](docs/images/wallet-connected-1.png)

---

# 3. Scenario Generation

After connecting the wallet, the application executed the `generate_scenario` contract method.

## Transaction Details

**Method:**
`generate_scenario`

**Transaction Hash:**

`0x4f4d37b7b7a93d73a5c9d4c3947a7119f96ef290c4adc68ff0fa51ccbd655bc7`

**Explorer:**

https://explorer-studio.genlayer.com/tx/0x4f4d37b7b7a93d73a5c9d4c3947a7119f96ef290c4adc68ff0fa51ccbd655bc7

**Created At:**
September 15, 2026, 8:12:15 AM

**From:**

`0x5e5eF11f49B0139F6cdBd0D324dcec97f4762ea6`

**To:**

`0x86b811b139924dD49E6259A9329456C97e08783B`

**Transaction Status:**
`FINALIZED`

**Consensus Result:**
`Accepted`

**Initial Validators:**
`5`

**Execution Mode:**
`Normal`

---

## 3.1 GenVM Execution

The GenLayer Explorer reports:

**Execution Result:**
`SUCCESS`

**Method:**
`generate_scenario`

The transaction reached the finalized state through the GenLayer consensus process.

The consensus stages shown by the Explorer are:

```text
Pending
   ↓
Proposing
   ↓
Committing
   ↓
Revealing
   ↓
Accepted
   ↓
Finalized
```

### Scenario Generation Transaction Evidence
![Scenario Generation Transaction](docs/images/Scenario Generation Transaction.png)
![Scenario Generation Transaction](docs/images/Scenario Generation Transaction-1.png)
![Scenario Generation Transaction](docs/images/Scenario Generation Transaction-2.png)
![Scenario Generation](docs/images/scenario-generation.png)

---

# 4. Generated Scenario

The `generate_scenario` execution returned an actual scenario from the deployed contract.

The returned scenario was:

> Astronaut ID: `0x5e5ef11f49b0139f6cdbd0d324dcec97f4762ea6` awakens in Hab-3 after a micrometeoroid puncture. The hull is sealed, but the primary CO₂ scrubber is offline, leaving only 48 hours of oxygen. A planet-wide dust storm blankets the horizon, and solar arrays are coated with fine regolith, dropping power to 30%. A nearby 20-meter-deep lava tube may contain water-ice, but its entrance is blocked by a collapsed rock slab. The rover’s manipulator arm is damaged, and the EVA suit battery sits at 40%.

The generated scenario contains the following three tactical questions:

**1.** Do you attempt to clear the slab and enter the lava tube to harvest ice, risking oxygen loss and structural collapse?

**2.** Will you divert remaining power to run the emergency CO₂ scrubber at reduced efficiency, sacrificing heating and communications?

**3.** Should you ration oxygen by entering a low-activity sleep cycle while you jury-rig the manipulator arm for a remote repair?

The scenario was returned by the finalized `generate_scenario` transaction and subsequently displayed by the application.

### Generated Scenario Application Evidence

![Generated Scenario](docs/images/generated-scenario.png)

---

# 5. Scenario Readback

After the scenario generation transaction completed, the application successfully fetched and displayed the generated scenario.

This establishes the following execution sequence:

```text
generate_scenario transaction
        ↓
GenVM execution
        ↓
Consensus Accepted
        ↓
Transaction Finalized
        ↓
Scenario returned
        ↓
Application fetched scenario
        ↓
Scenario displayed to user
```

### Scenario Readback Evidence

<!-- INSERT SCREENSHOT HERE -->

---

# 6. Survival Strategy Submission

After receiving the generated scenario, the user submitted a survival strategy through the application.

The application executed the `judge_survival` contract method.

## Transaction Details

**Method:**
`judge_survival`

**Transaction Hash:**

`0x53b166554c558e96158fda5bcb056ad8340465f991d700388ae4e4013d169dd0`

**Explorer:**

https://explorer-studio.genlayer.com/tx/0x53b166554c558e96158fda5bcb056ad8340465f991d700388ae4e4013d169dd0

**Created At:**
September 15, 2026, 8:14:54 AM

**From:**

`0x5e5eF11f49B0139F6cdBd0D324dcec97f4762ea6`

**To:**

`0x86b811b139924dD49E6259A9329456C97e08783B`

**Value:**
`0 GEN`

**Nonce:**
`3`

**Initial Validators:**
`5`

**Execution Mode:**
`Normal`

**Transaction Status:**
`FINALIZED`

**Consensus Result:**
`Accepted`

---

# 7. Submitted Survival Strategy

The actual strategy submitted to the deployed contract was recorded in the transaction input.

The submitted strategy was:

> I will prioritize keeping the habitat sealed and preserving life support. First, I will divert the remaining power to the emergency CO₂ scrubber, even at reduced efficiency. Oxygen and CO₂ control are more critical than heating and communications, and the dust storm makes an EVA extremely risky with the suit battery at only 40%. At the same time, I will enter a controlled low-activity sleep cycle to reduce oxygen consumption while jury-rigging the rover’s manipulator arm for a remote repair. I will not attempt to clear the lava-tube entrance yet. The 20-meter drop, unstable slab, damaged manipulator, and limited suit power make the immediate risk too high. Once the scrubber is stable and the manipulator is operational, I can reassess the lava tube and attempt to recover ice if it is still necessary. Survival priority: stabilize CO₂, conserve oxygen, restore equipment, then attempt resource recovery.

This is not a sample or hypothetical strategy. It is the actual parameter recorded in the `judge_survival` transaction.

### Submitted Strategy / Transaction Evidence

<!-- INSERT SCREENSHOT HERE -->

---

# 8. GenLayer Consensus Execution

The `judge_survival` transaction was processed through GenLayer consensus.

The finalized transaction shows:

**Transaction Status:**
`FINALIZED`

**Consensus Result:**
`Accepted`

**GenVM Execution Result:**
`SUCCESS`

**Initial Validators:**
`5`

**Equivalence Principle Output:**
`SURVIVED`

**Final Return Value:**

```text
{"status": "SURVIVED", "explanation": "Judged securely by GenLayer AI Consensus Protocol."}
```

The Explorer shows the complete consensus progression:

```text
Pending
   ↓
Proposing
   ↓
Committing
   ↓
Revealing
   ↓
Accepted
   ↓
Finalized
```

The GenVM execution completed successfully and the equivalence principle output was:

```text
SURVIVED
```

### Consensus Evidence

<!-- INSERT SCREENSHOT HERE -->

---

# 9. Final Judgment Readback

The final result returned by the `judge_survival` execution was:

**Status:**
`SURVIVED`

**Explanation:**
`Judged securely by GenLayer AI Consensus Protocol.`

The application received the completed judgment and displayed the survival result to the user.

### Final Judgment Application Evidence

<!-- INSERT SCREENSHOT HERE -->

---

# 10. Application Result

The completed execution therefore produced the following application result:

```text
SURVIVED
```

This result is supported by the finalized transaction's:

* `FINALIZED` status
* `Accepted` consensus result
* `SUCCESS` GenVM execution
* `SURVIVED` Equivalence Principle Output
* `SURVIVED` return value

### Application Result Screenshot

<!-- INSERT SCREENSHOT HERE -->

---

# 11. Contract / Application State Readback

Following the successful survival judgment, the application displayed the corresponding survival statistics in its leaderboard.

For the connected wallet:

| Wallet          | Survived | Died | Survival Rate |
| --------------- | -------: | ---: | ------------: |
| `0x5e5e...2ea6` |        2 |    0 |          100% |

The leaderboard therefore displayed:

**2 survived / 0 died / 100% survival rate**

for the connected wallet at the time of this execution record.

This provides application-level state readback corresponding to the recorded survival results.

### Leaderboard Evidence

<!-- INSERT SCREENSHOT HERE -->

---

# 12. Complete End-to-End Execution Record

The actual execution can be represented as follows:

```text
Rabby Wallet Connected
        ↓
GenLayer Studio Network
        ↓
Deployed Mars Survival Contract
        ↓
generate_scenario
        ↓
Transaction Submitted
        ↓
GenVM Execution: SUCCESS
        ↓
Consensus: Accepted
        ↓
Transaction: FINALIZED
        ↓
Actual Scenario Returned
        ↓
Scenario Read by Application
        ↓
Survival Strategy Submitted
        ↓
judge_survival
        ↓
Transaction Submitted
        ↓
GenVM Execution: SUCCESS
        ↓
Consensus: Accepted
        ↓
Equivalence Principle: SURVIVED
        ↓
Transaction: FINALIZED
        ↓
Return Value: SURVIVED
        ↓
Application Receives Judgment
        ↓
Leaderboard State Readback
        ↓
2 Survived / 0 Died / 100%
```

---

# 13. Transaction Evidence Summary

## Scenario Generation

**Method:** `generate_scenario`

**Transaction:**

`0x4f4d37b7b7a93d73a5c9d4c3947a7119f96ef290c4adc68ff0fa51ccbd655bc7`

**Explorer:**

https://explorer-studio.genlayer.com/tx/0x4f4d37b7b7a93d73a5c9d4c3947a7119f96ef290c4adc68ff0fa51ccbd655bc7

**Status:** `FINALIZED`

**Consensus:** `Accepted`

**GenVM:** `SUCCESS`

---

## Survival Judgment

**Method:** `judge_survival`

**Transaction:**

`0x53b166554c558e96158fda5bcb056ad8340465f991d700388ae4e4013d169dd0`

**Explorer:**

https://explorer-studio.genlayer.com/tx/0x53b166554c558e96158fda5bcb056ad8340465f991d700388ae4e4013d169dd0

**Status:** `FINALIZED`

**Consensus:** `Accepted`

**GenVM:** `SUCCESS`

**Equivalence Principle:** `SURVIVED`

**Return Value:** `SURVIVED`

---

# 14. Deployed Contract

**Contract Address:**

`0x86b811b139924dD49E6259A9329456C97e08783B`

**Explorer:**

https://explorer-studio.genlayer.com/address/0x86b811b139924dD49E6259A9329456C97e08783B

### Contract Evidence

<!-- INSERT SCREENSHOT HERE -->

---

# 15. Execution Video

A video recording of the application flow is provided as additional visual evidence.

The recording demonstrates the application-side execution flow, including:

* Wallet connection
* Scenario generation
* Scenario display
* Survival strategy submission
* Transaction execution
* GenLayer consensus
* Final judgment
* Result display

**Execution Video:**

https://drive.google.com/file/d/1suruKmHeP4V26O7kO3dER_7oOl_T2d0y/

### Video Evidence

<!-- INSERT SCREENSHOT HERE -->

---

# 16. Evidence Checklist

| Requirement            | Evidence                                  |
| ---------------------- | ----------------------------------------- |
| Wallet connection      | Rabby wallet + connected address          |
| Correct network        | GenLayer Studio Network                   |
| Deployed contract      | Contract address + Explorer               |
| Scenario generation    | Finalized `generate_scenario` transaction |
| Scenario output        | Actual returned scenario                  |
| Scenario readback      | Application screenshot                    |
| Strategy submission    | Finalized `judge_survival` transaction    |
| Submitted strategy     | Actual transaction input                  |
| GenVM execution        | `SUCCESS`                                 |
| Consensus              | `Accepted`                                |
| Finalization           | `FINALIZED`                               |
| Equivalence Principle  | `SURVIVED`                                |
| Final return value     | `SURVIVED`                                |
| Application judgment   | `SURVIVED`                                |
| State readback         | Leaderboard output                        |
| Visual execution proof | Execution video                           |

---

# 17. Conclusion

This document provides a concrete execution record of the Mars Survival application's complete flow on GenLayer Studio Network.

The evidence is based on actual finalized transactions rather than a description of the intended behavior.

The recorded execution demonstrates:

**Wallet Connection**

→ **Scenario Generation**

→ **GenVM Execution**

→ **GenLayer Consensus**

→ **Finalized Scenario**

→ **Scenario Readback**

→ **Survival Strategy Submission**

→ **GenVM Execution**

→ **GenLayer Consensus**

→ **Accepted Judgment**

→ **Equivalence Principle: SURVIVED**

→ **Finalized Transaction**

→ **Application Result Readback**

→ **Leaderboard State**

The two finalized transaction records provide independently verifiable blockchain evidence for the scenario generation and survival judgment steps.

The `judge_survival` transaction additionally contains the submitted strategy, a successful GenVM execution, an accepted consensus result, a `SURVIVED` equivalence output, and the final `SURVIVED` return value.

Together with the application screenshots and execution video, this provides a reproducible end-to-end execution record for the deployed Mars Survival application.
