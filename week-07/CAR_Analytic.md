# MITRE CAR Analytic — PowerShell Execution

## 1. Selected Analytic

- **CAR ID:** CAR-2014-04-003
- **Analytic Name:** Powershell Execution
- **Source:** https://car.mitre.org/analytics/CAR-2014-04-003/
- **Platform:** Windows
- **Data Type:** Process Creation

## 2. Analytic Description

The selected MITRE CAR analytic identifies PowerShell execution from non-interactive or unusual parent processes.

PowerShell is commonly used by administrators, but attackers may also use it to execute commands.

## 3. Original CAR Detection Logic

The original analytic searches process creation events where:

- The executable is `powershell.exe`.
- The parent executable is not `explorer.exe`.

This can identify PowerShell launched outside a typical interactive desktop workflow.

## 4. Required Data Fields

| Field | Description |
|---|---|
| process.name | Name of the executable |
| process.parent.name | Name of the parent process |
| process.command_line | Command-line arguments |
| host.name | Windows computer name |
| @timestamp | Event timestamp |

The first two process fields are essential for the adapted detection logic.

## 5. Elastic KQL Implementation

`event.category : "process" and event.type : "start" and process.name : "powershell.exe" and process.parent.name : * and not process.parent.name : "explorer.exe"`

This is an Elastic adaptation of the original CAR analytic.

## 6. MITRE ATT&CK Mapping

- **Tactic:** Execution
- **Technique:** T1059 — Command and Scripting Interpreter
- **Sub-technique:** T1059.001 — PowerShell

## 7. Investigation Procedure

For every matching event:

1. Examine the timestamp.
2. Identify the Windows host.
3. Check the parent process.
4. Review the PowerShell command line.
5. Identify the associated user.
6. Determine whether the activity was authorized.

## 8. False Positives

Legitimate scripts, scheduled tasks, system management software, and administrator tools may launch PowerShell without using explorer.exe as the parent.

A detection match is not proof of compromise.

## 9. Conclusion

The MITRE CAR analytic provides a reusable method for investigating potentially unusual PowerShell execution.

The detection requires process creation telemetry and must be validated against actual endpoint logs.

## References

- https://car.mitre.org/analytics/CAR-2014-04-003/
- https://attack.mitre.org/techniques/T1059/001/
