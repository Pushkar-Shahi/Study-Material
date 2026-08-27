<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — Data Preparation</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Building_the_Table-1E6FEB)

</div>

---

## 🔄 Horizontal → Vertical

The first step is transforming a horizontal data set into a **vertical table**, which makes the calculations much easier to manage.

---

## 🏗️ The Four Core Columns

| Column | Meaning |
|:---:|---|
| **x** | Independent variable — the years |
| **y** | Dependent variable — expenditure |
| **x²** | The square of each year |
| **xy** | The product of year × expenditure |

---

## 📊 Worked Example Table

| x (Year) | y (Expenditure) | x² | xy |
|:---:|:---:|:---:|:---:|
| 1 | 12 | 1 | 12 |
| 2 | 19 | 4 | 38 |
| 3 | 29 | 9 | 87 |
| 4 | 37 | 16 | 148 |
| 5 | 45 | 25 | 225 |

> [!NOTE]
> `xy` example: `2 × 19 = 38`

---

## ➕ Calculating the Summations (Σ)

Once the table is filled, sum each column:

| Sum | Value |
|:---:|:---:|
| **Σx** | 15 |
| **Σy** | 142 |
| **Σx²** | 55 |
| **Σxy** | 510 |

```
Σx  = 1 + 2 + 3 + 4 + 5         = 15
Σy  = 12 + 19 + 29 + 37 + 45    = 142
Σx² = 1 + 4 + 9 + 16 + 25       = 55
Σxy = 12 + 38 + 87 + 148 + 225  = 510
```

> [!TIP]
> These four sums are **exactly** what the regression formulas need in the next step.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Vertical table | Organizes raw data for easier calculation |
| x, y, x², xy columns | The four values needed per data point |
| Σ (summation) | Total of each column — feeds directly into the formulas |

---

### 🛠️ MLOps Perspective: This Table = A Feature Matrix
> [!IMPORTANT]
> The table you build in this step is conceptually identical to the **feature matrix** used in scikit-learn:
> - In `sklearn`, your `X` matrix holds the input features (the `x` column) and `y` is the target vector.
> - Computing `x²` is a form of **Feature Engineering** — creating a new feature from an existing one. In practice, this is done using `sklearn.preprocessing.PolynomialFeatures`.
> - The Σ sums are just `numpy` column-wise aggregations: `np.sum(X, axis=0)` and `np.dot(X.T, y)`.

---

<div align="center">

⬅️ [Previous: Section 1 — The Foundation](./01_foundation.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — Calculations & Formulas](./03_calculations_formulas.md)

</div>
