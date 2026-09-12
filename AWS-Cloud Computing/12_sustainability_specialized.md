<div align="center">

# <span style="color:#A855F7">🟪 Section 12 — Sustainability & Specialized Infrastructure</span>

![Section](https://img.shields.io/badge/Section-12-A855F7) ![Theme](https://img.shields.io/badge/Theme-Climate%2C_Satellites_%26_Hybrid_Hardware-A855F7)

</div>

---

## 🌱 Sustainability

AWS focuses on sustainability through several core goals aimed at reducing environmental impact.

| Goal | Detail |
|---|---|
| 🌍 **The Climate Pledge** | Amazon co-founded this to reach **net-zero carbon emissions** across all businesses, including AWS, by **2040** |
| ☀️ **Renewable Energy** | Working to power global infrastructure with **100% renewable energy by 2025** |
| ⚡ **Cloud Efficiency** | AWS infrastructure is **3.6x more energy efficient** than the median surveyed U.S. enterprise data center |
| 💧 **Water Stewardship** | Uses direct evaporative cooling technology and recycles non-potable water; aims for higher water-efficiency in every region |

> 💡 **Tip:** These efficiency gains are part of the same "heavy lifting" AWS absorbs on your behalf — one more reason migrating off self-managed data centers can reduce environmental impact at scale.

---

## 🛰️ AWS Ground Station

AWS Ground Station is a fully managed service for controlling satellite communications and processing data **without managing your own physical ground infrastructure** — think of it as a massive antenna dish pointing into the sky.

| Feature | Detail |
|---|---|
| **Use Cases** | Weather forecasting, surface imaging, communications, video broadcasts |
| **How It Works** | You schedule a "contact" with a specific satellite and ground location |
| **Data Handling** | A specialized EC2 image (AMI) uplinks/downlinks data, which can be stored directly in an **S3 bucket** |

---

## 📦 AWS Outposts

AWS Outposts delivers AWS infrastructure and services — essentially a **physical rack of servers** — directly to your on-premises data center or colocation space.

| Feature | Detail |
|---|---|
| **Data Residency** | Ideal for strict regulatory requirements — absolute certainty data stays on your premises |
| **Form Factors** | Full 42U rack (AWS-installed) or smaller 1U/2U units for existing racks |
| **Management** | AWS manages/monitors the hardware remotely, just like a standard region |

> ⚠️ **Gotcha:** Outposts hardware lives at *your* site, but it's still an AWS-managed service — you don't patch or maintain it yourself, which is different from a fully on-prem legacy setup.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---|---|
| The Climate Pledge | Amazon/AWS net-zero-by-2040 commitment |
| Renewable Energy Goal | 100% renewable power target by 2025 |
| Cloud Efficiency | AWS data centers are 3.6x more efficient than average enterprise DCs |
| Water Stewardship | Evaporative cooling + non-potable water recycling |
| AWS Ground Station | Managed satellite communication/data service |
| AWS Outposts | On-prem physical rack running AWS services, remotely managed |

---

## 🔜 Coming Next

> ⬜ *Not yet covered in this source material — flagged for future sections:*
> - **AWS Snow Family** (physically moving large data volumes to/from the cloud)
> - **AWS Well-Architected Framework**
> - **AWS Shared Responsibility Model**
> - **AWS Pricing Calculator & Migration Evaluator** (deep dive)

---

<div align="center">

⬅️ [Previous: Section 11 — Compliance, Data Residency & Government Cloud](./11_compliance_residency.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🏠 [Roadmap](./00_README.md)

### 🎉 You've completed the full AWS Cloud Practitioner Roadmap!

</div>
