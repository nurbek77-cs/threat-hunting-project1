# Week 8 — MITRE ATT&CK Mapping

## Overview

This document maps the proposed adversary emulation scenario to the MITRE ATT&CK framework.

## Technique Mapping

| Phase | Tactic | Technique ID | Technique Name | Practical Validation |
|---|---|---|---|---|
| 1 | Initial Access | T1566.001 | Spearphishing Attachment | Harmless local training artifact only |
| 2 | Execution | T1059.001 | PowerShell | Benign PowerShell command |
| 3 | Persistence | T1053.005 | Scheduled Task | Temporary scheduled task registration and removal |
| 4 | Exfiltration | T1567.002 | Exfiltration to Cloud Storage | Conceptual step only; no real external transfer |

## Phase Analysis

### Initial Access — T1566.001

The hypothetical attacker attempts to gain entry by sending a malicious email attachment.

In this exercise, the phase is documented but no real phishing is performed.

### Execution — T1059.001

The hypothetical attacker executes commands using PowerShell.

A harmless PowerShell test is performed on the authorized endpoint.

### Persistence — T1053.005

The hypothetical attacker establishes persistence using the Windows Task Scheduler.

A temporary benign task is used for the demonstration and then removed.

### Exfiltration — T1567.002

The hypothetical attacker transfers data to external cloud storage.

No real exfiltration is conducted. Instead, the lab produces synthetic data and a local mock output artifact.

## Related Techniques from Previous Weeks

Previous assignments investigated additional interpreters:

- T1059.003 — Windows Command Shell
- T1059.006 — Python
- T1059.007 — JavaScript

These are possible alternative execution techniques but are not required for the core Week 8 scenario.

## Conclusion

The plan covers Initial Access, Execution, Persistence, and Exfiltration.

The mapping provides a structured way to understand the proposed attack sequence and associate observable behavior with monitoring requirements.

## References

- https://attack.mitre.org/
- https://attack.mitre.org/techniques/T1566/001/
- https://attack.mitre.org/techniques/T1059/001/
- https://attack.mitre.org/techniques/T1053/005/
- https://attack.mitre.org/techniques/T1567/002/
