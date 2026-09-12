<div align="center">

# <span style="color:#EF4444">🟥 Section 11 — Compliance, Data Residency & Government Cloud</span>

![Section](https://img.shields.io/badge/Section-11-EF4444) ![Theme](https://img.shields.io/badge/Theme-GovCloud%2C_China_%26_Data_Sovereignty-EF4444)

</div>

---

## 📍 Data Residency & Sovereignty

**Data residency** refers to the physical/geographical location where an organization's data or cloud resources are stored — critical for orgs operating under **compliance boundaries** (legal/regulatory requirements dictating where data can live).

Closely related: **data sovereignty** — the legal/jurisdictional authority a country can assert over data physically located within its borders.

### 🧰 Tools & Strategies for Managing Data Residency

| Tool | What It Does |
|---|---|
| **AWS Outposts** | Physical rack of AWS servers delivered to your on-prem facility — absolute certainty of data location |
| **AWS Config** | "Policy as code" — rules that monitor configs and can alert/auto-delete resources violating residency rules |
| **IAM & Service Control Policies (SCPs)** | Explicit policies denying access to specific regions; SCPs enforce this **mandatorily** across an entire organization |
| **Regional Selection** | Specific regions (e.g., GovCloud) keep sensitive data on approved soil, managed only by vetted personnel |
| **EU Data Sovereignty Features** | Specialized features to meet strict European privacy/control requirements |

> ⚠️ **Gotcha:** IAM policies can be bypassed at the individual-account level, but **SCPs applied at the organization level** are mandatory across *all* accounts — that's the real safeguard against accidentally moving data into unapproved jurisdictions.

---

## 🏛️ AWS for Government

AWS supports the **public sector** (military, law enforcement, healthcare) by meeting strict compliance programs:

```
HIPAA · FedRAMP · CJIS · FIPS
```

The primary offering is **AWS GovCloud** — specialized, isolated regions for sensitive, controlled unclassified information.

---

## 🔐 GovCloud in Depth

| Feature | Detail |
|---|---|
| **Restricted Access** | Operated only by **US citizens on US soil**; accessible only to US entities that pass screening |
| **High Compliance** | Meets FedRAMP (High & Moderate), ITAR, HIPAA, DOJ's CJIS policy |
| **Isolated Partition** | Physically & logically separate from standard regions — some features (e.g., Reserved Instance Marketplace) aren't available |
| **Data Residency Backup** | For absolute physical certainty, government entities can pair this with **AWS Outposts** |

> 💡 **Tip:** Use **AWS Artifact** to download the compliance reports that prove GovCloud (and other regions) meet these standards.

---

## 🇨🇳 AWS in China

AWS China is a **separate, intentionally isolated** cloud offering built to meet mainland China's regulatory requirements.

| Feature | Detail |
|---|---|
| **Domain** | `amazon.cn` — "AWS" branding largely absent due to trademark restrictions |
| **Local Partners** | **Sinnet** operates Beijing; **NWCD** operates Northwest (Ningxia) |
| **Licensing** | Requires a Chinese business license (ICP license) + registration process |
| **Connectivity** | Traffic doesn't cross the "Great Firewall" → better performance for local users |
| **Service Limitations** | Not all AWS Global services available — e.g., **Route 53 is not offered** |

### 🖱️ Follow Along: Exploring AWS China

```text
1. Access the Chinese Portal
   → amazon.aws.cn (branding differs from aws.amazon.com)

2. Review Onboarding Requirements
   → Chinese Business License (ICP)
   → Mandatory screening / business registration certificate

3. Identify Regional Isolation
   → Separate domain, no cross-interaction with AWS Global
   → Beijing = Sinnet · Ningxia = NWCD

4. Check Service Availability
   → e.g. Route 53 NOT available in China regions
```

> ⚠️ **Gotcha:** Workloads created in AWS Global **cannot interact** with AWS China — treat it as a fully separate cloud, not just another region.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---|---|
| Data Residency | Physical location where data is stored |
| Data Sovereignty | Legal jurisdiction over data based on location |
| AWS Outposts | On-prem AWS hardware for guaranteed residency |
| AWS Config | Policy-as-code monitoring for compliance violations |
| SCPs | Org-wide mandatory region-restriction policies |
| GovCloud | Isolated US regions for sensitive government workloads |
| FedRAMP / ITAR / HIPAA / CJIS | Government compliance standards met by GovCloud |
| AWS China | Fully isolated cloud for the Chinese market (Sinnet/NWCD) |
| AWS Artifact | Source for downloading compliance reports |

---

<div align="center">

⬅️ [Previous: Section 10 — Networking & Edge Infrastructure](./10_networking_edge.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🏠 [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [➡️ Next: Section 12 — Sustainability & Specialized Infrastructure](./12_sustainability_specialized.md)

</div>
