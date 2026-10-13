# Week 6 — MITRE ATT&CK Framework

## 1. Introduction

This week focuses on studying the MITRE ATT&CK framework, understanding tactics, techniques, and procedures (TTPs), and simulating an attacker technique in a controlled environment.

Our project focuses on threat hunting for suspicious Windows activity using Cyber Threat Intelligence and OSINT.

## 2. Selected ATT&CK Technique

- **Technique:** T1059 — Command and Scripting Interpreter
- **Sub-technique:** T1059.001 — PowerShell
- **Tactic:** Execution
- **Platform:** Windows

PowerShell is a legitimate Windows command-line and scripting environment. Attackers may abuse PowerShell to execute commands and scripts.

## 3. Attack Simulation

We selected a harmless PowerShell execution test.

Command:

`powershell.exe -ExecutionPolicy Bypass -Command "Write-Output 'Week 6 ATTACK Simulation'"`

The command runs PowerShell with an execution policy bypass parameter and prints a test message.

No malicious code is executed.

## 4. Tools Used

- Windows PowerShell
- Elastic Agent
- Elastic Cloud
- Elastic Discover
- KQL
- MITRE ATT&CK

## 5. Detection

PowerShell events are collected from the Windows endpoint through Elastic Agent.

KQL query:

`data_stream.dataset : "windows.powershell" and "Bypass"`

This query searches PowerShell events for the keyword `Bypass`.

## 6. MITRE ATT&CK Mapping

| Activity | ATT&CK Tactic | Technique |
|---|---|---|
| PowerShell command execution | Execution | T1059.001 — PowerShell |
| ExecutionPolicy Bypass test | Execution | T1059.001 — PowerShell |

## 7. Results

The experiment is designed to demonstrate how PowerShell execution can be investigated using Elastic Discover.

Screenshots of the command execution and Elastic search results will be added after testing.

## 8. Conclusion

This exercise demonstrates how MITRE ATT&CK can help analysts understand attacker techniques and map observable Windows activity to a known framework.

## References

- https://attack.mitre.org/techniques/T1059/001/
- https://attack.mitre.org/
