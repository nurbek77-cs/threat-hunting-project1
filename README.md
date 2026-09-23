# Threat Hunting for Malicious Windows Activity using CTI, OSINT and MISP

## Project Overview

This project focuses on **Cyber Threat Intelligence (CTI)** and **Threat Hunting**. The main goal is to collect, analyze, enrich, and correlate cyber threat indicators using open-source intelligence and security frameworks.

# Project Goal
The goal of this project is to investigate malicious activity on Windows systems using Cyber Threat Intelligence (CTI), Open Source Intelligence (OSINT), Indicators of Compromise (IOCs), and MITRE ATT&CK.

The project covers the first three weeks of our threat hunting methodology:

* **Week 1:** Cyber Threat Intelligence Fundamentals
* **Week 2:** OSINT and IOC Data Collection
* **Week 3:** Data Processing, Enrichment, and MITRE ATT&CK Mapping

---

# Week 1 — Cyber Threat Intelligence Fundamentals

During Week 1, we studied the basic concepts of Cyber Threat Intelligence.

### Topics Covered

* CTI definition
* CTI levels: Strategic, Operational, Tactical, and Technical
* IOC and TTP concepts
* Cyber threat classification
* Threat intelligence sources
* Introduction to MITRE ATT&CK
* Introduction to OSINT

### Main Threat Types

| Threat           | Example IOC      |
| ---------------- | ---------------- |
| Malware          | File hash        |
| Phishing         | URL / Domain     |
| Ransomware       | Hash / Domain    |
| Botnet           | C2 IP            |
| Credential Theft | Suspicious login |
| DDoS             | Source IP        |
| Exploitation     | IP / Request     |

### CTI Sources

We identified several open sources that can be used for threat intelligence:

* MITRE ATT&CK
* ENISA
* VirusTotal
* MISP OSINT feeds
* Shodan
* Abuse.ch

### Week 1 Result

At the end of Week 1, we created:

* CTI glossary
* Threat classification
* List of intelligence sources
* Initial threat hunting methodology

---

# Week 2 — OSINT and IOC Data Collection

Week 2 focuses on collecting technical indicators from publicly available sources.

## OSINT

**OSINT (Open Source Intelligence)** is the collection and analysis of information from publicly available sources.

Our main OSINT sources are:

1. VirusTotal
2. Shodan
3. MISP OSINT feeds
4. MITRE ATT&CK
5. ENISA

## VirusTotal

VirusTotal is used to investigate:

* File hashes
* URLs
* Domains
* IP addresses
* Malware detections
* Network relationships

Example workflow:

```text
Suspicious File
      ↓
Calculate SHA256
      ↓
Search in VirusTotal
      ↓
Check Detections
      ↓
Extract IOCs
```

## Shodan

Shodan is used to investigate publicly available information about Internet-facing infrastructure.

We can investigate:

* IP addresses
* Open ports
* Services
* Banners
* Hostnames
* Network infrastructure

## MISP

MISP is used to organize and correlate threat intelligence.

We can work with indicators such as:

* SHA256
* MD5
* SHA1
* IP addresses
* Domains
* URLs

## IOC Dataset

The collected dataset contains the following fields:

| Field           | Description              |
| --------------- | ------------------------ |
| IOC             | Indicator of Compromise  |
| Type            | Hash, IP, Domain, URL    |
| Source          | Intelligence source      |
| First Seen      | First observed date      |
| Last Seen       | Last observed date       |
| Threat Type     | Type of threat           |
| MITRE Technique | Related ATT&CK technique |
| Confidence      | Confidence level         |
| Description     | Additional information   |

### Week 2 Result

At the end of Week 2, we created an initial IOC dataset and documented the data collection process.

---

# Week 3 — Data Processing and Threat Hunting

Week 3 focuses on making the collected threat intelligence useful for threat hunting.

## Data Enrichment

Raw indicators are enriched with additional information from different sources.

Example:

