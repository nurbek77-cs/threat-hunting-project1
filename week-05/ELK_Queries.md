# Elastic Threat Hunting Queries

## Environment

The threat hunt was performed using Elastic Discover.

PowerShell logs were collected from a Windows endpoint using Elastic Agent and the Windows integration.

---

## Query 1 — Find Windows PowerShell Events

```kql
data_stream.dataset : *powershell*
