# Splunk Hunt Queries — Suspicious PowerShell

## Query 1 — Find PowerShell Execution

```spl
index=* 
("powershell.exe" OR "pwsh.exe")
