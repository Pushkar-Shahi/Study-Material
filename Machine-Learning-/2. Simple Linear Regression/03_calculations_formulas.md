<div align="center">

# <span style="color:#D4A017">🟡 Section 3 — Calculations & Formulas</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Solving_for_a_and_b-D4A017)

</div>

---

## 🔢 1. Calculating the Coefficient (a)

$$a = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}$$

### 📊 Plugging In Our Values (n = 5)

```
a = [5(510) − (15)(142)] / [5(55) − (15)²]
```

| Step | Calculation | Result |
|---|---|---|
| Numerator | `5(510) − (15)(142)` | `2550 − 2130 = 420` |
| Denominator | `5(55) − (15)²` | `275 − 225 = 50` |
| **a** | `420 / 50` | **8.4** |

---

## 🔢 2. Calculating the Intercept (b)

$$b = \frac{1}{n}(\sum y - a\sum x)$$

### 📊 Plugging In Our Values

```
b = (1/5) × (142 − 8.4 × 15)
```

| Step | Calculation | Result |
|---|---|---|
| Inside brackets | `142 − 8.4 × 15` | `142 − 126 = 16` |
| **b** | `16 / 5` | **3.2** |

---

## ✅ The Final Equation

Plugging `a` and `b` back into `y = ax + b`:

```
y = 8.4x + 3.2
```

> [!TIP]
> This equation is now a fully working prediction tool — plug in any year to estimate expenditure.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Coefficient formula (a) | Determines the slope / rate of change |
| Intercept formula (b) | Determines the starting value at x = 0 |
| Final equation `y = ax + b` | The complete regression line, ready for prediction |

---

### 🛠️ MLOps Perspective: Closed-Form vs Gradient Descent
> [!IMPORTANT]
> The formula you just used to compute `a` and `b` is called the **Closed-Form (Normal Equation)** solution.
> - For small datasets, this formula computes the optimal weights in a single step with no iteration required.
> - **The Problem at Scale:** When your dataset has millions of rows, computing `(XᵀX)⁻¹` (the matrix equivalent) becomes too memory-intensive. This is why large-scale ML systems use **Gradient Descent** instead — an iterative algorithm that finds `a` and `b` step by step.
> - `sklearn.linear_model.LinearRegression` uses the closed-form (or SVD decomposition) internally. `sklearn.linear_model.SGDRegressor` uses Stochastic Gradient Descent — the scalable version used in deep learning.

---

<div align="center">

⬅️ [Previous: Section 2 — Data Preparation](./02_data_preparation.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 4 — Final Prediction](./04_final_prediction.md)

</div>
