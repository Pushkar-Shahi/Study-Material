<div align="center">

# <span style="color:#2E8B57">🟢 Step 1 — How the Web Works</span>

![Step](https://img.shields.io/badge/Step-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Infrastructure-2E8B57)

</div>

---

## 🌍 The Physical Backbone

The internet runs on a vast physical infrastructure of towers and cables owned by **Internet Service Providers (ISPs)** like Jio or Airtel. These companies provide data (measured in MB/GB) that travels back and forth to your device.

---

## 📡 1. Types of Networks

| Network | Scale | Example |
|---|---|---|
| 📱 **PAN** (Personal) | Very small range | Phone → Bluetooth earbuds |
| 🏠 **LAN** (Local) | Single building/room | Home WiFi |
| 🏙️ **MAN** (Metropolitan) | A whole city/campus | Multiple LANs linked together |
| 🌐 **WAN** (Wide) | Countries / the entire planet | The internet itself |

> [!TIP]
> The internet **is** a WAN — the largest possible scale of network.

---

## 🤝 2. The Client-Server Model

Web communication follows a simple **"ask and receive"** pattern.

| Role | Description |
|---|---|
| 💻 **Client** | Your browser or app — the one **asking** for information |
| 🗄️ **Server** | A powerful, always-on computer that **stores and sends** the website |
| 📤 **Request** | What you send — *"Give me the YouTube homepage"* |
| 📥 **Response** | The data the server sends back |

---

## 📇 3. IP Addresses & DNS

Every device has a unique "home address" — an **IP Address**.

| Format | Description |
|---|---|
| **IPv4** | 4 numbers (e.g., `142.250.183.78`) — ~4.3 billion possible addresses |
| **IPv6** | Newer, much longer format — solves the address shortage |

### 📖 DNS (Domain Name System)
Since humans can't remember long numbers, **DNS** acts like a giant phonebook — translating a human-readable name (`google.com`) into the server's actual IP address.

```
google.com  →  DNS lookup  →  142.250.183.78
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| ISP | Provides your physical connection to the internet |
| PAN/LAN/MAN/WAN | Describe network scale, smallest to largest |
| Client-Server Model | How browsers and websites communicate |
| Request / Response | The two halves of every web interaction |
| IP Address | A device's unique numeric identifier |
| DNS | Translates domain names into IP addresses |

---

### 🛠️ MLOps Perspective: Networking Basics
> [!NOTE]
> Understanding the web is non-negotiable for MLOps:
> - **Client-Server Model:** When you deploy an ML model using FastAPI or TensorFlow Serving, you are building a **Server**. When a user's mobile app sends a photo for classification, it is the **Client** making a **Request**.
> - **IP & DNS:** In AWS or GCP, your ML model containers will be assigned IP addresses. You will configure DNS records (Route 53, Cloud DNS) so developers can access your model via `api.yourcompany.com/predict` instead of raw IPs.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 2 — HTML Basics](./02_html_basics.md)

</div>
