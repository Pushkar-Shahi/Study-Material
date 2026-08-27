<div align="center">

# 📈 Simple Linear Regression Walkthrough
### *Predicting Business Expenditure with a Step-by-Step Numerical Example*

![Progress](https://img.shields.io/badge/Sections_Covered-5-blue) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Statistics_%26_Regression-4B0082?logo=python&logoColor=white)

</div>

---

## 📍 Progress Map

| # | Section | Focus | File | Status |
|---|-------|-------|------|:---:|
| 1️⃣ | 🟢 **The Foundation** | The equation `y = mx + c` explained | [`01_foundation.md`](./01_foundation.md) | ✅ |
| 2️⃣ | 🔵 **Data Preparation** | Building the x, y, x², xy table | [`02_data_preparation.md`](./02_data_preparation.md) | ✅ |
| 3️⃣ | 🟡 **Calculations & Formulas** | Solving for coefficient (a) and intercept (b) | [`03_calculations_formulas.md`](./03_calculations_formulas.md) | ✅ |
| 4️⃣ | 🟠 **Final Prediction** | Using the equation to predict Year 6 | [`04_final_prediction.md`](./04_final_prediction.md) | ✅ |
| 5️⃣ | 🔴 **Practice Problem** | Full worked solution for a new dataset | [`05_practice_problem.md`](./05_practice_problem.md) | ✅ |

---

## 📖 Quick-Reference Cheat Sheet

| Color | Section | Keywords |
|:---:|---|---|
| 🟢 | The Foundation | `y = mx + c`, dependent/independent variable, coefficient, intercept |
| 🔵 | Data Preparation | x, y, x², xy table, Σ (summation) |
| 🟡 | Calculations & Formulas | Coefficient formula (a), Intercept formula (b) |
| 🟠 | Final Prediction | Substituting x into `y = ax + b` |
| 🔴 | Practice Problem | Full independent worked example |

---

## 🔢 The Core Formulas at a Glance

```
Line equation:        y = ax + b

Coefficient (a):      a = [n(Σxy) − (Σx)(Σy)] / [n(Σx²) − (Σx)²]

Intercept (b):        b = (1/n) × [Σy − a(Σx)]
```

---

### 🛠️ MLOps Perspective: Why Simple Linear Regression?
> [!IMPORTANT]
> Simple Linear Regression (SLR) is the **foundation of every supervised ML algorithm**.
> - **Baseline Model:** In production ML systems, SLR is always implemented first as the baseline. If a more complex model (XGBoost, Neural Network) can't beat it, something is wrong.
> - **Feature Importance:** The coefficient `a` (slope) tells you directly how much `y` changes per unit change in `x`. This interpretability is critical in regulated industries (finance, healthcare) where MLOps engineers must explain model predictions to stakeholders.
> - **Model Monitoring:** Linear models are the simplest to monitor for data drift. If the learned slope shifts significantly over time, it's a clear signal that the underlying relationship has changed and retraining is needed.

---

<div align="center">

### 🎉 Walkthrough Complete!
*From the raw equation to a fully solved practice problem.*

</div>
