<div align="center">

# <span style="color:#E07B00">🟠 Section 4 — Solving for Coefficients (θ₁, θ₂, θ₀)</span>

![Section](https://img.shields.io/badge/Section-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_The_Solving_Order-E07B00)

</div>

---

## 🔄 The Critical Sequence

> [!WARNING]
> **Order matters:** Calculate **θ₁ and θ₂ first**, then solve for **θ₀ (intercept) last**.

```
Step 1: θ1  ←  from intermediate elements
Step 2: θ2  ←  from intermediate elements
Step 3: θ0  ←  from θ1, θ2, and the means of y, x1, x2
```

---

## 1️⃣ Solving for θ₁ and θ₂

These are calculated using the **intermediate elements** (adjusted summations) found in Section 3.

| Coefficient | Uses | Example Result |
|:---:|---|:---:|
| **θ₁** | Adjusted sums involving x₁ | ≈ **2.28** |
| **θ₂** | Adjusted sums involving x₂ and the interaction term | ≈ **-1.67** |

---

## 2️⃣ Solving for θ₀ (the Intercept)

Calculated **last** because its formula depends on θ₁ and θ₂ — plus the **means** of your original variables.

### 📊 Step A: Calculate the Means

```
mean(y)  = Σy / n
mean(x1) = Σx1 / n
mean(x2) = Σx2 / n
```

### 🔢 Step B: Apply the Formula

$$\theta_0 = \text{mean}(y) - (\theta_1 \cdot \text{mean}(x_1)) - (\theta_2 \cdot \text{mean}(x_2))$$

```
θ0 = mean(y) − (θ1 × mean(x1)) − (θ2 × mean(x2))
```

**Example result:** θ₀ ≈ **2.796**

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| θ₁, θ₂ first | Solved directly from intermediate (adjusted) sums |
| Means of y, x₁, x₂ | Required inputs for the intercept formula |
| θ₀ last | Depends on θ₁, θ₂, and the variable means |

---

### 🛠️ MLOps Perspective: Weights, Bias & Gradient Descent
> [!IMPORTANT]
> What you are solving here is identical to what a neural network's training loop computes:
> - **θ₁ and θ₂ are the "weights"** of each feature. A large positive θ means the feature strongly increases the prediction; a large negative θ means it strongly decreases it.
> - **θ₀ is the "bias"** — the baseline prediction before any feature is considered.
> - **Why `θ₀` is computed last:** This mirrors how biases are updated in backpropagation — weights are adjusted first based on the gradient, and then the bias is corrected to account for the mean offset.
> - In `sklearn`, after calling `.fit()`, you can inspect `model.coef_` (which gives `[θ₁, θ₂]`) and `model.intercept_` (which gives `θ₀`) — exactly what you computed here manually.

---

<div align="center">

⬅️ [Previous: Section 3 — Intermediate Elements](./03_intermediate_elements.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 5 — Final Equation Construction](./05_final_equation.md)

</div>
