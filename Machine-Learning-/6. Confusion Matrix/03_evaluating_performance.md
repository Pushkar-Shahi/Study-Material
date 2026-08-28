<div align="center">

# <span style="color:#D4A017">🟡 Section 3 — Evaluating Performance</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Accuracy_Recall_Specificity-D4A017)

</div>

---

## 🎯 1. Accuracy

The most basic performance metric — the ratio of correct predictions to total predictions.

\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}

`
Accuracy = (TP + TN) / (TP + TN + FP + FN)
`

| When to Use | Limitation |
|---|---|
| ✅ Best for **balanced** datasets (roughly equal positive/negative cases) | ❌ Misleading on **imbalanced** datasets — a model can score 99% while missing every sick patient |

---

## 🔍 2. Recall (Sensitivity)

Focuses on the **Positive** class — how many actual positives did the model correctly catch?

\text{Recall} = \frac{TP}{TP + FN}

`
Recall = TP / (TP + FN)
`

| Why It Matters |
|---|
| In medical diagnosis, **high Recall** often matters more than high Accuracy — you want to catch **every** sick person (TP + FN), even if it means a few false alarms (FP) |

---

## 🛡️ 3. Specificity

The counterpart to Recall — focuses on the **Negative** class — how many actual negatives did the model correctly catch?

\text{Specificity} = \frac{TN}{TN + FP}

`
Specificity = TN / (TN + FP)
`

| Why It Matters |
|---|
| Tells you how good the model is at **avoiding false alarms** — high specificity means healthy people are rarely mislabeled as sick |

---

## 📊 All Three Metrics Side by Side

| Metric | Formula | Focuses On | Best Used When |
|---|---|---|---|
| **Accuracy** | (TP+TN)/(TP+TN+FP+FN) | Overall correctness | Balanced datasets |
| **Recall** | TP/(TP+FN) | Catching actual positives | Missing a positive is costly (e.g., disease) |
| **Specificity** | TN/(TN+FP) | Catching actual negatives | False alarms are costly |

> [!TIP]
> Looking at all three together gives a **much clearer picture** of model performance than a single accuracy percentage ever could.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Accuracy | Overall correct-prediction ratio — misleading on imbalanced data |
| Recall (Sensitivity) | Measures how well the model finds real positive cases |
| Specificity | Measures how well the model avoids false positives |
| Combined view | Three metrics together > one accuracy score alone |

---

### 🛠️ MLOps Perspective: The Precision-Recall Tradeoff
> [!IMPORTANT]
> The real-world complement to **Recall** is **Precision** (TP / (TP + FP)): "Out of everything the model labeled as Sick, how many actually were?"
> - **The Tradeoff:** You cannot maximize both. If you increase Recall (catch everyone who might be sick), you decrease Precision (you accidentally flag many healthy people).
> - **F1-Score:** Because of this tradeoff, MLOps systems usually optimize for the **F1-Score** — the harmonic mean of Precision and Recall (2 * (Precision * Recall) / (Precision + Recall)).
> - In sklearn, you use rom sklearn.metrics import classification_report to instantly generate a table containing Precision, Recall, F1-Score, and Accuracy for all your classes!

---

<div align="center">

⬅️ [Previous: Section 2 — Building the Matrix](./02_building_the_matrix.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full Confusion Matrix & Model Evaluation Walkthrough!

</div>
