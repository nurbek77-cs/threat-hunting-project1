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

---# Week 2 — OSINT and IOC Data Collection

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
