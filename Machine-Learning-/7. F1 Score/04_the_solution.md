<div align="center">

# <span style="color:#E07B00">🟠 Section 4 — The Solution (F1 Score)</span>

![Section](https://img.shields.io/badge/Section-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Balancing_the_Trade-Off-E07B00)

</div>

---

## 🎯 The Problem It Solves

The **precision-recall trade-off**: improving one usually causes the other to drop. Evaluating a model with only **one** of these metrics can be misleading.

> [!TIP]
> The **F1 Score** combines both into a **single number** for a more balanced view of performance.

---

## 🧮 The Formula

F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}

`
F1 Score = 2 × (Precision × Recall) / (Precision + Recall)
`

> [!NOTE]
> This is the **harmonic mean** of Precision and Recall — it penalizes extreme imbalances between the two more than a simple average would.

---

## 🏆 The Goal

| F1 Score | Meaning |
|:---:|---|
| Close to **1** | Both Precision and Recall are high — model performs well on both fronts |
| Close to **0** | At least one of Precision or Recall is very poor |

---

## ✅ Best Use Case

> [!IMPORTANT]
> The F1 Score is the **preferred metric** when dealing with **imbalanced or skewed data**, where simple accuracy is not enough.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| F1 Score | Single balanced metric combining Precision and Recall |
| Formula | Harmonic mean of Precision and Recall |
| High F1 (~1) | Indicates strong performance on both metrics simultaneously |
| Best use case | Imbalanced/skewed datasets where accuracy alone is misleading |

---

### 🛠️ MLOps Perspective: Automating F1 in Pipelines
> [!NOTE]
> When building CI/CD pipelines for Machine Learning (like GitHub Actions for models), you don't manually check these numbers. You write a test:
> `python
> from sklearn.metrics import f1_score
> 
> def test_model_performance():
>     f1 = f1_score(y_true, y_pred)
>     assert f1 > 0.85, f"Model degraded! F1 Score {f1} is below threshold."
> `
> If a data scientist submits a new model that improves Accuracy but sacrifices too much Precision (causing the F1 score to drop below 0.85), the pipeline automatically blocks the model from being deployed to production!

---

<div align="center">

⬅️ [Previous: Section 3 — The Metrics](./03_the_metrics.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full Precision, Recall & F1 Score Walkthrough!

</div>
