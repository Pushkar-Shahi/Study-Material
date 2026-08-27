<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — Calculating Summations</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Column_Totals-1E6FEB)

</div>

---

## ➕ The Task

Once your table is expanded, calculate the **summation (Σ)** for **every single column** by adding all the values within it.

---

## 🏗️ The Eight Required Sums

| Sum | Column It Totals |
|:---:|---|
| **Σy** | Dependent variable |
| **Σx₁** | First independent variable |
| **Σx₂** | Second independent variable |
| **Σx₁²** | Squared x₁ column |
| **Σx₂²** | Squared x₂ column |
| **Σx₁y** | x₁ × y column |
| **Σx₂y** | x₂ × y column |
| **Σx₁x₂** | x₁ × x₂ column |

```
Σy    = sum of the y column
Σx1   = sum of the x1 column
Σx2   = sum of the x2 column
Σx1²  = sum of the x1² column
Σx2²  = sum of the x2² column
Σx1y  = sum of the x1y column
Σx2y  = sum of the x2y column
Σx1x2 = sum of the x1x2 column
```

---

## 💡 Why This Matters

These eight totals are the **essential inputs** for the next step — finding the "intermediate elements" that eventually lead to your final coefficients (θ).

> [!WARNING]
> Miss even one sum, and you won't be able to complete the intermediate-element formulas in Section 3.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Σ (summation) | Total of every column in the expanded table |
| 8 required sums | Σy, Σx₁, Σx₂, Σx₁², Σx₂², Σx₁y, Σx₂y, Σx₁x₂ |
| Next step | These sums feed directly into the intermediate-element formulas |

---

### 🛠️ MLOps Perspective: Summations = Matrix Operations
> [!IMPORTANT]
> These 8 summations are just **matrix dot products** written out longhand:
> - `Σx₁y` = `np.dot(X[:, 0], y)` in NumPy
> - `Σx₁²` = `np.dot(X[:, 0], X[:, 0])` — the diagonal of the Gram matrix `XᵀX`
> - The full set of summations forms the **Normal Equations matrix**: `XᵀX` and `Xᵀy`, which is what `sklearn.LinearRegression` solves internally.
> - For large datasets, computing `XᵀX` is expensive ($\mathcal{O}(n \cdot p^2)$ where `p` is number of features). This is why distributed computing frameworks (Spark MLlib, Dask-ML) split these sums across multiple machines in parallel.

---

<div align="center">

⬅️ [Previous: Section 1 — Data Preparation](./01_data_preparation.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — Intermediate Elements](./03_intermediate_elements.md)

</div>
