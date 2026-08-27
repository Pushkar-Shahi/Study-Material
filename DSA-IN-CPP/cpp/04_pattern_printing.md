<div align="center">

# <span style="color:#E07B00">🟠 Phase 4 — Pattern Printing</span>

![Phase](https://img.shields.io/badge/Phase-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Nested_Loop_Mastery-E07B00)

</div>

---

## 🧩 Core Logic

| Loop | Controls |
|---|---|
| **Outer Loop** | Number of rows |
| **Inner Loop** | What's printed in each column (stars, numbers, letters) |
| **Conditionals** | Used inside loops for hollow shapes, crosses, plus signs |

---

## ⭐ Star Triangle

```cpp
void starTriangle(int x) {
    for(int i = 1; i <= x; i++) {       // Outer loop → rows
        for(int j = 1; j <= i; j++) {    // Inner loop → stars per row
            cout << "*";
        }
        cout << endl;
    }
}
```

```
*
* *
* * *
* * * *
```

> [!NOTE]
> The number of stars per row matches the current row number.

---

## 🔢 Floyd's Triangle

Numbers **keep incrementing** across every row instead of resetting.

```cpp
int n = 4;   // Number of rows
int a = 1;   // Extra variable — tracks the continuous count
for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= i; j++) {
        cout << a << " ";
        a++;
    }
    cout << endl;
}
```

```
1
2 3
4 5 6
7 8 9 10
```

| Component | Role |
|---|---|
| Extra variable (`a`) | Tracks the running count, declared **outside** the loops |
| Outer loop | Controls total rows |
| Inner loop | Prints current `a`, then increments it |

---

## 🗂️ Other Common Patterns

| Pattern | Description |
|---|---|
| 🔲 Squares / Rectangles | Stars or numbers in a grid |
| 🔃 Flipped Triangles | Horizontally or vertically mirrored |
| 🔤 Alphabet Triangles | ASCII characters instead of numbers |
| 🔺 Pyramids & Diamonds | Centered shapes — requires managing **leading spaces** |
| 🔢 Number Spirals | Values change based on coordinates |

> [!TIP]
> **Pascal's Triangle** (combinations-based) is covered as an advanced topic — see [Phase 6](./06_advanced_topics.md).

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Nested loops | Foundation of all pattern printing |
| Outer loop | Row control |
| Inner loop | Column/content control |
| Extra tracking variable | Needed for continuously incrementing patterns |
| Leading spaces | Needed for centered shapes like pyramids |

---

### 🛠️ MLOps Perspective: Nested Loops & Matrix Operations
> [!NOTE]
> Pattern printing with nested loops is the gateway to understanding **matrix and tensor operations** — the foundation of all of deep learning:
> - A 2D image (e.g., 28×28 pixels) is iterated with nested loops: outer loop = rows, inner loop = columns
> - **Convolution operations** in CNNs are essentially nested loops sliding a kernel over an image
> - **Attention mechanisms** in Transformers compute a score for every pair (i, j) of tokens — a nested loop over sequence length
> - Mastering nested loop complexity (O(n²)) helps you reason about model inference time and batch processing efficiency

---

<div align="center">

⬅️ [Previous: Phase 3 — Loops](./03_loops.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Phase 5 — Functions & Pointers](./05_functions_pointers.md)

</div>
