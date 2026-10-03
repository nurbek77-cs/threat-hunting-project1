# Hypothesis-Driven Hunt — Suspicious PowerShell Activity

## 1. Scenario

An attacker has potentially gained access to a Windows endpoint.

Instead of installing a new command-line tool, the attacker may abuse PowerShell to execute commands.

The attacker may attempt to hide the activity by using encoded commands, hidden windows, or execution policy bypasses.

---

## 2. Hunting Hypothesis

### Hypothesis

"If an attacker is using PowerShell for malicious execution, Windows process logs may contain suspicious PowerShell commands such as encoded commands, hidden execution, execution policy bypasses, or download commands."

---

## 3. Data Required

To test the hypothesis, we need Windows process execution data.

Possible data sources:

- Windows Security Event Logs
- Sysmon
- PowerShell logs
- Splunk Windows events

Important Windows events can include:

- Event ID 4688 — Process Creation
- Sysmon Event ID 1 — Process Creation
- PowerShell Event ID 4104 — Script Block Logging

---

## 4. Indicators to Hunt

We search for:

powershell.exe

-EncodedCommand

-enc

-ExecutionPolicy Bypass

-WindowStyle Hidden

Invoke-WebRequest

DownloadString

IEX

---

## 5. MITRE ATT&CK Mapping

Technique:

T1059.001 — PowerShell

Tactic:

Execution

The technique represents adversaries abusing PowerShell commands and scripts for execution.

---

## 6. Expected Result

The hunt should identify PowerShell executions that require further investigation.

Not every PowerShell command is malicious.

Therefore, suspicious results must be analyzed using additional context such as:

- User
- Host
- Parent process
- Command line
- Execution time
- Network connections
