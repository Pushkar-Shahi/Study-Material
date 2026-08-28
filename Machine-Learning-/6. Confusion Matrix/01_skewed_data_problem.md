<div align="center">

# <span style="color:#2E8B57">🟢 Section 1 — The "Skewed Data" Problem</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Why_Accuracy_Lies-2E8B57)

</div>

---

## ⚖️ What Is Skewed Data?

Also called an **imbalanced dataset** — a situation where the data is heavily tilted toward one outcome.

---

## 🏥 The Healthcare Example

| Detail | Value |
|---|---|
| Total patients | 100 |
| Healthy (99%) | 99 people |
| Has tuberculosis (1%) | 1 person |

---

## 🪤 The "Error Rate" Trap

If a poorly designed model **simply predicts "healthy" for everyone**:

| Metric | Result |
|---|:---:|
| Accuracy | **99%** |
| Error Rate | **1%** |

> [!WARNING]
> That sounds great on paper — but it's a trap.

---

## 🚨 The Real-World Danger

That "1% error" means the **one person who is actually sick** is told they're healthy.

```
Sick patient → Told "Healthy" → Doesn't seek treatment → Could die
```

Because they trust the report, they don't seek treatment — a devastating consequence hidden behind a seemingly great accuracy score.

---

## 🎯 Why This Matters

> [!IMPORTANT]
> **Accuracy is not a useful metric on its own for imbalanced datasets** — it hides the fact that the model completely fails to catch the most critical cases.

This is exactly why we need the **Confusion Matrix**: it lets us look past the overall error rate and see **exactly where** the model is making mistakes.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Skewed/imbalanced data | Dataset heavily weighted toward one outcome |
| Error rate trap | A low error rate can still mean total failure on critical cases |
| Why accuracy fails | High accuracy can be achieved by ignoring the minority class entirely |
| Confusion Matrix | The tool that reveals what accuracy hides |

---

### 🛠️ MLOps Perspective: Handling Imbalanced Data
> [!NOTE]
> MLOps engineers have several tools to fix models that fall into the "Accuracy Trap" during training:
> - **Class Weights:** In `sklearn`, setting `class_weight="balanced"` forces the algorithm to penalize errors on the minority class (sick patients) much more heavily than errors on the majority class.
> - **SMOTE (Synthetic Minority Over-sampling Technique):** Synthetically generates new training examples for the minority class to balance the dataset before training.
> - **Threshold Tuning:** Instead of assuming a >50% probability means "Sick", we can lower the threshold to >5% to aggressively flag anyone who might have the disease.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 2 — Building the Matrix](./02_building_the_matrix.md)

</div>
