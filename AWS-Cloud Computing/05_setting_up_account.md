<div align="center">

# <span style="color:#C0392B">🟥 Section 5 — Setting Up Your AWS Account</span>

![Section](https://img.shields.io/badge/Section-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Getting_Started_Securely-C0392B)

</div>

---

## 📝 Creating Your Account

| Step | Requirement |
|---|---|
| Visit | aws.amazon.com → "Create an AWS Account" |
| Email | A unique email — ideally accessible by your whole team |
| Payment | A valid credit card |

> 💡 If your card fails verification, you may need to contact AWS support.

---

## 👑 The Root User

Once active, you operate as the **Root User** — a special identity with **full, unlimited access** to every resource and service.

> ⚠️ The root user should **not** be used for daily tasks.

---

## ✅ Critical First Steps After Creation

### 1️⃣ Enable Multi-Factor Authentication (MFA)

Protect your root account from unauthorized access.

| Option | Description |
|---|---|
| Virtual MFA App | Google Authenticator, Microsoft Authenticator |
| Physical Security Key | YubiKey |

### 2️⃣ Create an IAM User for Daily Use

- Go to the **IAM console**
- Create a new user, assign to an **"Admin"** or **"Power User"** group
- Use this IAM user for regular work
- Reserve the root account for specialized tasks (e.g., closing the account, changing support plan)

```
❌ Don't use Root for daily work
✅ Create an IAM user → assign Admin/Power User group → use that instead
```

### 3️⃣ Leverage the Free Tier

New accounts get access to certain services **free for 12 months**, including:
- **750 hours/month** of EC2 (virtual machines)
- **750 hours/month** of RDS (databases) — micro instance types

---

## 🌍 Setting Your Default Region

| Tip | Detail |
|---|---|
| Check region | Top-right corner of the Management Console |
| Recommended region for learning | **US-East-1** (Northern Virginia) — original region, most new features launch here first |

---

## 🧭 Summary Table

| Concept | Purpose |
|---|---|
| Root User | Full-access identity created at account signup — avoid daily use |
| MFA | First security step — protects the root account |
| IAM User | Your everyday login, scoped to Admin/Power User permissions |
| Free Tier | 12 months of limited free usage on EC2, RDS, and more |
| US-East-1 | Recommended default region for learning AWS |

---

<div align="center">

⬅️ [Previous: Section 4 — Types of Cloud Computing](./04_types_of_cloud_computing.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🏠 [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 6 — Managing Costs](./06_managing_costs.md)

</div>
