<div align="center">

# <span style="color:#D4A017">🟡 Section 3 — The Purpose</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Why_It_Matters-D4A017)

</div>

---

## 🎯 The Core Purpose

The primary purpose of a Decision Tree is to enable a computer to **predict outcomes** and **classify information**.

---

## ⚙️ How It Works in Practice

| Capability | Description |
|---|---|
| 🔮 **Prediction (Regression)** | Taking complex data and reaching a likely future outcome (e.g., predicting a continuous number like stock price or age) |
| 🗂️ **Classification** | Sorting data into distinct categories based on structured logic (e.g., Spam vs. Not Spam) |

> By using this model, a machine can take complex data and reach a final decision through a **structured, repeatable process**.

---

## 🏦 Real-World Application: The Bank Example

| Category | Outcome |
|---|---|
| ✅ Applicant meets criteria | **"Loan Accepted"** |
| ❌ Applicant doesn't meet criteria | **"Loan Rejected"** |

> [!TIP]
> Another common real-world use: **predicting customer preferences** (e.g., Will they buy this product?) based on background demographic data.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Prediction | Estimating a likely future numerical outcome from data |
| Classification | Sorting data into defined discrete categories |
| Bank loan example | Classifies applicants into "Accepted" or "Rejected" |

---

### 🛠️ MLOps Perspective: Classification vs Regression Trees
> [!IMPORTANT]
> Decision Trees can actually handle both Classification (categorical outputs) AND Regression (continuous numerical outputs):
> - **CART Algorithm:** Modern Decision Trees use the CART algorithm (Classification and Regression Trees).
> - **Classification Leaf:** The leaf node returns the majority class (e.g., 8 out of 10 people in this leaf defaulted on loans, so prediction = "Default").
> - **Regression Leaf:** The leaf node returns the average value (e.g., 5 houses in this leaf have prices 100k, 110k, 120k, 115k, 105k, so prediction = 110k).
> - In `sklearn`, this is the difference between `DecisionTreeClassifier` and `DecisionTreeRegressor`.

---

<div align="center">

⬅️ [Previous: Section 2 — The Structure](./02_the_structure.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 4 — Practice Scenario](./04_practice_scenario.md)

</div>
