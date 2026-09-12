<div align="center">

# <span style="color:#EAB308">🟨 Section 9 — AWS Global Infrastructure</span>

![Section](https://img.shields.io/badge/Section-9-EAB308) ![Theme](https://img.shields.io/badge/Theme-Regions_%26_Availability_Zones-EAB308)

</div>

---

## 🌐 The Three Core Components

AWS Global Infrastructure is the physical backbone of the platform — a globally distributed network of hardware and data centers.

| Component | Description |
|---|---|
| 🗺️ **Regions** | Geographically distinct locations (currently 39), e.g. **US-East-1** (Northern Virginia) |
| 🏢 **Availability Zones (AZs)** | Isolated data centers within a region, connected by low-latency networking; most regions have ≥3 |
| 📡 **Edge Locations** | Intermediate sites used by CloudFront/Global Accelerator to cache content near end users |

> 💡 **Tip:** For specialized needs, AWS also offers **Local Zones** (single-digit ms latency in populated areas) and **Wavelength Zones** (edge computing on 5G) — covered in Section 10.

---

## 🗺️ Regions in Depth

Regions are geographically distinct locations designed to be **completely independent and isolated** from one another — in location, power, and water supply — for maximum fault tolerance.

### Core Characteristics

| Feature | Detail |
|---|---|
| **AZ Count** | Every region generally has ≥3 Availability Zones |
| **Service Scoping** | Most services are "regional" — scoped to the region selected in the console |
| **Global Exceptions** | CloudFront, IAM, Route 53 are "global" services fixed to a global setting |
| **US-East-1** | The most important region — AWS's first; new features launch here first; **only** region showing all billing/cost info |

### 🧮 Four Factors for Selecting a Region

| # | Factor | Why It Matters |
|---|---|---|
| 1 | **Regulatory Compliance** | Data sovereignty may require data to stay within jurisdictional boundaries |
| 2 | **Cost** | Pricing varies significantly by region |
| 3 | **Service Availability** | Not every service is offered in every region |
| 4 | **Proximity/Latency** | Choosing a region near end users reduces data travel time |

> ⚠️ **Gotcha:** A region isn't just a "location setting" — it's a **fault level**. A disaster in one region (tornado, power grid failure) is designed **not** to cascade into others.

---

## 🏢 Regional vs. Global Services

| | **Regional Services** | **Global Services** |
|---|---|---|
| **Scope** | Hosted within the specific Region you select | Operate across the entire AWS network |
| **Console Behavior** | Selector shows only resources in the active region | Region selector locks to **"Global"** |
| **Examples** | EC2, RDS, Lambda, VPC | IAM, Route 53, CloudFront, WAF |
| **Creation** | Resource auto-bound to whatever region is active | N/A — not tied to one region |

### 🪣 The S3 Exception

S3 has a **global namespace** (bucket names must be unique across all of AWS) — but you must still **choose a specific region** to store your data when the bucket is created.

---

## 🏗️ Availability Zones (AZs)

AZs are isolated physical locations within a Region, each made up of one or more discrete data centers.

| Feature | Detail |
|---|---|
| **Redundancy** | Most regions have ≥3 AZs for high availability |
| **Isolation** | Each AZ has its own power, cooling, and physical security — an independent "failure zone" |
| **Connectivity** | Low-latency, high-bandwidth, encrypted networking; typically within 100 km (60 mi) of each other |
| **Deployment** | You choose a **subnet** when launching resources, which anchors the resource to a specific AZ |

---

## 🖱️ Follow Along: Selecting Regions & AZs

```text
1. Choose a Region
   - Top-right dropdown in the Management Console
   - Learning recommendation: US East 1 (Northern Virginia)
   - Production: choose the region closest to your end users

2. Select an Availability Zone
   - Interact with AZs via subnet selection during resource creation
   - "No preference" → AWS picks any available AZ
   - Specific subnet (e.g. US-East-1a) → pins resource to that AZ

3. Handle Global vs. Regional Services
   - Regional (EC2): bound to currently selected region
   - Global (CloudFront, IAM): selector locks to "Global"
   - S3 (hybrid): global namespace, but region chosen at bucket creation
```

> 💡 **Tip:** If you're just learning, stick to **US-East-1** — it's where new features ship first and the only region with unified billing visibility.

---

## 🛡️ Fault Tolerance

Fault tolerance is the ability to keep a service operational by **preventing** a single point of failure from causing an outage — different from disaster recovery, which focuses on *recovering after* a failure.

| Strategy | Description |
|---|---|
| **Failovers** | Automatically shift traffic to a redundant system if the primary fails |
| **RDS Multi-AZ** | A standby database in a different AZ takes over immediately if the primary fails |
| **Fault Domains & Levels** | AWS organizes infrastructure into fault levels (Regions) and fault domains (AZs) |

> 💡 **Tip:** Use **AWS Trusted Advisor** to actively monitor fault tolerance — e.g., flagging unassociated Elastic IPs or unbacked-up RDS databases.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---|---|
| Region | Isolated geographic location; a "fault level" |
| Availability Zone (AZ) | Isolated data center(s) within a region; a "fault domain" |
| Edge Location | Caches content near end users |
| US-East-1 | Original region; first for new features; only unified-billing view |
| Regional Service | Scoped to selected region (EC2, RDS, Lambda, VPC) |
| Global Service | Spans all regions (IAM, Route 53, CloudFront, WAF) |
| S3 | Global namespace, but region-bound storage |
| Fault Tolerance | Preventing outages via failovers, Multi-AZ, fault domains |
| AWS Trusted Advisor | Monitors account for fault-tolerance gaps |

---

<div align="center">

⬅️ [Previous: Section 8 — The Benefits of the Cloud](./08_cloud_benefits.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🏠 [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [➡️ Next: Section 10 — Networking & Edge Infrastructure](./10_networking_edge.md)

</div>
