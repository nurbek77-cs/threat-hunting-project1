# Week 7 — Multi-Interpreter Detection Using Elastic SIEM

## 1. Introduction

During Week 7, we studied MITRE CAR analytics and adapted detection logic to Elastic SIEM.

The original selected analytic was CAR-2014-04-003 — PowerShell Execution.

To extend the project, we added custom detection queries for Python, JavaScript, and Windows Command Shell.

## 2. Objective

The objective is to detect and investigate execution activity involving multiple command and scripting interpreters.

The selected interpreters are:

- PowerShell
- Python
- JavaScript using Windows Script Host
- Windows Command Shell

## 3. MITRE ATT&CK Mapping

| Interpreter | ATT&CK Technique | Tactic |
|---|---|---|
| PowerShell | T1059.001 | Execution |
| Python | T1059.006 | Execution |
| JavaScript | T1059.007 | Execution |
| Windows CMD | T1059.003 | Execution |

## 4. Data Source

The detection uses process creation telemetry collected from a Windows endpoint.

Sysmon Event ID 1 records process creation events.

Elastic Agent can collect Sysmon events through the Windows integration.

The expected dataset is:

`windows.sysmon_operational`

Useful fields include:

- process.name
- process.command_line
- process.parent.name
- host.name
- user.name
- event.code
- @timestamp

## 5. Query 1 — Search for Process Creation Events

`data_stream.dataset : "windows.sysmon_operational" and event.code : "1"`

Purpose:

Identify Windows process creation events collected by Sysmon.

## 6. Query 2 — PowerShell Detection

`data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : "powershell.exe"`

Purpose:

Identify PowerShell process executions.

ATT&CK mapping: T1059.001.

## 7. Query 3 — Python Detection

`data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : ("python.exe" or "python3.exe" or "py.exe")`

Purpose:

Identify Python interpreter executions.

ATT&CK mapping: T1059.006.

## 8. Query 4 — JavaScript Detection

`data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : ("cscript.exe" or "wscript.exe" or "node.exe")`

Purpose:

Identify Windows Script Host or Node.js interpreter executions.

These process names are investigation candidates. A matching process does not prove that JavaScript was executed; command-line arguments and script paths must also be reviewed.

ATT&CK mapping for confirmed JavaScript execution: T1059.007.

## 9. Query 5 — Windows CMD Detection

`data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : "cmd.exe"`

Purpose:

Identify Windows Command Shell executions.

ATT&CK mapping: T1059.003.

## 10. Query 6 — Combined Detection

`data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : ("powershell.exe" or "python.exe" or "python3.exe" or "py.exe" or "cscript.exe" or "wscript.exe" or "node.exe" or "cmd.exe")`

Purpose:

Search for different command and scripting interpreters using one KQL query.

## 11. Query 7 — Unusual Parent Process Detection

`data_stream.dataset : "windows.sysmon_operational" and event.code : "1" and process.name : ("powershell.exe" or "python.exe" or "python3.exe" or "cscript.exe" or "wscript.exe" or "node.exe" or "cmd.exe") and process.parent.name : * and not process.parent.name : "explorer.exe"`

Purpose:

Identify interpreters launched by processes other than Windows Explorer.

This query extends the parent-process hunting concept to multiple interpreters.

It is a custom analytic inspired by the investigation approach used for PowerShell; it is not an official MITRE CAR analytic covering all these interpreters.

## 12. Investigation Workflow

When matching activity is found, investigate:

1. Timestamp of the event.
2. Process name.
3. Parent process.
4. Command-line arguments.
5. Script path.
6. Username and hostname.
7. Other related endpoint or network events.

## 13. False Positives and Limitations

PowerShell, Python, JavaScript, and CMD are used by legitimate administrators and developers.

Process execution alone does not indicate malicious activity.

Searching for unusual parent processes may produce false positives from legitimate automation, terminals, scheduled tasks, and development tools.

Missing process creation logs may cause false negatives.

## 14. Results

Execution and detection results must be recorded using real Elastic Discover screenshots.

If a query returns no matching events, verify the logging configuration and the time range before drawing conclusions.

## 15. Conclusion

The extended Week 7 detection demonstrates how Elastic SIEM can support threat hunting across multiple scripting and command interpreters.

The exercise combines the original MITRE CAR PowerShell analytic with additional custom hunting queries mapped to MITRE ATT&CK.

## References

- https://car.mitre.org/analytics/CAR-2014-04-003/
- https://attack.mitre.org/techniques/T1059/
- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
- https://www.elastic.co/docs/
