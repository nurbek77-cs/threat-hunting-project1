# Week 8 — Adversary Emulation Plan

## 1. Introduction

This week focuses on creating an adversary emulation plan based on the MITRE ATT&CK framework.

The objective is to understand how attacker behavior can be represented as a sequence of tactics and techniques and how these activities could be investigated using a SIEM.

Our project is titled "Threat Hunting for Malicious Windows Activity using Cyber Threat Intelligence and OSINT."

## 2. Objective

Develop a simple adversary emulation plan covering:

1. Initial Access
2. Execution
3. Persistence
4. Exfiltration

Map each phase to MITRE ATT&CK techniques and identify useful detection opportunities.

## 3. Selected Scenario

A hypothetical attacker targets a Windows endpoint through a phishing attachment, executes a command, establishes persistence through a scheduled task, and attempts to exfiltrate data to cloud storage.

The scenario is documented as an educational exercise. No real phishing, malware deployment, credential theft, or external data exfiltration is required.

## 4. MITRE ATT&CK Mapping

| Phase | Tactic | Technique | ID |
|---|---|---|---|
| 1 | Initial Access | Phishing: Spearphishing Attachment | T1566.001 |
| 2 | Execution | Command and Scripting Interpreter: PowerShell | T1059.001 |
| 3 | Persistence | Scheduled Task/Job: Scheduled Task | T1053.005 |
| 4 | Exfiltration | Exfiltration Over Web Service: Exfiltration to Cloud Storage | T1567.002 |

## 5. Lab Environment

- Operating system: Windows
- Endpoint: HOME-PC
- Monitoring: Microsoft Sysmon
- Log collector: Elastic Agent
- SIEM: Elastic Cloud
- Investigation: Elastic Discover
- Query language: KQL
- Documentation: GitHub

## 6. Emulation Approach

The exercise uses a safe local simulation:

- Initial Access: Create a harmless local training artifact representing a phishing attachment.
- Execution: Run a benign PowerShell test command.
- Persistence: Create a scheduled task that only executes a harmless command, then remove it.
- Exfiltration: Create synthetic test data and copy it to a local mock collection directory. External cloud exfiltration remains a documented hypothetical step.

## 7. Detection Strategy

Windows events and Sysmon process creation telemetry are used to investigate observable activity.

Relevant information includes:

- Process name
- Command line
- Parent process
- Hostname
- Timestamp
- Scheduled task events, if available
- File creation events, if configured

## 8. Expected Outcome

The exercise should produce an ATT&CK-aligned emulation plan, safe simulation artifacts, and relevant security telemetry for analysis.

Observed events and actual test results should be documented separately from hypothetical attacker behavior.

## 9. Conclusion

Week 8 connects previously studied ATT&CK techniques and SIEM detection queries into a complete adversary emulation plan.

The exercise helps illustrate how threat hunting and adversary emulation can support the evaluation of endpoint visibility and security controls.

## References

- https://attack.mitre.org/
- https://attack.mitre.org/techniques/T1566/001/
- https://attack.mitre.org/techniques/T1059/001/
- https://attack.mitre.org/techniques/T1053/005/
- https://attack.mitre.org/techniques/T1567/002/
- https://caldera.readthedocs.io/en/stable/
