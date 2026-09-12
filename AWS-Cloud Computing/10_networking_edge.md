<div align="center">

# <span style="color:#F97316">🟧 Section 10 — Networking & Edge Infrastructure</span>

![Section](https://img.shields.io/badge/Section-10-F97316) ![Theme](https://img.shields.io/badge/Theme-PoPs%2C_Direct_Connect_%26_Edge_Zones-F97316)

</div>

---

## 🛣️ The AWS Global Network

The AWS Global Network is the physical backbone of AWS — a private "expressway" that lets data move rapidly between regions and data centers.

| Feature | Description |
|---|---|
| **Edge Locations as Ramps** | On/off-ramps to the network, used by Global Accelerator and S3 Transfer Acceleration |
| **Reduced Latency** | Traversing this private network (vs. the public internet) is faster and more reliable |
| **VPC Endpoints** | Let resources communicate entirely within AWS, never touching the public internet |
| **Redundant Connectivity** | AZs are redundantly connected to multiple tier-one transit providers |

---

## 📍 Points of Presence (PoP)

PoPs are intermediate data center locations situated **between** an AWS Region and the end user.

| Type | Purpose |
|---|---|
| **Edge Locations** | Cache popular files (web pages, images, videos) to cut delivery distance/latency |
| **Regional Edge Caches** | Larger caches for *less* popular files — reduces round trips to origin and data-transfer fees |

### Services That Use PoPs

| Service | Function |
|---|---|
| **Amazon CloudFront** | CDN routing requests to the nearest edge cache |
| **Amazon S3 Transfer Acceleration** | Uploads go to a nearby edge location, then travel fast over the private AWS network to S3 |
| **AWS Global Accelerator** | Uses edge locations to find the optimal path from users to your servers |

> 💡 **Tip:** Think of PoPs as **"on and off-ramps"** to the AWS Global Network's expressway.

---

## 🔌 AWS Direct Connect

Direct Connect links your internal network directly to an AWS Direct Connect location over a standard fiber-optic Ethernet cable — creating a "hybrid" network.

| Feature | Detail |
|---|---|
| **Dedicated Connection** | Private, physical "expressway" — bypasses the public internet (unlike a VPN) |
| **High Performance** | Ultra-low, consistent latency; cloud feels like part of your local network |
| **Bandwidth Options** | Lower: 50 Mbps–500 Mbps · Higher: 1 Gbps–10 Gbps |
| **Reduced Costs** | Especially beneficial when moving large volumes of data |

> ⚠️ **Gotcha:** Direct Connect is **private but not secure (encrypted)**. If you need encryption in transit, layer an **AWS Site-to-Site VPN** on top of it.

### Direct Connect Locations

| Feature | Detail |
|---|---|
| **Trusted Partner Sites** | Colocations / "carrier hotels" |
| **Physical Link** | Fiber-optic Ethernet cable connects your network to AWS |
| **Bypasses Internet** | Data avoids the public internet entirely |
| **Example** | Allied data center in Toronto |

---

## 🏙️ AWS Local Zones

Local Zones place compute, storage, and select services close to large population/industry/IT centers.

| Feature | Detail |
|---|---|
| **Low Latency** | As low as **7 ms** for latency-sensitive apps |
| **Regional Extension** | Tied to a specific Region — e.g., LA Local Zone extends US West (Oregon) |
| **Selective Services** | Limited subset: specific EC2 types, EBS, VPC, Application Load Balancers |
| **Opt-in Required** | Must opt in via Console or support ticket |

### Primary Use Cases

```
🎬 Media & Entertainment  — real-time video editing/rendering
🛠️ Electronic Design Automation — high-performance engineering
📢 Ad Tech — rapid ad bidding and delivery
🤖 Machine Learning — low-latency inference
```

---

## 📶 Wavelength Zones

Wavelength Zones are built for **edge computing on 5G networks**, placing AWS hardware directly inside telecom providers' data centers.

| Feature | Detail |
|---|---|
| **Target Audience** | Mobile apps needing single-digit ms latency on 5G |
| **Telecom Partners** | Verizon, Vodafone, KDDI |
| **Deployment** | Opt in via Console → create subnet tied to the Wavelength Zone → launch EC2 directly on the 5G network |
| **Network Path** | Mobile traffic routes to nearby hardware instead of a distant Region over the public internet |

> 💡 **Tip:** **Local Zones** = latency for *general* populated-area workloads. **Wavelength Zones** = latency specifically for *mobile/5G* workloads. Don't mix them up.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---|---|
| AWS Global Network | Private backbone connecting AWS infrastructure worldwide |
| Edge Location | Caches content near users |
| Regional Edge Cache | Larger cache for less-popular content |
| Point of Presence (PoP) | On/off-ramp to the AWS network |
| Direct Connect | Dedicated, private (not encrypted) fiber link to AWS |
| Direct Connect Location | Partner colocation site for establishing the link |
| Local Zones | Low-latency extension of a region near population centers |
| Wavelength Zones | Edge computing embedded in telecom 5G networks |

---

<div align="center">

⬅️ [Previous: Section 9 — AWS Global Infrastructure](./09_global_infrastructure.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🏠 [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [➡️ Next: Section 11 — Compliance, Data Residency & Government Cloud](./11_compliance_residency.md)

</div>
