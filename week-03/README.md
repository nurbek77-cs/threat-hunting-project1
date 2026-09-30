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
