<div align="center">

# <span style="color:#D4AC0D">🟨 Level 3: Indexing and Slicing</span>
![Level](https://img.shields.io/badge/Level-3-F1C40F) ![Theme](https://img.shields.io/badge/Theme-Selection-F1C40F) ![NumPy](https://img.shields.io/badge/NumPy-slicing-013243)

</div>

## 📍 1. Indexing 1D Arrays

```python
marks = np.array([70, 80, 65, 90, 75])
marks[0]    # 70      first
marks[3]    # 90
marks[-1]   # 75      last (same as marks[n-1])
marks[-2]   # 90
marks[2] = marks[2] + 5   # modify in place -> [70 80 70 90 75]
```

```python
for i in range(len(marks)):
    print(marks[i], end=" ")
```

## 🔪 2. Slicing 1D: `a[start:stop:step]`
Start is included, stop is **excluded**.

| Slice | Meaning | Result on `[70 80 65 90 75]` |
|-------|---------|------------------------------|
| `a[0:3]` / `a[:3]` | first three | `[70 80 65]` |
| `a[2:4]` | index 2–3 | `[65 90]` |
| `a[1:]` | from index 1 | `[80 65 90 75]` |
| `a[::]` | everything | full copy |
| `a[::2]` | every 2nd | `[70 65 75]` |
| `a[1::2]` | every 2nd from 1 | `[80 90]` |
| `a[0:5:2]` | with stop | `[70 65 75]` |
| `a[-3:]` | last three | `[65 90 75]` |
| `a[:-2]` | all but last two | `[70 80 65]` |
| `a[::-1]` | reversed | `[75 90 65 80 70]` |

> ⚠️ **Reverse-last-N gotcha:** `temperature[-4:-1:-1]` returns `[]` (empty). A negative step needs start *after* stop. The working version is `temperature[-1:-5:-1]` → `[29 30 32 34]`.

> ⚠️ **Source inconsistency:** the `numbers[::-1]` demo shows output with `60` although its array was defined with 5 elements (`10…50`). The reversal behavior itself is correct.

## 🧱 3. Indexing 2D Arrays

```python
marks = np.array([[70, 80, 90],
                  [60, 75, 85],
                  [88, 92, 95]])
marks[0][2]    # 90
marks[0,2]     # 90   preferred: [row, col]
marks[2]       # whole third row
marks[:, 1]    # whole second column
marks[-1, -1]  # last row, last column
```

| Goal | Code |
|------|------|
| One row | `a[r]` or `a[r, :]` |
| One column | `a[:, c]` |
| First k rows | `a[:k]` |
| Last 2 columns | `a[:, -2:]` |
| Sub-block | `a[1:3, 1:3]` |
| Top-left 3×3 | `a[:3, :3]` |
| Bottom-right 2×2 | `a[-2:, -2:]` |
| Centre 3×3 of 5×5 | `a[1:4, 1:4]` |

## ✏️ 4. Modifying Through Slices

```python
marks[:, 2] = marks[:, 2] + 5      # +5 to the English column
marks[3, 0] = 75                   # single cell
temperature[:, 0] += 2             # augmented assignment on a column
image[1:4, 1:4] += 20              # centre block
prices[2:5] = prices[2:5] * 0.90   # 10% off items 3-5
seat[2] = 1                        # whole row
seat[5, -2:] = 1                   # last two seats of last row
```

### 🧾 Case studies (from source)

| Scenario | Key code |
|----------|----------|
| Student marks: 3rd student, Science of 2nd | `marks[2]`, `marks[1,1]` |
| Last employee via negative index | `employees[-1]` |
| Last 3 months revenue +10% | `revenue[-3:] = revenue[-3:] * 1.10` |
| Last two products −10% (4×5 stock) | `inventory[:, -2:] = inventory[:, -2:] * 0.90` |
| Basic salary of last two +10% | `salary[-2:, 0] = salary[-2:, 0] * 1.10` |
| Price/quantity columns only | `orders[:, 1:3]` |

> ⚠️ **Integer truncation:** assigning float results into an **int** array silently drops decimals. `employees[2,0] = 50000*1.15` stores `57500` fine, but `orders[-2:,-1]*1.1` stores `330, 990` (truncated). Use `dtype=float` if you need decimals.

> ❌ **Source bug (flagged):** for "increase allowances by ₹1,000" the notebook ran `salary[:,1] += 1000`, then also `*= 1000` and `+ 1000.5`, giving `6001000`. **Working version:** only `salary[:,1] += 1000`.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `a[i]`, `a[-1]` | Pick one element from either end |
| `a[s:e:k]` | Slice with step |
| `a[::-1]` | Reverse |
| `a[r, c]` | 2D element |
| `a[:, c]`, `a[r]` | Column / row |
| `a[r1:r2, c1:c2]` | Sub-matrix |
| Slice assignment | Update many cells in one line |

## 📝 Practice (incomplete in source)

1. Print all **diagonal elements** of a 2D array (cell was started with `row, col = marks.shape` but not finished).
   > 💡 Hint: loop `for i in range(row)` and print `marks[i, i]`.
2. Warehouse A receives 20 extra units of every product (`inventory`, 4×3).
   > 💡 Hint: `inventory[:, 0] += 20`. The source skipped this step, so its final printout lacks it.
3. Display the last 4 temperature readings **in reverse**.
   > 💡 Hint: `temperature[-1:-5:-1]`.

---
⬅️ [Previous](02_arithmetic_and_attributes.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Math and Statistics](04_math_and_statistics.md)
