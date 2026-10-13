# Week 6 — PowerShell Attack Simulation

## Objective

Simulate a PowerShell execution pattern and investigate it using Elastic SIEM.

## Step 1 — Execute Test Command

Open Windows PowerShell and execute:

`powershell.exe -ExecutionPolicy Bypass -Command "Write-Output 'Week 6 ATTACK Simulation'"`

Expected output:

`Week 6 ATTACK Simulation`

## Step 2 — Collect Windows Logs

Elastic Agent collects Windows PowerShell events and forwards them to Elastic Cloud.

## Step 3 — Search PowerShell Activity

Open Elastic Discover and select the `logs-*` data view.

Use the following KQL query:

`data_stream.dataset : "windows.powershell"`

## Step 4 — Hunt for Execution Policy Bypass

Use the KQL query:

`data_stream.dataset : "windows.powershell" and "Bypass"`

Investigate matching events, including timestamps, hostnames, and available command details.

## Step 5 — Map to MITRE ATT&CK

- Tactic: Execution
- Technique: T1059 — Command and Scripting Interpreter
- Sub-technique: T1059.001 — PowerShell

## Results

Results and screenshots will be documented after the simulation.

## Security Considerations

This is a controlled educational simulation. The test does not download malware, establish persistence, or access external systems.
