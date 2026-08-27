<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — The Structure</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Anatomy_of_a_Tree-1E6FEB)

</div>

---

## 🏗️ The Structural Components

A Decision Tree is a **hierarchy of questions** that systematically narrows down information until a conclusion is reached.

| Component | Description |
|---|---|
| 🔲 **Decision Nodes** | The main components — the specific criteria/questions being asked (e.g., "Employed," "Salary," "Credit Score") |
| 🔀 **Branching (Paths)** | Each node splits into branches based on the possible answers |
| 🔄 **Sequential Logic** | The answer to one question determines exactly which node comes next |
| 🔽 **Narrowing Down** | Information gets more specific the deeper you go |
| 🍃 **Leaf Nodes (Bottom Line)** | The end of the tree — a final classification or decision |

---

## 🌳 Visualizing the Structure

```
[Decision Node: "Employed?"]
        ├── Yes → [Decision Node: "Salary?"]
        │             ├── High → 🍃 "Loan Accepted"
        │             └── Low  → 🍃 "Loan Rejected"
        └── No  → 🍃 "Loan Rejected"
```

---

## 🔀 Example Branch Breakdown

| Node | Possible Branches |
|---|---|
| "Employed" | → "Yes" or "No" |
| "Salary" | → "High" or "Low" |
| "Credit Score" | → "Good" or "Poor" |

> [!TIP]
> The tree stops asking questions once it hits a **Leaf Node** — at that point, no more branching is possible.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Decision Node | A question/criterion that the tree evaluates |
| Branch | A possible answer path from a node |
| Sequential logic | Determines which node comes next based on the previous answer |
| Leaf Node | The final classification — where the tree terminates |

---

### 🛠️ MLOps Perspective: Tree Depth & Overfitting
> [!IMPORTANT]
> The **depth** of a tree is how many sequential questions it asks before reaching a leaf.
> - A tree that is too shallow (e.g., depth 1, called a "Decision Stump") will underfit the data and make poor predictions.
> - A tree with no depth limit will keep asking questions until every single leaf node perfectly isolates exactly one training example. This is massive **Overfitting** — the tree memorized the training data but will fail horribly in production.
> - In `sklearn`, controlling this is a crucial hyperparameter: `DecisionTreeClassifier(max_depth=5, min_samples_split=10)`.

---

<div align="center">

⬅️ [Previous: Section 1 — The Concept](./01_the_concept.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — The Purpose](./03_the_purpose.md)

</div>
