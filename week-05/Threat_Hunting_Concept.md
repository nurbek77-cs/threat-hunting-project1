# Threat Hunting Concept

## What is Threat Hunting?

Threat hunting is a proactive cybersecurity process used to search for suspicious or malicious activity inside an environment.

Unlike traditional alert-based monitoring, threat hunting does not always start with a security alert.

Instead, analysts actively investigate systems, logs, network activity, and endpoint telemetry.

## Intel-Driven Hunting

Intel-driven hunting starts with known threat intelligence.

Examples include:

- Malicious IP addresses
- Malicious domains
- Malware hashes
- Known attacker TTPs
- Indicators of Compromise (IOCs)

Example:

If threat intelligence identifies a malicious IP address, a threat hunter can search SIEM logs to determine whether any internal computer communicated with that IP.

## Hypothesis-Driven Hunting

Hypothesis-driven hunting starts with an assumption about possible attacker behavior.

Example hypothesis:

> An attacker may abuse PowerShell to execute suspicious commands.

The analyst then identifies the required data and searches the environment for evidence that supports or rejects the hypothesis.

## Selected Approach

For this assignment, we used hypothesis-driven threat hunting.

The hunt focuses on suspicious PowerShell activity on a Windows endpoint.
