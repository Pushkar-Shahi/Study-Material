<div align="center">

# <span style="color:#E67E22">🟧 Level 4: Math and Statistics</span>
![Level](https://img.shields.io/badge/Level-4-E67E22) ![Theme](https://img.shields.io/badge/Theme-Aggregation-E67E22) ![NumPy](https://img.shields.io/badge/NumPy-ufuncs-013243)

</div>

## 🧮 1. Mathematical Functions

| Function | Example | Result |
|----------|---------|--------|
| `np.sqrt(a)` | `np.sqrt([4,9,16,25])` | `[2. 3. 4. 5.]` |
| `np.power(a, n)` / `a**n` | `np.power([3,5,8], 3)` | `[ 27 125 512]` |
| `np.cbrt(a)` / `a**(1/3)` | `np.cbrt([27,125,512])` | `[3. 5. 8.]` |
| `np.abs(a)` | `np.abs([-10,-5,0,5,10])` | `[10 5 0 5 10]` |
| `np.square(a)` | squares each value | — |

```python
x = np.array([3, 5, 8]); y = np.array([4, 12, 15])
np.sqrt(x**2 + y**2)      # distance from origin -> [ 5. 13. 17.]
np.sqrt(np.square(a))     # another way to get abs
```

## 🎯 2. Rounding Functions

Given `[2.9, 5.7, -3.8, -7.2]` and `[2.1, 2.9, 5.5, 7.99]`:

| Function | Behavior | Example |
|----------|----------|---------|
| `np.around(a)` / `np.round(a)` | nearest integer | `[10.2345, 20.6789, 30.4567]` → `[10. 21. 30.]` |
| `np.around(a, 2)` | 2 decimals | `[10.23 20.68 30.46]` |
| `np.floor(a)` | round **down** | `[2.1 2.9 5.5 7.99]` → `[2. 2. 5. 7.]` |
| `np.ceil(a)` | round **up** | → `[3. 3. 6. 8.]` |
| `np.trunc(a)` | drop decimals (toward 0) | `[2.9 5.7 -3.8 -7.2]` → `[ 2. 5. -3. -7.]` |

> 💡 `floor` vs `trunc` differ only for **negatives**: floor(−3.8) = −4, trunc(−3.8) = −3.

## 📊 3. Statistics Functions

```python
sales = np.array([100, 200, 300, 400, 500])
np.sum(sales)      # 1500
np.mean(sales)     # 300.0
np.min(sales)      # 100
np.max(sales)      # 500
np.median(sales)
np.std(sales)
np.argmax(sales)   # index of max
np.argmin(sales)   # index of min
```

| Function | Returns |
|----------|---------|
| `sum` / `mean` | total / average |
| `min` / `max` | smallest / largest |
| `median` | middle value (robust to outliers) |
| `std` | spread around the mean |
| `argmax` / `argmin` | **index**, not value |

> ❌ `np.avg` does not exist (`AttributeError`). Use `np.mean`.

> 💡 If the maximum appears twice (e.g. 95 at indexes 6 and 8), `np.argmax` returns the **first** index (6).

### 🔍 Outlier example
`[45000, 47000, 49000, 52000, 50000, 48000, 250000]`

| Measure | Value |
|---------|-------|
| Mean | 77285.71 |
| Median | 49000 |
| Std | 70540.19 |

> 🧠 The median (49,000) represents a typical day better because the 250,000 spike drags the mean up.

### 🛠️ Manual min/max loops (what NumPy replaces)

```python
mn = sales[0]            # start from the FIRST ELEMENT
for s in sales:
    if s < mn:
        mn = s
```

> ⚠️ **Initialization gotcha:** starting `mn = 0` returns `0` for positive data, and `mx = 0` returns `0` for all-negative data. Always initialize with `sales[0]`.

## 🧭 4. The `axis` Parameter (2D)

| `axis` | Collapses | Gives |
|:------:|-----------|-------|
| `0` | down the rows | one result **per column** |
| `1` | across the columns | one result **per row** |
| none | everything | one number |

```python
sales = np.array([[120,150,180],[200,170,160],[100,140,130],[180,190,210]])
np.sum(sales, axis=1)    # per salesperson [450 530 370 580]
np.mean(sales, axis=0)   # per month       [150.  162.5 170.]
np.max(sales, axis=1)    # best per person [180 200 140 210]
```

Student marks (5×4): `np.mean(marks, axis=1)` → per-student averages, `np.max(marks, axis=0)` → top mark per subject.

## 🧾 5. Chained Case Study (online store prices)

```python
prices = np.array([499.50, 799.90, 1299.75, 2499.50, 3999.90, 599.25, 899.80, 1599.40])
np.round(prices)                                  # nearest whole number
disc = np.round(prices[prices > 1000] * 0.85)     # 15% off items > ₹1000
np.mean(disc)                                     # 1997.25
np.max(prices), np.argmax(prices)                 # 3999.9, 4
prices[-4:]                                       # last 4 products
np.round(np.sqrt(disc), 2)                        # [33.24 46.1 58.31 36.86]
```

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `sqrt`, `power`, `cbrt`, `abs` | Element-wise math |
| `round`, `floor`, `ceil`, `trunc` | Control decimals |
| `sum`, `mean`, `median`, `std` | Describe data |
| `argmax`, `argmin` | Locate extremes |
| `axis=0/1` | Column-wise / row-wise stats |

## 📝 Practice (no solution in source)

1. Median of `[50, 30, 10, 190, 100]`.
   > 💡 Hint: sort mentally, the middle value is 50; verify with `np.median`.

---
⬅️ [Previous](03_indexing_and_slicing.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Boolean Filtering and np.where](05_boolean_filtering_and_where.md)
