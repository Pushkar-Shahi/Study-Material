<div align="center">

# <span style="color:#E07B00">🟠 Section 4 — Final Prediction</span>

![Section](https://img.shields.io/badge/Section-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Using_the_Equation-E07B00)

</div>

---

## 🎯 The Goal: Predict Year 6

We now use our finished regression equation to forecast expenditure for a year **outside** our original dataset.

```
y = 8.4x + 3.2
```

---

## 📊 Substituting x = 6

| Step | Calculation |
|---|---|
| Substitute | `y = 8.4(6) + 3.2` |
| Multiply | `y = 50.4 + 3.2` |
| Add | `y = 53.6` |

```
y = 8.4(6) + 3.2
y = 50.4 + 3.2
y = 53.6
```

---

## 🏆 The Result

> [!TIP]
> **Predicted expenditure for Year 6 = 53.6 thousand**

Since the original data was measured in **thousands**, the final answer is also in thousands.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Substitution | Plug the target x-value into the regression equation |
| `y = 8.4x + 3.2` | Our specific solved equation from this dataset |
| Year 6 prediction | 53.6 thousand — the final forecasted value |

---

### 🛠️ MLOps Perspective: Inference & Model Serving
> [!IMPORTANT]
> What you just did — substituting `x = 6` to get `y = 53.6` — is **model inference**.
> - **In Production:** When a user sends a request to your ML model's REST API (e.g., `POST /predict {"year": 6}`), your server does exactly this: loads the pre-trained weights `a = 8.4` and `b = 3.2`, substitutes the input, and returns `{"prediction": 53.6}` as the response JSON.
> - **Extrapolation Risk:** Predicting Year 6 when you trained on Years 1–5 is called **extrapolation**. In production ML, this is a data distribution shift — your model is receiving inputs outside its training range. This is monitored using tools like **Evidently AI** or **Arize** to alert when inputs deviate from the training distribution.

---

<div align="center">

⬅️ [Previous: Section 3 — Calculations & Formulas](./03_calculations_formulas.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 5 — Practice Problem](./05_practice_problem.md)

</div>
