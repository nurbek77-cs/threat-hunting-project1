# Week 7 — MITRE CAR Analytics

## 1. Introduction

This week focuses on the MITRE Cyber Analytics Repository (CAR), a collection of analytics designed to identify potentially malicious behavior.

The objective is to select an existing CAR analytic, adapt it to our SIEM environment, and map it to the MITRE ATT&CK framework.

## 2. Selected CAR Analytic

- **Analytic ID:** CAR-2014-04-003
- **Name:** PowerShell Execution
- **Platform:** Windows
- **SIEM:** Elastic Cloud
- **Query Language:** Kibana Query Language (KQL)

Official source: https://car.mitre.org/analytics/CAR-2014-04-003/

## 3. Detection Concept

PowerShell is a legitimate Windows administration tool, but it can also be used by attackers.

The selected analytic examines PowerShell process execution, particularly executions launched by unexpected parent processes.

## 4. MITRE ATT&CK Mapping

| Tactic | Technique | ID |
|---|---|---|
| Execution | Command and Scripting Interpreter: PowerShell | T1059.001 |

## 5. Implementation

The analytic is adapted for Elastic Discover using KQL.

Process-based detection requires telemetry containing the process name and parent process name.

Our existing Windows PowerShell logs provide additional context but may not contain all required process creation fields.

## 6. Investigation Workflow

1. Select a CAR analytic.
2. Identify the required data fields.
3. Collect relevant Windows events.
4. Execute the adapted detection query.
5. Investigate matching processes.
6. Map the behavior to MITRE ATT&CK.
7. Document findings and limitations.

## 7. Results

The results will be documented after validating the available process telemetry and testing the detection query.

## 8. Conclusion

MITRE CAR provides reusable detection ideas that can be implemented in SIEM platforms.

This assignment demonstrates how a CAR analytic can be adapted to Elastic and used for hypothesis-driven threat hunting.

## References

- https://car.mitre.org/
- https://car.mitre.org/analytics/CAR-2014-04-003/
- https://attack.mitre.org/techniques/T1059/001/
