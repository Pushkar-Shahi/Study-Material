<div align="center">

# <span style="color:#C0392B">🔴 Section 5 — Practice Problem</span>

![Section](https://img.shields.io/badge/Section-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Apply_What_You_Learned-C0392B)

</div>

---

## 📋 The Problem

**Goal:** Predict the business expenditure for **Year 4** based on the data below.

| Year (x) | Expenditure (y, in thousands) |
|:---:|:---:|
| 1 | 8 |
| 2 | 12 |
| 3 | 16 |

---

## ✅ Step 1 — Data Preparation

| x | y | x² | xy |
|:---:|:---:|:---:|:---:|
| 1 | 8 | 1 | 8 |
| 2 | 12 | 4 | 24 |
| 3 | 16 | 9 | 48 |

| Sum | Value |
|:---:|:---:|
| **Σx** | 6 |
| **Σy** | 36 |
| **Σx²** | 14 |
| **Σxy** | 80 |

---

## ✅ Step 2 — Calculate the Coefficient (a)

```
a = [n(Σxy) − (Σx)(Σy)] / [n(Σx²) − (Σx)²]      (n = 3)

a = [3(80) − (6)(36)] / [3(14) − (6)²]
a = [240 − 216] / [42 − 36]
a = 24 / 6
a = 4
```

---

## ✅ Step 3 — Calculate the Intercept (b)

```
b = (1/n)(Σy − a × Σx)

b = (1/3)(36 − 4 × 6)
b = (1/3)(36 − 24)
b = 12 / 3
b = 4
```

---

## ✅ Step 4 — Final Prediction for Year 4

**Regression equation:**
```
y = 4x + 4
```

**Substitute x = 4:**
```
y = 4(4) + 4
y = 16 + 4
y = 20
```

---

## 🏆 Answer

> [!TIP]
> **The predicted expenditure for Year 4 is 20 thousand.**

---

## 📝 Summary Table

| Step | Result |
|---|:---:|
| Coefficient (a) | 4 |
| Intercept (b) | 4 |
| Final equation | `y = 4x + 4` |
| Predicted expenditure (Year 4) | **20 thousand** |

---

### 🛠️ MLOps Perspective: Model Evaluation & Validation
> [!NOTE]
> Notice that in this practice problem, we predicted **Year 4** but we actually **know** what Year 4 would look like (the data is perfectly linear: 8, 12, 16, and therefore 20 is the obvious next value). This is intentional — it simulates **model evaluation**:
> - In real ML workflows, you split your data into a **Train set** and a **Test set**. You train on the first portion, predict on the test portion, and compare the predictions against the known ground truth.
> - **Evaluation Metrics for SLR:** `Mean Absolute Error (MAE)`, `Mean Squared Error (MSE)`, and `R² Score` tell you how far off your predictions are. In `sklearn`: `from sklearn.metrics import mean_absolute_error, r2_score`.
> - **Perfect R² = 1.0** means the model explains 100% of the variance in `y` — this dataset would achieve that since the relationship is perfectly linear.

---

<div align="center">

⬅️ [Previous: Section 4 — Final Prediction](./04_final_prediction.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full Simple Linear Regression Walkthrough!

</div>