```text
Suspicious IP
      ↓
VirusTotal
      ↓
Domain Relationships
      ↓
Malware Relationships
      ↓
MISP
      ↓
MITRE ATT&CK
      ↓
Threat Context
```

## IOC Normalization

Indicators from different sources may have different formats.

For example:

```text
HTTP://Example.COM
http://example.com/
example.com
```

can be normalized to:

```text
example.com
```

Hashes are also identified by their type:

* MD5
* SHA1
* SHA256

## IOC Filtering

We remove:

* Duplicate indicators
* Invalid values
* Irrelevant indicators
* Indicators with insufficient context
* Clearly benign indicators outside the project scope

## Correlation

Correlation connects indicators and information from different sources.

Example:

```text
Malicious Hash
      |
      +---- VirusTotal
      |
      +---- IP Address
      |
      +---- Domain
      |
      +---- MISP
      |
      +---- MITRE ATT&CK
```

This helps identify relationships between different indicators and potentially connect them to the same malicious activity.

---

# MITRE ATT&CK Mapping

Observed attacker behavior is mapped to the **MITRE ATT&CK** framework.

Examples:

| Observed Behavior            | MITRE ATT&CK |
| ---------------------------- | ------------ |
| User opens malicious file    | T1204        |
| PowerShell execution         | T1059.001    |
| Command execution            | T1059        |
| System information discovery | T1082        |
| Process discovery            | T1057        |

MITRE ATT&CK helps us describe attacker behavior using standardized tactics and techniques.

---

# MISP Implementation

MISP is used to organize collected intelligence into events and attributes.

Example event:

```text
Event: Windows Malware Investigation

Attributes:
1. SHA256
2. IP Address
3. Domain
4. URL
5. Malware Name
```

Example attributes:

```text
Type: sha256
Category: Payload delivery
Value: <SHA256>
```

```text
Type: ip-dst
Category: Network activity
Value: <IP>
```

```text
Type: domain
Category: Network activity
Value: <DOMAIN>
```

---

# Threat Hunting Workflow

The overall workflow for Weeks 1–3 is:

```text
             CTI
              ↓
       Identify Threat
              ↓
         OSINT Sources
              ↓
   ┌──────────┼──────────┐
   ↓          ↓          ↓
VirusTotal   Shodan     MISP
   └──────────┼──────────┘
              ↓
        Collect IOCs
              ↓
      Normalize Data
              ↓
         Filter IOCs
              ↓
        Correlate Data
              ↓
       MITRE ATT&CK
              ↓
       Threat Hunting
              ↓
      Detection Rules
```

---

# Repository Structure

```text
threat-hunting-project/
│
├── README.md
│
├── week-01/
│   ├── CTI_Glossary.md
│   ├── Threat_Classification.md
│   └── images/
│
├── week-02/
│   ├── OSINT_Data_Collection.md
│   ├── IOC_Dataset.csv
│   ├── Source_Mapping.md
│   └── images/
│
├── week-03/
│   ├── Data_Processing.md
│   ├── MISP_Analysis.md
│   ├── MITRE_Mapping.md
│   ├── iocs.csv
│   └── images/
│
├── scripts/
│   └── normalize_iocs.py
│
└── presentation/
    └── weekly-defense.pptx
```

---

# Project Result

After completing the first three weeks, the project provides a basic threat hunting workflow:

1. Understand Cyber Threat Intelligence.
2. Identify different types of cyber threats.
3. Collect IOCs using OSINT sources.
4. Normalize and filter collected data.
5. Enrich indicators with additional context.
6. Correlate indicators from different sources.
7. Map attacker behavior to MITRE ATT&CK.
8. Prepare intelligence for threat hunting and detection.

## Conclusion

The first three weeks established the foundation for the project. We created a CTI glossary, classified common threats, collected OSINT data, built an IOC dataset, processed indicators, and mapped relevant behavior to MITRE ATT&CK.

The next stage of the project will focus on using the collected intelligence for practical **threat hunting, detection, and analysis**.
