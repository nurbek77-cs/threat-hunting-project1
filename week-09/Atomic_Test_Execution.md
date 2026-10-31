# Week 9 — Atomic Test Execution

## 1. Objective

Execute selected Atomic Red Team tests and analyze generated telemetry using Elastic SIEM.

## 2. Test Environment

- Endpoint: HOME-PC
- Operating System: Windows
- Framework: Atomic Red Team
- Monitoring: Sysmon
- SIEM: Elastic Cloud

## 3. Atomic Test 1

**Technique:** T1059.001 — PowerShell

**Test number:** 17

**Test name:** PowerShell Command Execution

**Description:**

This test uses an encoded and obfuscated PowerShell command to print a harmless message.

**Expected output:**

Hello, from PowerShell!

**Detection opportunities:**

- PowerShell process creation
- Encoded PowerShell command-line arguments
- Parent-child process relationships
- PowerShell event logs

## 4. Atomic Test 2

**Technique:** T1059.003 — Windows Command Shell

**Test number:** 2

**Test name:** Writes text to a file and displays it.

**Description:**

This test executes commands using cmd.exe to create a temporary file and display its contents.

**Expected output:**

Hello from the Windows Command Prompt!

**Detection opportunities:**

- CMD process creation
- Command-line arguments
- Temporary file creation, if file monitoring is enabled

## 5. SIEM Investigation

We use Elastic Discover and Kibana Query Language to investigate the generated events.

Important fields:

- event.code
- process.name
- process.command_line
- process.parent.name
- host.name
- @timestamp

## 6. Validation

For each executed test, compare:

1. Test execution time.
2. Expected test behavior.
3. Events collected by Sysmon.
4. Matching events in Elastic Discover.
5. Potential detection limitations.

## 7. Results

The actual execution status, number of matching events, and screenshots must be added after testing.

A successful test command does not automatically mean that the SIEM detected the behavior.

## 8. Cleanup

Run the cleanup procedure for any selected test that creates temporary artifacts.

## 9. Conclusion

Selected Atomic Red Team tests provide controlled activity that can be used to validate endpoint logging and threat hunting queries.

## References

- https://www.atomicredteam.io/docs/atomics/T1059.001
- https://www.atomicredteam.io/docs/atomics/T1059.003
