# Week 5 — Threat Hunting Concept

## 1. Introduction

Threat hunting is a proactive cybersecurity process used to search for suspicious or malicious activity that may not have been detected by existing security tools.

Instead of waiting for an alert, a threat hunter actively searches through logs, endpoint data, and network activity.

---

## 2. Threat Hunting Models

Two common threat hunting approaches are:

### Intel-Driven Hunting

Intel-driven hunting starts with known threat intelligence.

Examples:

- Malicious IP addresses
- Domains
- File hashes
- Malware indicators
- Known attacker TTPs

Example:

A threat intelligence feed reports a malicious IP address.

The hunter searches SIEM logs to determine whether any internal computer communicated with this IP.

Threat Intelligence → IOC → Search Logs → Investigation

---

### Hypothesis-Driven Hunting

Hypothesis-driven hunting starts with an assumption about suspicious attacker behavior.

Example hypothesis:

"An attacker may use PowerShell to execute encoded or hidden malicious commands on a Windows endpoint."

The hunter creates queries to search logs for evidence supporting or rejecting this hypothesis.

Hypothesis → Data → Query → Investigation → Result

---

## 3. Selected Hunting Approach

For this project, we selected hypothesis-driven threat hunting.

Our scenario focuses on suspicious PowerShell activity on Windows systems.

PowerShell is a legitimate Windows administration tool, but attackers can also abuse it to execute commands, download files, or run encoded scripts.

MITRE ATT&CK identifies PowerShell as technique T1059.001 under Command and Scripting Interpreter.

---

## 4. Hunting Objective

The objective of this hunt is to identify suspicious PowerShell execution by searching Windows process creation logs.

We will search for indicators such as:

- powershell.exe
- -EncodedCommand
- -enc
- -ExecutionPolicy Bypass
- -WindowStyle Hidden
- download commands
- unusual PowerShell process execution

The results will then be investigated to determine whether the activity is legitimate or potentially malicious.
