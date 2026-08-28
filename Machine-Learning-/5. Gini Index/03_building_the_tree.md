<div align="center">

# <span style="color:#D4A017">🟡 Section 3 — Building the Tree</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Putting_It_All_Together-D4A017)

</div>

---

## 🔝 1. The Root Node — Parents

Since **Parents** had the lowest initial Gini Index (**0.36**), it sits at the very top of the tree.

```
[Root Node: Parents?]
        ├── Yes → ?
        └── No  → ?
```

---

## ✅ 2. The "Yes" Branch

| Condition | Result |
|---|---|
| Parents = "Yes" | Decision is **always** Cinema |

> [!TIP]
> No uncertainty → this branch ends **immediately** at a final decision.

```
Parents = Yes → 🍃 "Cinema"
```

---

## 🔄 3. The "No" Branch

When Parents = "No," the outcomes are **mixed** (Tennis, Stay in, etc.) — another question is needed.

| Remaining Variable | Gini |
|---|:---:|
| **Weather** | **0.2** ✅ Lowest — wins! |
| Money | 0.5 |

```
Parents = No → [Next Node: Weather?]
```

---

## 🌦️ 4. Splitting the Weather Node

Weather branches into **three** possibilities:

| Branch | Outcome |
|---|---|
| ☀️ **Sunny** | Clear decision → 🍃 "Tennis" |
| 🌧️ **Rainy** | Clear decision → 🍃 "Stay in" |
| 🌬️ **Windy** | Still mixed → needs **one more** split |

```
Weather:
   ├── Sunny → 🍃 "Tennis"
   ├── Rainy → 🍃 "Stay in"
   └── Windy → ?
```

---

## 💰 5. Final Decision — Money (Under "Windy")

The last remaining factor, **Money**, resolves the Windy branch.

| Condition | Final Decision |
|---|---|
| Rich | 🍃 "Cinema" |
| Poor | 🍃 "Shopping" |

```
Windy:
   ├── Rich → 🍃 "Cinema"
   └── Poor → 🍃 "Shopping"
```

---

## 🌳 The Complete Decision Tree

```
[Root Node: Parents?]
        ├── Yes → 🍃 "Cinema"
        └── No  → [Weather?]
                      ├── Sunny → 🍃 "Tennis"
                      ├── Rainy → 🍃 "Stay in"
                      └── Windy → [Money?]
                                       ├── Rich → 🍃 "Cinema"
                                       └── Poor → 🍃 "Shopping"
```

---

## 📝 Summary Table

| Step | Node | Decision Rule |
|---|---|---|
| 1 | Root Node | Parents — lowest overall Gini (0.36) |
| 2 | "Yes" branch | No uncertainty → ends at "Cinema" |
| 3 | "No" branch | Weather has lowest Gini (0.2) among remaining variables |
| 4 | Weather split | Sunny/Rainy resolve directly; Windy stays mixed |
| 5 | Windy split | Money (last remaining variable) makes the final call |

---

### 🛠️ MLOps Perspective: Greedy Algorithms
> [!IMPORTANT]
> The way you just built this tree is called a **Greedy Algorithm**. 
> - At every single node, you picked the variable with the lowest Gini Index *right then and there*, without looking ahead to see if a different split might be better 3 levels down.
> - **Why Greedy?** Computing every possible full tree combination is NP-complete (computationally impossible for large datasets). Greedy algorithms sacrifice the "perfect global tree" to build a "really good tree" in seconds instead of years.
> - **In Production:** To compensate for trees being "greedy" and sometimes suboptimal, MLOps systems train **hundreds of greedy trees** (Random Forests) and let them vote on the final answer!

---

<div align="center">

⬅️ [Previous: Section 2 — Calculating Gini Decisions](./02_calculating_gini.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full Gini Index & Decision Tree Walkthrough!

</div>
