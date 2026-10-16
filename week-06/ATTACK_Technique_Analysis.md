# Week 6 — MITRE ATT&CK Technique Analysis

## 1. Introduction

MITRE ATT&CK is a knowledge base of adversary tactics, techniques, and procedures (TTPs) based on real-world observations.

The framework helps cybersecurity analysts understand how attackers operate, identify suspicious behavior, and develop threat hunting and detection strategies.

The objective of this assignment is to study a specific MITRE ATT&CK technique, simulate related activity in a controlled environment, and map the results to ATT&CK.

## 2. Understanding Tactics, Techniques, and Procedures

### Tactics

Tactics describe **why** an attacker performs an action.

Examples include:

- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Defense Evasion
- Credential Access
- Discovery
- Command and Control

### Techniques

Techniques describe **how** an attacker achieves a tactical objective.

For example, attackers may use PowerShell to execute commands on a compromised Windows computer.

### Procedures

Procedures describe the specific implementation of a technique, such as executing a particular PowerShell command.

## 3. Selected MITRE ATT&CK Technique

For this assignment, we selected:

**T1059.001 — Command and Scripting Interpreter: PowerShell**

| Attribute | Description |
|---|---|
| Framework | MITRE ATT&CK Enterprise |
| Tactic | Execution |
| Parent Technique | T1059 — Command and Scripting Interpreter |
| Sub-technique | T1059.001 — PowerShell |
| Platform | Windows |
| Data Source | Windows PowerShell event logs |
| Detection Platform | Elastic Stack |

Official reference:

https://attack.mitre.org/techniques/T1059/001/

## 4. Technique Description

PowerShell is a command-line shell and scripting environment developed for Windows administration and automation.

System administrators use PowerShell to manage processes, services, files, and system configurations.

However, attackers may abuse PowerShell to execute malicious commands and scripts.

Examples of potentially suspicious PowerShell behavior include:

- Execution policy bypass
- Encoded commands
- Hidden PowerShell execution
- Downloading scripts from external servers
- Running unusual scripts

These behaviors require additional investigation because they may also occur during legitimate administrative activity.

## 5. Attack Simulation

We selected a harmless PowerShell command to simulate an execution pattern that can be investigated through Windows event logs.

Command:

`powershell.exe -ExecutionPolicy Bypass -Command "Write-Output 'Week 6 ATTACK Simulation'"`

### Explanation

- `powershell.exe` starts a PowerShell process.
- `-ExecutionPolicy Bypass` sets the execution policy for the new PowerShell session.
- `-Command` specifies the command to execute.
- `Write-Output` displays a test message.

Expected output:

`Week 6 ATTACK Simulation`

The command does not execute malware, download external files, or modify sensitive system settings.

## 6. Threat Hunting Environment

The following tools were used:

- Windows endpoint
- Windows PowerShell
- Elastic Agent
- Windows Integration
- Elastic Cloud
- Elastic Discover
- Kibana Query Language (KQL)

Elastic Agent collects Windows PowerShell events and forwards them to Elastic Cloud for analysis.

## 7. Detection and Investigation

### Query 1 — Identify PowerShell Events

`data_stream.dataset : "windows.powershell"`

This query identifies PowerShell events collected from the Windows endpoint.

### Query 2 — Search for Execution Policy Bypass

`data_stream.dataset : "windows.powershell" and "Bypass"`

This query searches for the keyword `Bypass` in collected PowerShell events.

A matching event is a starting point for investigation, not proof of malicious activity.

### Additional Investigation

For matching events, analysts should examine:

- Event timestamp
- Hostname
- Username, if available
- Event message
- PowerShell command details, if logged
- Related process activity

## 8. MITRE ATT&CK Mapping

| Observed or Simulated Activity | ATT&CK Tactic | ATT&CK Technique | Explanation |
|---|---|---|---|
| PowerShell command execution | Execution | T1059.001 | PowerShell is used to execute a command |
| PowerShell execution with `-ExecutionPolicy Bypass` | Execution | T1059.001 | Demonstrates a PowerShell execution pattern worth investigating |
| Searching PowerShell event logs | Detection activity | T1059.001 | Defensive investigation of behavior associated with the technique |

The detection activity in the final row is a defender action, not an adversary tactic.

## 9. Results and Findings

The Windows endpoint was connected to Elastic Cloud through Elastic Agent.

PowerShell events were successfully collected in the `windows.powershell` dataset.

During the earlier threat hunting exercise, a query searching for the keyword `Bypass` returned matching events.

The Week 6 simulation should be validated separately by comparing the event timestamp and available command details with the newly executed test.

## 10. Security Recommendations

Organizations can improve PowerShell monitoring by:

1. Enabling PowerShell Script Block Logging where appropriate.
2. Collecting process creation events.
3. Monitoring unusual PowerShell command-line arguments.
4. Investigating unexpected parent processes.
5. Correlating PowerShell activity with other endpoint and network events.

## Additional MITRE ATT&CK Techniques

The Week 6 analysis was extended from PowerShell to four
command and scripting interpreters.

| Interpreter | ATT&CK ID | Description |
|---|---|---|
| PowerShell | T1059.001 | PowerShell command and script execution |
| Python | T1059.006 | Python interpreter execution |
| JavaScript | T1059.007 | JavaScript execution |
| Windows CMD | T1059.003 | Windows Command Shell execution |

Each interpreter may be used for legitimate purposes or
abused by adversaries.

We prepared harmless simulations for the four techniques
and documented the commands in Multi_Interpreter_Simulation.md.

## 11. Conclusion

This assignment demonstrates how MITRE ATT&CK can be applied to practical threat hunting.

We studied technique T1059.001, prepared a controlled PowerShell simulation, and developed KQL queries for investigating related Windows events.

The exercise shows how ATT&CK helps analysts connect observable endpoint behavior to documented adversary techniques.

## 12. References

1. MITRE ATT&CK — PowerShell (T1059.001): https://attack.mitre.org/techniques/T1059/001/
2. MITRE ATT&CK Enterprise Matrix: https://attack.mitre.org/matrices/enterprise/
3. Elastic Documentation: https://www.elastic.co/docs/
