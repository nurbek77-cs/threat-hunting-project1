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
