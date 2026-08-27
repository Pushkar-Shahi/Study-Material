<div align="center">

# <span style="color:#2E8B57">🟢 Section 1 — Data Preparation & Table Expansion</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Building_the_Table-2E8B57)

</div>

---

## 🎯 The Goal

The process begins with a table of values for a **dependent variable (y)** and **two independent variables (x₁ and x₂)**. To solve a multiple linear regression, you must **expand** this table with five additional columns.

---

## 🏗️ The Five New Columns

| Column | Meaning |
|:---:|---|
| **x₁²** | The square of the first independent variable |
| **x₂²** | The square of the second independent variable |
| **x₁y** | The product of x₁ and y |
| **x₂y** | The product of x₂ and y |
| **x₁x₂** | The product of the two independent variables |

```
For each row:
x1²  = x1 × x1
x2²  = x2 × x2
x1y  = x1 × y
x2y  = x2 × y
x1x2 = x1 × x2
```

---

## 📊 Expanded Table Template

| y | x₁ | x₂ | x₁² | x₂² | x₁y | x₂y | x₁x₂ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## 💡 Why This Matters

Expanding the table this way is essential because the values in these columns are used to find the **summations** required for the regression formulas.

> [!TIP]
> **Exam tip:** Rewrite the original table and append these five columns to keep your work organized and complete.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Original table (y, x₁, x₂) | Starting raw data |
| x₁², x₂² | Squared terms — needed for the coefficient formulas |
| x₁y, x₂y | Cross-products with y — capture the relationship between each x and y |
| x₁x₂ | Interaction term between the two independent variables |

---

### 🛠️ MLOps Perspective: Feature Engineering
> [!NOTE]
> What you're doing here is called **Feature Engineering** — one of the highest-impact skills in ML:
> - **x₁²** and **x₂²** are **polynomial features** — they allow the linear model to capture non-linear relationships. In scikit-learn: `PolynomialFeatures(degree=2)` does exactly this.
> - **x₁x₂** is an **interaction feature** — it encodes the combined effect of two variables. This is how pricing models capture "a discount works better for premium customers than budget customers."
> - In production pipelines, Feature Engineering is done in a `sklearn.Pipeline` so the same transformations are applied consistently during both training and inference.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 2 — Calculating Summations](./02_calculating_summations.md)

</div>
