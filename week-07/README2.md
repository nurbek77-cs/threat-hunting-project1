## Multi-Interpreter Detection Extension

The detection scope was expanded beyond PowerShell.

We developed additional Elastic KQL queries for:

- T1059.001 — PowerShell
- T1059.006 — Python
- T1059.007 — JavaScript
- T1059.003 — Windows Command Shell

These queries use Windows process creation telemetry.

The original MITRE CAR-2014-04-003 analytic remains
focused on PowerShell. The additional interpreter queries
are custom hunting rules.

See [Multi-Interpreter Detection](Multi_Interpreter_Detection.md).
