<div align="center">

# <span style="color:#2E8B57">🟢 Section 1 — The Foundation</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_The_Line_Equation-2E8B57)

</div>

---

## 📐 The Equation of a Straight Line

Simple Linear Regression starts with the classic equation:

```
y = mx + c
```

---

## 🔤 Breaking Down Each Term

| Symbol | Name | Meaning (in this business example) |
|:---:|---|---|
| **y** | Dependent Variable | The value we want to **predict** — expenditure |
| **x** | Independent Variable | The value we use **to** predict — the year |
| **m** | Coefficient | The **rate of change** for expenditure |
| **c** | Intercept | The value of **y when x = 0** |

---

## 🎯 The Goal

Find the specific values of **m** (coefficient) and **c** (intercept) so that plugging in any year lets us calculate a predicted expenditure.

```
Known year (x) → Regression equation → Predicted expenditure (y)
```

> [!TIP]
> Once we solve for `m` and `c`, the equation becomes a reusable **prediction machine** for any future year.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `y = mx + c` | The base linear equation regression is built on |
| Dependent variable (y) | What you're trying to predict |
| Independent variable (x) | What you use to make the prediction |
| Coefficient (m) | Rate of change / slope |
| Intercept (c) | Starting value when x = 0 |

---

### 🛠️ MLOps Perspective: `y = mx + c` in Production
> [!NOTE]
> Understanding `y = mx + c` at its most basic level directly maps to how ML model inference works:
> - **`x` = Features:** Every feature in your model (CPU usage, request count, etc.) is an `x` variable fed into the model.
> - **`m` = Weights:** The `m` coefficient is the "weight" that the model learns during training — how much influence each feature has on the output.
> - **`c` = Bias:** The intercept `c` is the bias term added at the end of every neural network layer.
> - **`y` = Prediction:** The output your model serves via a REST API endpoint in production.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 2 — Data Preparation](./02_data_preparation.md)

</div>
