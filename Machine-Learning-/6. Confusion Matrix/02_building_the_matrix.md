<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — Building the Matrix</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_TP_FP_FN_TN-1E6FEB)

</div>

---

## 🔲 What Is a Confusion Matrix?

A grid used to compare **what actually happened** with **what your model predicted**. For a simple binary case (like TB diagnosis), it creates **four categories**.

---

## 🏗️ The Four Quadrants

| Category | Meaning | TB Example |
|:---:|---|---|
| ✅ **True Positive (TP)** | Correctly predicted **positive** | Patient has TB → predicted "has TB" |
| ✅ **True Negative (TN)** | Correctly predicted **negative** | Patient is healthy → predicted "healthy" |
| ❌ **False Positive (FP)** | Incorrectly predicted **positive** ("false alarm") | Patient is healthy → predicted "has TB" |
| ❌ **False Negative (FN)** | Incorrectly predicted **negative** — the **dangerous** error | Patient has TB → predicted "healthy" |

---

## 🎯 The Simple Reading Rule

| Prediction vs. Reality | Label |
|---|:---:|
| Match | **"True"** |
| Mismatch | **"False"** |

`
Predicted = Actual   →  "True"  (TP or TN)
Predicted ≠ Actual   →  "False" (FP or FN)
`

---

## 📊 The Matrix Visualized

|  | Predicted: Positive | Predicted: Negative |
|---|:---:|:---:|
| **Actual: Positive** | ✅ TP | ❌ FN *(dangerous!)* |
| **Actual: Negative** | ❌ FP | ✅ TN |

> [!WARNING]
> In our TB example, **False Negative** is the most dangerous quadrant — it's a sick person told they're healthy.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Confusion Matrix | Compares predictions vs. actual outcomes |
| True Positive (TP) | Correctly caught a positive case |
| True Negative (TN) | Correctly caught a negative case |
| False Positive (FP) | False alarm — predicted positive incorrectly |
| False Negative (FN) | Missed a real positive — the most dangerous error |

---

### 🛠️ MLOps Perspective: Automating the Matrix in Python
> [!IMPORTANT]
> You never build these by hand in practice. Scikit-learn generates this array for you instantly:
> `python
> from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
> import matplotlib.pyplot as plt
>
> # Calculate the matrix
> cm = confusion_matrix(y_true, y_pred) 
> # Returns: [[TN, FP], [FN, TP]]
>
> # Plot it for stakeholders
> disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Healthy", "Sick"])
> disp.plot(cmap="Blues")
> plt.show()
> `
> In ML pipelines (like MLflow or Weights & Biases), this visual matrix is automatically saved as an artifact for every model run so reviewers can approve or reject the model deployment.

---

<div align="center">

⬅️ [Previous: Section 1 — The "Skewed Data" Problem](./01_skewed_data_problem.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — Evaluating Performance](./03_evaluating_performance.md)

</div>
