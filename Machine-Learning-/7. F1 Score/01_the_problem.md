<div align="center">

# <span style="color:#2E8B57">🟢 Section 1 — The Problem</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_When_Accuracy_Lies-2E8B57)

</div>

---

## ⚖️ The Skewed Data Trap

When dealing with **skewed (imbalanced) data**, a basic Accuracy score can completely hide the fact that a model is failing.

| Metric | Value |
|---|---|
| Total patients | 100 |
| Have Tuberculosis (TB) | 1 |
| Healthy | 99 |

> [!WARNING]
> If a model predicts **"nobody has TB"** for every patient, it still scores **99% accuracy**.

`
Model prediction: "Everyone is healthy"
Accuracy:          99%
Reality:           1 person is actually sick and gets missed entirely
`

---

## 🚨 High Risk of Errors

| Fact | Consequence |
|---|---|
| A 1% error rate sounds low | But in medical/high-stakes contexts, that 1% can be **catastrophic** |
| Sick person told "healthy" | Won't seek treatment → could be **fatal** |

---

## 🎯 Why Simple Metrics Fail

Standard metrics like accuracy **don't highlight** these critical misses in imbalanced data. This is why we need a **Confusion Matrix** to properly evaluate model performance.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Skewed/imbalanced data | Dataset heavily weighted toward one class |
| Misleading accuracy | High accuracy can hide total failure on the minority (critical) class |
| High-stakes risk | Missing rare-but-critical cases can have severe real-world consequences |
| Confusion Matrix | The tool needed to see past the misleading accuracy number |

---

### 🛠️ MLOps Perspective: Defining "Positive"
> [!NOTE]
> In Machine Learning, the "Positive" class doesn't mean "Good" — it means **the event you are trying to detect**. 
> - In this case, "Positive" = Has Tuberculosis. 
> - Because this is the rare, critical event, MLOps practitioners focus almost entirely on how the model performs on the Positive class, often completely ignoring the True Negatives (healthy people correctly predicted as healthy) when evaluating the model's worth.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 2 — The Building Blocks](./02_building_blocks.md)

</div>
