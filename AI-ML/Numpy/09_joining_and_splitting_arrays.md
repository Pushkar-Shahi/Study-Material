<div align="center">

# <span style="color:#D4AC0D">🟨 Level 9: Joining and Splitting Arrays</span>
![Level](https://img.shields.io/badge/Level-9-F1C40F) ![Theme](https://img.shields.io/badge/Theme-Combine_Split-F1C40F) ![NumPy](https://img.shields.io/badge/NumPy-stack-013243)

</div>

## 🔗 1. Joining Arrays

| Function | Joins | Typical use |
|----------|-------|-------------|
| `np.concatenate((a, b, …), axis=0)` | along an existing axis | any number of arrays |
| `np.vstack((a, b))` | **vertically** (add rows) | stack months/records |
| `np.hstack((a, b))` | **horizontally** (add columns) | add a feature column |
| `np.column_stack((a, b, c))` | 1D arrays as **columns** | build a table from fields |

> 💡 Pass the arrays as **one tuple**: `np.concatenate((a, b))`, not `np.concatenate(a, b)`.

### 1D arrays
```python
np.concatenate((january, february))   # [120 150 180 140 160 200]
np.concatenate((a, b, c))             # 3 arrays at once
np.hstack((a, b))                     # works even if lengths differ: [1 2 3 7 4 5 6]
```

### 2D arrays and `axis`
```python
a = np.array([[1,2],[3,4]]);  b = np.array([[5,6],[7,8]])
np.concatenate((a, b))              # axis=0 (default) -> [[1 2] [3 4] [5 6] [7 8]]
np.concatenate((a, b), axis=1)      # side by side    -> [[1 2 5 6] [3 4 7 8]]
```

| `axis` | Result | Equivalent |
|:------:|--------|-----------|
| `0` | stacks **down** (more rows) | `vstack` |
| `1` | stacks **across** (more columns) | `hstack` |

> ❌ **Source comment is reversed:** one notebook comment says `axis = 1 ==> along the rows/ vertically` and `axis = 0 ==> horizontally`. The **actual outputs** show the opposite (axis 0 adds rows, axis 1 adds columns). Follow the table above.

> ⚠️ **Shape rules** (all dimensions *except the joining axis* must match):
> - `(3,2)` and `(2,2)` with `axis=1` → `ValueError` (3 rows vs 2 rows). With `axis=0` it works → 5 rows.
> - `np.vstack` of lengths `4` and `3` → `ValueError`.
> - `np.vstack((sales_data, bonus))` with `(3,2)` and `(3,1)` → `ValueError`; use `hstack`.

## 🧱 2. Building Tables

### vstack: records of the same width
```python
overall_sales = np.vstack((jan_sales, feb_sales, mar_sales))   # 3 months x 3 products
sales_data = np.vstack((jan, feb))                             # (3,2) + (3,2) -> (6,2)
```

### hstack: add a column (needs a column shape)
```python
sales_data = np.array([[101,5000],[102,7000],[103,4500]])
bonus = np.array([[500],[700],[450]])         # shape (3,1)
np.hstack((sales_data, bonus))                # [[101 5000 500] ...]
```

### `reshape(-1, 1)`: turn a 1D array into a column
```python
ids = np.array([101, 102, 103]).reshape(-1, 1)
salary = np.array([50000, 65000, 72000]).reshape(-1, 1)
experience = np.array([3, 5, 7]).reshape(-1, 1)
np.hstack((ids, salary, experience))          # 3x3 table
```

### `column_stack`: same result without reshaping
```python
np.column_stack((ids, salary, experience))    # works directly on 1D arrays
revenue = quantity * price
np.column_stack((quantity, price, revenue))   # add a computed column
```

| Approach | Needs `reshape(-1,1)`? |
|----------|:---------------------:|
| `np.hstack` on 1D arrays | ✅ yes (otherwise it makes one long 1D array) |
| `np.column_stack` on 1D arrays | ❌ no |

> 💡 Four weekly quantity arrays of 7 items, each reshaped to `(7,1)` and hstacked, give shape `(7, 4)`.

## ✂️ 3. Splitting Arrays

```python
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80])
parts = np.split(numbers, 2)    # [array([10 20 30 40]), array([50 60 70 80])]
parts = np.split(numbers, 4)    # four arrays of 2
parts = np.split(numbers, [3, 5])   # split at positions: [10 20 30] [40 50] [60 70 80]
```

| Call | Meaning |
|------|---------|
| `np.split(a, n)` | `n` **equal** parts (size must divide evenly) |
| `np.split(a, [i, j])` | cut **before index** `i` and `j` (unequal parts allowed) |
| `np.split(a2d, 2, axis=0)` | split rows into 2 groups |
| `np.split(a2d, 2, axis=1)` | split columns into 2 groups |

```python
data = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
np.split(data, 2, axis=0)   # top 2 rows | bottom 2 rows
np.split(data, 2, axis=1)   # left 2 columns | right 2 columns
```

> ❌ `np.split(numbers, 3)` on 8 items → `ValueError: array split does not result in an equal division`. Same for `np.split(arr, 5)` on 12 items.

> ⚠️ **The result is a Python list**, not an array. Use `parts[0]`, `parts[3]`, or loop `for p in parts`. `parts[(0,3)]` raises `TypeError`.

## 🧪 4. Use Cases

| Scenario | Code |
|----------|------|
| Train/test split (10×2 data) | `train = data[:8]`, `test = data[-2:]` |
| 12 monthly sales → 4 quarters | `np.split(sales, 4)` → four arrays of 3 |

> 💡 For a train/test split, **slicing** is enough because the parts have unequal sizes (8 and 2).

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `concatenate(axis)` | General joining |
| `vstack` / `hstack` | Add rows / add columns |
| `reshape(-1,1)` | Make a column vector |
| `column_stack` | Build a table from 1D fields |
| `np.split` | Cut into equal or indexed parts (returns a list) |

## 📝 Practice

1. Join `[[1,2],[3,4],[6,7]]` with `[[5,6],[7,8]]` so it **works**. 
   > 💡 Hint: the working call is `axis=0`.
2. Split a `(4,4)` array into 4 parts of one row each. 
   > 💡 Hint: `np.split(data, 4, axis=0)`.

---
⬅️ [Previous](08_stats_toolkit_and_time_series.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Random Numbers](10_random_numbers.md)
