# Week 4 — MITRE ATT&CK Mapping

## WannaCry

| Technique ID | Technique | WannaCry Activity |
|---|---|---|
| T1018 | Remote System Discovery | Scans remote systems |
| T1210 | Exploitation of Remote Services | Exploits SMBv1 |
| T1543.003 | Windows Service | Creates mssecsvc2.0 service |
| T1573.002 | Encrypted Channel | Uses Tor for C2 |
| T1486 | Data Encrypted for Impact | Encrypts user files |
| T1490 | Inhibit System Recovery | Disables recovery mechanisms |

## Explanation

WannaCry used several techniques that can be mapped to the MITRE ATT&CK framework.

The most important technique for propagation was T1210, Exploitation of Remote Services. WannaCry used an SMBv1 exploit to spread to vulnerable Windows systems.

For persistence/execution, WannaCry created the Windows service mssecsvc2.0, which corresponds to T1543.003.

For impact, WannaCry encrypted user files using T1486 and attempted to inhibit system recovery using T1490.
