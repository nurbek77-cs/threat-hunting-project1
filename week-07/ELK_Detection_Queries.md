# Week 7 — Elastic SIEM Detection Queries

## Objective

Implement and test the MITRE CAR-2014-04-003 PowerShell Execution analytic using Elastic Discover.

## Query 1 — Identify Process Creation Events

```kql
event.category : "process" and event.type : "start"
```

**Purpose:** Check whether process creation telemetry is available.

## Query 2 — Find PowerShell Process Execution

```kql
process.name : "powershell.exe"
```

**Purpose:** Identify recorded PowerShell process executions.

## Query 3 — MITRE CAR Analytic

```kql
event.category : "process" and event.type : "start" and process.name : "powershell.exe" and process.parent.name : * and not process.parent.name : "explorer.exe"
```

**Purpose:** Identify PowerShell processes launched by parent processes other than explorer.exe.

This query adapts the original MITRE CAR detection logic to Elastic Common Schema fields.

## Query 4 — Existing PowerShell Event Telemetry

```kql
data_stream.dataset : "windows.powershell"
```

**Purpose:** Verify that Windows PowerShell event logs are available.

This query does not implement the original process-parent CAR detection.

## Query 5 — PowerShell Bypass Investigation

```kql
data_stream.dataset : "windows.powershell" and "Bypass"
```

**Purpose:** Search existing PowerShell events for a potentially interesting execution policy bypass indicator.

This is a supplementary hunting query, not the original CAR analytic.

## Data Requirements

The CAR detection requires process creation events containing the executable and parent executable.

Sysmon Event ID 1 is one possible source of this telemetry.

## Results

Record the actual number of matching events, screenshots, timestamps, and relevant fields after executing the queries.

Do not interpret missing process events as proof that no PowerShell execution occurred.

## Conclusion

MITRE CAR provides detection logic that can be translated into Elastic KQL.

Successful implementation depends on collecting the required endpoint telemetry and validating the query against real events.

## Reference

https://car.mitre.org/analytics/CAR-2014-04-003/
