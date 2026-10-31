# Week 10 — Learning APT Techniques

## 1. Introduction

This week focuses on studying the tactics, techniques, and procedures (TTPs) of an Advanced Persistent Threat (APT) group.

We selected APT29 because its documented behavior includes Windows command execution, persistence mechanisms, credential abuse, and command-and-control activity.

## 2. Selected Threat Group

- Group: APT29
- MITRE ATT&CK Group ID: G0016
- Alternative Names: Cozy Bear, Midnight Blizzard, NOBELIUM
- Main Motivation: Cyber espionage
- Associated Campaign: SolarWinds Compromise

## 3. Objectives

- Understand what an APT group is.
- Research documented APT29 activities.
- Analyze relevant TTPs.
- Map techniques to MITRE ATT&CK.
- Identify detection opportunities using Elastic SIEM.
- Connect previous threat hunting exercises to real-world threat intelligence.

## 4. Methodology

1. Select an APT group.
2. Research the group's background.
3. Study its known campaigns.
4. Identify ATT&CK techniques.
5. Analyze techniques relevant to Windows.
6. Map the identified techniques to ATT&CK tactics.
7. Propose defensive monitoring queries.

## 5. Selected Techniques

| Technique | ATT&CK ID |
|---|---|
| Supply Chain Compromise | T1195.002 |
| PowerShell | T1059.001 |
| Windows Command Shell | T1059.003 |
| Scheduled Task | T1053.005 |
| Masquerade Task or Service | T1036.004 |
| Web Protocols | T1071.001 |
| Remote Email Collection | T1114.002 |

These techniques have been documented in APT29 activity or associated campaigns. They do not necessarily belong to one continuous attack sequence.

## 6. Connection to Our Project

Previous assignments demonstrated PowerShell and CMD execution and their detection through Sysmon and Elastic.

This week connects those techniques to documented adversary behavior.

## 7. Conclusion

The APT29 case study helps demonstrate how threat intelligence and MITRE ATT&CK can inform threat hunting hypotheses and detection engineering.

## References

- https://attack.mitre.org/groups/G0016/
- https://attack.mitre.org/campaigns/C0024/
- https://attack.mitre.org/
