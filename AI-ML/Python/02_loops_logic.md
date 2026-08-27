<div align="center">

# <span style="color:#1E6FEB">🔵 Level 2 — Loops & Logic</span>

![Level](https://img.shields.io/badge/Level-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Repeating_Actions-1E6FEB)

</div>

---

## 🔁 `for` Loop

Used when the number of iterations is **known in advance**.

```python
for i in range(0, 10, 2):   # start=0, stop=10 (excluded), step=2
    print(i)
```

> [!NOTE]
> `range(start, stop, step)` — `start` is **included**, `stop` is **excluded**.

---

## 🔄 `while` Loop

Runs as long as a condition stays `True`. Needs **3 essential parts**:

| Part | Role | Example |
|---|---|---|
| Initialization | Set starting value | `i = 0` |
| Condition | Checked every loop | `while i < 5:` |
| Update | Prevents infinite loop | `i += 1` |

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 🎮 Loop Control Statements

| Statement | Effect |
|---|---|
| `break` | Immediately exits the loop |
| `continue` | Skips the rest of this iteration, jumps to the next |

```python
for i in range(10):
    if i == 5:
        break        # stop entirely at 5
    if i % 2 == 0:
        continue     # skip even numbers
    print(i)
```

---

## 🔀 Nested Loops

A loop placed **inside** another loop — great for grids and patterns.

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

> [!TIP]
> Common use cases: printing patterns, iterating through 2D data/grids — very relevant for working with matrices in NumPy!

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `for` | Iterate a known number of times |
| `while` | Iterate until a condition becomes false |
| `break` / `continue` | Control loop flow |
| Nested loops | Handle multi-dimensional iteration |

---

### 🛠️ MLOps Perspective: Loops in Pipelines
> [!NOTE]
> Loops are everywhere in MLOps:
> - **`for` loops** iterate over model hyperparameters during grid search or batches of files in a data ingestion pipeline
> - **`while` loops** are used for retry logic in API calls (e.g., keep retrying a failed cloud API request until it succeeds or a max retry count is hit)
> - **`break`** is used in early stopping implementations — stop training if the validation loss hasn't improved in N epochs

---

<div align="center">

⬅️ [Previous: Level 1 — Fundamentals](./01_fundamentals.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 3 — Data Structures](./03_data_structures.md)

</div>
