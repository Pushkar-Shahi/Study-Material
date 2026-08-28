<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — Calculating Gini Decisions</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_The_Math-1E6FEB)

</div>

---

## 1️⃣ The Overall Gini Decision

First, calculate the Gini Index for the **entire dataset** to understand the distribution of final choices.

| Dataset | Value |
|---|:---:|
| Total instances | 10 |
| Possible outcomes | Cinema, Tennis, Shopping, Stay in |
| **Overall Gini Decision** | **0.58** |

---

## 2️⃣ Weighted Averages for Each Variable

For each supporting variable, calculate the Gini Index of its sub-categories, then find the **weighted average** based on how often each appears in the 10 instances.

### 💰 Money

| Category | Gini |
|---|:---:|
| Rich | 0.694 |
| Poor | 0 |
| **Weighted Average** | **0.486** |

### 👨‍👩‍👧 Parents

| Category | Gini |
|---|:---:|
| Yes | 0 |
| No | 0.72 |
| **Weighted Average** | **0.36** |

### 🌦️ Weather

| Category | Gini |
|---|:---:|
| Sunny, Windy, Rainy (combined) | — |
| **Weighted Average** | **0.416** |

---

## 3️⃣ Choosing the Root Node

The variable with the **lowest** weighted Gini Index becomes the root node.

| Variable | Weighted Gini | Selected? |
|---|:---:|:---:|
| Money | 0.486 | ❌ |
| **Parents** | **0.36** | ✅ **Lowest — wins!** |
| Weather | 0.416 | ❌ |

> [!WARNING]
> **Rule:** The **lowest** Gini Index = the **cleanest** split = the best candidate for the top of the tree.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Overall Gini Decision | Baseline "impurity" of the full dataset |
| Weighted average Gini | Combines sub-category Gini values by frequency |
| Lowest Gini wins | Determines which variable becomes the root node |
| Result: Parents (0.36) | The winning root node for this dataset |

---

### 🛠️ MLOps Perspective: Hyperparameter Tuning the Splitting Metric
> [!IMPORTANT]
> The math you just did manually is executed thousands of times per second during model training.
> - By default, algorithms like Random Forest test a random subset of features (like "Money" or "Weather") at each node, rather than *all* features. This prevents overfitting and forces tree diversity.
> - You can tune the criterion hyperparameter in sklearn to use gini or entropy. 
> - **In practice:** Both yield very similar trees! MLOps engineers usually leave it as gini by default because it's slightly faster to compute across huge datasets.

---

<div align="center">

⬅️ [Previous: Section 1 — The Basics](./01_the_basics.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — Building the Tree](./03_building_the_tree.md)

</div>
