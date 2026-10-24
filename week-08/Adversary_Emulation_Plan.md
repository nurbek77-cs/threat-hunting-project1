# Week 8 — Adversary Emulation Plan

## 1. Scenario Overview

This adversary emulation plan describes a hypothetical attack against a Windows workstation.

The attacker aims to obtain initial access, execute commands, establish persistence, and exfiltrate information.

The plan is based on MITRE ATT&CK and is intended for a controlled educational environment.

## 2. Scope and Rules of Engagement

**Target:** Authorized Windows lab endpoint (HOME-PC)

**Monitoring:** Microsoft Sysmon, Elastic Agent, Elastic Cloud

**Allowed activities:**
- Creating harmless training files
- Executing benign commands
- Creating and removing a clearly labeled test scheduled task
- Copying synthetic data within a local lab directory
- Investigating generated logs

**Excluded activities:**
- Sending real phishing emails
- Deploying malware
- Stealing credentials
- Accessing other users' data
- Sending data to an external service
- Leaving persistent tasks installed after testing

## 3. Phase 1 — Initial Access

**Tactic:** Initial Access

**Technique:** T1566.001 — Phishing: Spearphishing Attachment

### Hypothetical Attacker Behavior

An attacker sends a phishing email containing a malicious attachment. The attacker attempts to persuade the recipient to open the attachment and execute its content.

### Safe Emulation

Create a harmless local text file representing a received attachment. Do not send an email or execute malicious content.

### Detection Opportunities

- Email security logs
- Attachment inspection
- User activity
- Process execution after an attachment is opened

### Expected Result

A training artifact is created. The initial access technique is represented in the plan but no actual initial compromise occurs.

## 4. Phase 2 — Execution

**Tactic:** Execution

**Technique:** T1059.001 — PowerShell

### Hypothetical Attacker Behavior

After gaining access, an attacker may use PowerShell to execute commands or scripts on the endpoint.

### Safe Emulation

Execute a benign PowerShell command that prints a training message.

### Detection Opportunities

- Sysmon Event ID 1
- PowerShell event logs
- Process command-line monitoring
- Parent process analysis

### Expected Result

The command completes and a PowerShell process creation event may be observable in Sysmon.

## 5. Phase 3 — Persistence

**Tactic:** Persistence

**Technique:** T1053.005 — Scheduled Task

### Hypothetical Attacker Behavior

The attacker creates a scheduled task to maintain repeated execution on the compromised endpoint.

### Safe Emulation

Create a clearly named temporary scheduled task that executes only a harmless echo command.

Schedule it for the following day to prevent execution during testing.

Inspect the task and remove it immediately after collecting evidence.

### Detection Opportunities

- Windows Security Event ID 4698, if auditing is enabled
- Task Scheduler operational logs
- Process creation events
- Scheduled task inventory and changes

### Expected Result

A temporary training task is registered, verified, and removed.

## 6. Phase 4 — Exfiltration

**Tactic:** Exfiltration

**Technique:** T1567.002 — Exfiltration to Cloud Storage

### Hypothetical Attacker Behavior

After collecting information, the attacker attempts to transfer files to an external cloud storage service.

### Safe Emulation

Create a synthetic text file containing no confidential information.

Copy the file to a separate local directory named `mock_outbox` to represent preparation for transfer.

No network upload is performed.

### Detection Opportunities

- File access telemetry
- Process command lines
- Outbound network connections
- Web proxy logs
- Cloud service audit events
- Unusual upload volume

### Expected Result

Only a local copy of synthetic data is created.

**Important:** The local copy is not a successful implementation of T1567.002. Real cloud exfiltration remains hypothetical. The local copy is an educational staging artifact.

## 7. ATT&CK Attack Flow

Initial Access (T1566.001)

↓

Execution (T1059.001)

↓

Persistence (T1053.005)

↓

Exfiltration (T1567.002 — hypothetical external transfer)

## 8. Telemetry and Validation

The defender should investigate:

- Windows host identity
- Process creation events
- Command-line arguments
- Parent-child process relationships
- Scheduled task registration and deletion
- File activity where logging is available
- Network activity only if a network transfer is intentionally tested in an authorized environment

## 9. Success Criteria

1. The full four-phase scenario is documented.
2. Each phase is mapped to the correct ATT&CK tactic and technique.
3. The safe Execution simulation produces visible output.
4. The temporary scheduled task is created and removed.
5. Synthetic data is copied to a local mock directory.
6. Relevant events are investigated in Elastic where telemetry is available.
7. No malicious activity or real exfiltration is performed.

## 10. Cleanup

Remove the training scheduled task and optionally remove the temporary local lab files.

Confirm that no scheduled task or unexpected service remains after testing.

## 11. Conclusion

This adversary emulation plan demonstrates how several attacker behaviors can be organized into a sequence aligned with MITRE ATT&CK.

The practical exercise uses harmless artifacts to illustrate the sequence while preserving a clear distinction between hypothetical adversary actions and actions actually performed in the laboratory.

## References

- https://attack.mitre.org/techniques/T1566/001/
- https://attack.mitre.org/techniques/T1059/001/
- https://attack.mitre.org/techniques/T1053/005/
- https://attack.mitre.org/techniques/T1567/002/
