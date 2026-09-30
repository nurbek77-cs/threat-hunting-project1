# Week 4 — Cyber Kill Chain Analysis

## 1. Introduction

This week focuses on analyzing a real-world cyberattack using the Cyber Kill Chain model and mapping the attack activities to MITRE ATT&CK techniques.

For this analysis, we selected the WannaCry ransomware attack of 2017.

WannaCry was a Windows ransomware attack that spread rapidly across networks by exploiting a vulnerability in SMBv1. The malware used the EternalBlue exploit to spread to vulnerable systems.

The purpose of this analysis is to understand how the attack progressed through the Cyber Kill Chain and identify the corresponding MITRE ATT&CK techniques.

---

## 2. Cyber Kill Chain

The Cyber Kill Chain was developed by Lockheed Martin to describe the stages of a cyber intrusion.

The seven stages are:

1. Reconnaissance
2. Weaponization
3. Delivery
4. Exploitation
5. Installation
6. Command and Control
7. Actions on Objectives

---

# 3. WannaCry Attack Analysis

## 3.1 Reconnaissance

During reconnaissance, attackers identify potential targets and vulnerable systems.

In the WannaCry case, the malware scanned networks for systems that were accessible through SMB and potentially vulnerable to the MS17-010 vulnerability.

The malware also searched for remote systems that it could attempt to infect.

### Threat Hunting Evidence

Security analysts could look for:

- SMB traffic
- TCP port 445 scanning
- Large numbers of connection attempts
- Connections to many internal hosts

### MITRE ATT&CK

**T1018 — Remote System Discovery**

WannaCry scanned local networks for remote systems that it could attempt to exploit.

---

## 3.2 Weaponization

Weaponization is the stage where an attacker prepares a malicious payload and the exploit required to compromise the target.

WannaCry combined ransomware functionality with a worm-like propagation mechanism.

The attack used the EternalBlue exploit to target the SMBv1 vulnerability in Windows systems.

### Threat Hunting Evidence

Analysts can investigate:

- Exploit-related traffic
- Suspicious SMB activity
- Files associated with WannaCry
- Known malware hashes

### MITRE ATT&CK

**T1210 — Exploitation of Remote Services**

WannaCry used an SMBv1 exploit to spread to remote systems.

---

## 3.3 Delivery

Delivery is the stage where the malicious payload reaches the target.

Unlike a typical phishing attack, WannaCry mainly spread automatically through vulnerable SMB services.

The malware searched for vulnerable Windows systems and attempted to exploit them.

### Threat Hunting Evidence

Analysts can monitor:

- TCP port 445 traffic
- SMB connections between unusual hosts
- Large numbers of SMB connection attempts
- Unexpected SMB traffic from workstation systems

### MITRE ATT&CK

**T1210 — Exploitation of Remote Services**

The SMB service was used as the path for spreading the malware to remote systems.

---

## 3.4 Exploitation

In the exploitation stage, the attacker takes advantage of a vulnerability.

WannaCry exploited the MS17-010 vulnerability in Windows SMBv1 using the EternalBlue exploit.

Successful exploitation allowed the malware to execute code on vulnerable systems.

### Threat Hunting Evidence

Indicators include:

- Suspicious SMB packets
- Exploitation attempts against TCP/445
- Unexpected process creation
- Connections from infected systems to other systems

### MITRE ATT&CK

**T1210 — Exploitation of Remote Services**

WannaCry exploited SMBv1 to compromise and spread to other systems.

---

## 3.5 Installation

After successful exploitation, WannaCry installed its malicious components on the compromised system.

WannaCry created a Windows service named:

`mssecsvc2.0`

This allowed the malware to execute as a Windows service.

### Threat Hunting Evidence

Security analysts can monitor:

- New Windows services
- Suspicious service creation
- Unknown executable files
- Changes to system directories

### MITRE ATT&CK

**T1543.003 — Create or Modify System Process: Windows Service**

MITRE reports that WannaCry creates the `mssecsvc2.0` Windows service.

---

## 3.6 Command and Control

Command and Control (C2) allows malware to communicate with infrastructure controlled by the attacker.

WannaCry used Tor for some command and control traffic.

### Threat Hunting Evidence

Analysts can investigate:

- Tor-related network traffic
- Unexpected encrypted connections
- Connections to suspicious external infrastructure
- Unusual outbound network traffic

### MITRE ATT&CK

**T1573.002 — Encrypted Channel: Asymmetric Cryptography**

MITRE documents that WannaCry uses Tor for command and control traffic and routes a custom cryptographic protocol through the Tor circuit.

---

## 3.7 Actions on Objectives

The final stage is when the attacker performs the intended malicious actions.

WannaCry encrypted user files and displayed a ransom demand.

The malware also attempted to delete or disable system recovery mechanisms.

### Threat Hunting Evidence

Analysts can monitor:

- Large numbers of file modifications
- File encryption
- Ransomware notes
- Shadow copy deletion
- Recovery configuration changes
- Suspicious use of administrative utilities

### MITRE ATT&CK

**T1486 — Data Encrypted for Impact**

WannaCry encrypts user files and demands payment.

**T1490 — Inhibit System Recovery**

WannaCry can use Windows utilities such as `vssadmin`, `wbadmin`, `bcdedit` and `wmic` to delete or disable recovery features.

---

# 4. Kill Chain and MITRE ATT&CK Mapping

| Kill Chain Stage | WannaCry Activity | MITRE ATT&CK |
|---|---|---|
| Reconnaissance | Scanning remote systems | T1018 |
| Weaponization | Malware combined with SMB exploit | T1210 |
| Delivery | SMB-based propagation | T1210 |
| Exploitation | Exploitation of MS17-010 | T1210 |
| Installation | Creates Windows service | T1543.003 |
| Command and Control | Uses Tor for C2 | T1573.002 |
| Actions on Objectives | Encrypts files | T1486 |
| Actions on Objectives | Disables recovery | T1490 |

---

# 5. Threat Hunting Opportunities

The WannaCry attack provides several opportunities for threat hunting.

Security analysts can search for:

1. Unusual SMB traffic.
2. Large numbers of connections to TCP port 445.
3. New Windows services.
4. Suspicious file encryption activity.
5. Attempts to delete shadow copies.
6. Unexpected Tor traffic.
7. Hosts scanning many other internal systems.

A simplified threat hunting process is:

Network Traffic
→ Identify suspicious SMB activity
→ Identify infected host
→ Investigate processes
→ Check Windows services
→ Search for ransomware behavior
→ Map findings to MITRE ATT&CK

---

# 6. Conclusion

The WannaCry attack demonstrates how a cyberattack can be analyzed using the Cyber Kill Chain.

The attack used SMB exploitation to spread between vulnerable Windows systems, created a Windows service, communicated through Tor and encrypted user files.

Mapping the attack to MITRE ATT&CK helps security analysts understand the techniques used by the malware and identify possible detection opportunities.

This analysis can be used as a foundation for practical threat hunting in the next stages of the project.
