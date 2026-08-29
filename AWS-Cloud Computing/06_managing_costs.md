<div align="center">

# <span style="color:#8E44AD">🟪 Section 6 — Managing Costs</span>

![Section](https://img.shields.io/badge/Section-6-8E44AD) ![Theme](https://img.shields.io/badge/Theme-Purple_%E2%80%94_Budgets_%26_Alerts-8E44AD)

</div>

---

## 💰 AWS Budgets

Set custom budgets to track costs/usage and get alerted when you exceed (or are forecasted to exceed) a threshold.

| Feature | Description |
|---|---|
| **Budget Types** | Costs, usage, or reservations (EC2, RDS, Redshift, ElastiCache) |
| **Time Periods** | Daily, monthly, quarterly, yearly |
| **Alerts** | Email or chatbot notification at a set % (e.g., 80%) |
| **Forecasting** | Predicts future spend based on current usage patterns |
| **Actions** | Can shift traffic or throttle resources if a limit is breached |

### 💵 Pricing

| Item | Cost |
|---|---|
| First 2 budgets | **Free** |
| Additional budgets | ~$0.02/day (~$0.60/month) |
| First 2 action-enabled budgets | **Free** |

---

## 🆓 AWS Free Tier

Explore and learn AWS at no cost, for a specified period or usage limit.

| Type | Description |
|---|---|
| **12-Month Free** | EC2 (750 hrs/month micro), RDS (750 hrs/month micro) |
| **Always Free** | Lambda (1M requests/month), SES (62,000 emails/month) |
| **Short-term Trials** | Limited-time trials for specific services |

### 🎁 Popular Free Tier Services

| Category | Allowance |
|---|---|
| Compute | 750 hrs/month of Linux/Windows T2/T3 micro instances |
| Storage | 5 GB standard S3 storage (12 months) |
| Networking | 50 GB CloudFront data transfer out |
| Monitoring | 10 free CloudWatch alarms + 1,000 email notifications/month |

> ⚠️ **Tip:** Enable Free Tier usage alerts in your billing preferences, and always read the fine print — some hardware/OS types are excluded.

---

## 🔔 Billing Alarm

A **CloudWatch** feature that monitors AWS spend and notifies you when costs exceed a threshold.

| Step | Detail |
|---|---|
| **Prerequisite** | Enable "Receive Billing Alerts" in Billing Preferences |
| **Metric** | CloudWatch's "Billing" metric → Total Estimated Charge (USD) |
| **Notification** | Sent via Amazon SNS when threshold (e.g., $50) is hit |
| **Free Tier** | 10 free billing alarms + 1,000 free email notifications/month |

---

## ⚖️ Budgets vs. Billing Alarms

| Feature | AWS Budgets | Billing Alarms |
|---|:---:|:---:|
| Forecasting | ✅ | ❌ |
| Flexible complex alerting | Moderate | ✅ More flexible |
| Free tier | 2 free | 10 free |

---

## 🧭 Summary Table

| Concept | Purpose |
|---|---|
| AWS Budgets | Set thresholds + forecast future spend |
| Free Tier | 12-month, always-free, and trial-based free usage |
| Billing Alarm | CloudWatch-based spend notification (simpler, no forecasting) |
| SNS | Delivers billing alarm notifications via email |

---

<div align="center">

⬅️ [Previous: Section 5 — Setting Up Your AWS Account](./05_setting_up_account.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🏠 [Roadmap](./00_README.md)

### 🎉 You've completed the full AWS Cloud Practitioner Roadmap!

</div>
