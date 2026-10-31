# Week 10 — APT29 MITRE ATT&CK Mapping

## Objective

Map selected APT29 tactics, techniques, and procedures to the MITRE ATT&CK framework and identify relevant detection opportunities.

## ATT&CK Mapping Table

| Tactic | Technique | ID | Potential Data Source |
|---|---|---|---|
| Initial Access | Supply Chain Compromise: Compromise Software Supply Chain | T1195.002 | Software integrity and update logs |
| Execution | PowerShell | T1059.001 | Sysmon Event ID 1, PowerShell logs |
| Execution | Windows Command Shell | T1059.003 | Sysmon Event ID 1 |
| Persistence | Scheduled Task | T1053.005 | Windows Security and Task Scheduler logs |
| Defense Evasion | Masquerade Task or Service | T1036.004 | Scheduled task inventory and process logs |
| Command and Control | Web Protocols | T1071.001 | Network, DNS, proxy, and EDR telemetry |
| Collection | Remote Email Collection | T1114.002 | Exchange and cloud audit logs |

## Detection Queries in Elastic

### Query 1 — PowerShell

```kql
data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : "powershell.exe"
```

### Query 2 — Windows CMD

```kql
data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : "cmd.exe"
```

### Query 3 — Scheduled Task Utility

```kql
data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : "schtasks.exe"
```

This detects executions of the schtasks.exe utility but does not cover every method of creating scheduled tasks.

### Query 4 — Scheduled Task Registration

```kql
data_stream.dataset : "windows.security" and event.code : "4698"
```

This query requires the corresponding Windows Security auditing to be enabled.

## Detection Coverage

| Technique | Available in Our Lab | Additional Requirements |
|---|---|---|
| PowerShell execution | Supported by existing PowerShell/Sysmon telemetry | Examine command details |
| CMD execution | Supported by Sysmon when events are collected | Examine parent process |
| Scheduled task activity | Partial | Task Scheduler and Security auditing |
| Supply chain compromise | Not fully covered | Software integrity and update monitoring |
| Web-based C2 | Not fully covered | Network telemetry |
| Remote email collection | Not covered | Exchange/cloud audit logs |

## Interpretation

These queries identify potentially relevant behavior.

A matching process event does not establish that APT29 was responsible.

Group attribution requires a broader combination of behavioral evidence, infrastructure intelligence, campaign context, and other indicators.

## Conclusion

MITRE ATT&CK provides a structured method for connecting documented APT29 techniques to defensive monitoring capabilities.

Our current environment supports investigation of selected Windows execution behaviors, while other APT29 techniques require additional monitoring sources.

## References

- https://attack.mitre.org/groups/G0016/
- https://attack.mitre.org/campaigns/C0024/
