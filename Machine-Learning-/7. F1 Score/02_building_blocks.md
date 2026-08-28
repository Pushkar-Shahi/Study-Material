<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — The Building Blocks</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_TP_TN_FP_FN-1E6FEB)

</div>

---

## 🔲 The Four Outcome Types

To move beyond simple accuracy, we use a **Confusion Matrix** to track four specific types of outcomes.

| Category | Meaning | Example |
|:---:|---|---|
| ✅ **True Positive (TP)** | Correctly predicted **positive** | Correctly identified a patient with TB |
| ✅ **True Negative (TN)** | Correctly predicted **negative** | Correctly identified a healthy person |
| ❌ **False Positive (FP)** | Predicted positive, actual was negative | "Incorrectly identified negative" — a false alarm |
| ❌ **False Negative (FN)** | Predicted negative, actual was positive | "Incorrectly identified positive" — the dangerous miss |

---

## 🎯 The Simple Reading Rule

`
Prediction matches reality  →  "True"  (TP or TN)
Prediction differs from reality → "False" (FP or FN)
`

---

## 🚨 The Most Dangerous Error

> [!WARNING]
> In critical scenarios like medical testing, a **False Negative** is the most dangerous error — a sick person is told they're healthy and might not seek life-saving treatment.

---

## 📊 The Matrix Visualized

|  | Predicted: Positive | Predicted: Negative |
|---|:---:|:---:|
| **Actual: Positive** | ✅ TP | ❌ FN *(dangerous!)* |
| **Actual: Negative** | ❌ FP | ✅ TN |

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| True Positive (TP) | Correctly caught a positive case |
| True Negative (TN) | Correctly caught a negative case |
| False Positive (FP) | False alarm — predicted positive incorrectly |
| False Negative (FN) | Missed a real positive — the most dangerous error |

---

<div align="center">

⬅️ [Previous: Section 1 — The Problem](./01_the_problem.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — The Metrics](./03_the_metrics.md)

</div>
