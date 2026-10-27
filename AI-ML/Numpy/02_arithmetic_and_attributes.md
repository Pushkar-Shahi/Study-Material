<div align="center">

# <span style="color:#2980B9">🟦 Level 2: Arithmetic and Attributes</span>
![Level](https://img.shields.io/badge/Level-2-2980B9) ![Theme](https://img.shields.io/badge/Theme-Vectorization-2980B9) ![NumPy](https://img.shields.io/badge/NumPy-shape-013243)

</div>

## ➕ 1. Array and Scalar Operations
Operations apply to **every element** (vectorization).

```python
an = np.array([3, 5, 6])
an + 5     # [ 8 10 11]
an - 5     # [-2  0  1]
an * 5     # [15 25 30]
an / 2     # [1.5 2.5 3. ]
an ** 2    # [ 9 25 36]
```

### 🆚 List vs array behavior

| Expression | List | NumPy array |
|-----------|------|-------------|
| `x + 2` | `TypeError` | adds 2 to each |
| `x * 2` | repeats: `[10,20,30,10,20,30]` | doubles: `[20 40 60]` |
| `a + b` | concatenates | element-wise sum |
| `a * b` | `TypeError` | element-wise product |

## 🔗 2. Array and Array Operations

```python
a = np.array([10, 20, 30, 40]);  b = np.array([1, 2, 3, 4])
a + b   # [11 22 33 44]
a - b   # [ 9 18 27 36]
a * b   # [ 10  40  90 160]
```

> ❌ Different lengths fail: `np.array([10,20,30,40]) + np.array([1,2,3])` → `ValueError: operands could not be broadcast together with shapes (4,) (3,)`

2D arrays work the same way with scalars: `marks + 5`, `marks * 2`, `marks - 10` change every cell.

## 🧮 3. Percentage Patterns

| Goal | Formula | Example |
|------|---------|---------|
| Add p% | `x * (1 + p/100)` | GST 18%: `prices * 1.18` |
| Subtract p% | `x * (1 - p/100)` | 10% off: `prices * 0.90` |
| Amount only | `x * p/100` | `discount = prices * 0.10` |

```python
prices = np.array([50, 100, 40, 90, 80])
prices * 1.18        # [ 59. 118.  47.2 106.2  94.4]   (p + 0.18p = 1.18p)
```

> 💡 Two equivalent routes: `price - price*0.10` and `price*0.90` give the same result.

## 🧪 4. Worked Examples

| Task | Code | Output |
|------|------|--------|
| Celsius → Fahrenheit | `c*9/5 + 32` for `[0 10 20 30 40]` | `[ 32. 50. 68. 86. 104.]` |
| Revenue per product | `prices * units` | `[3000 3200 3750 12000]` |
| 5% forecast uplift | `revenue * 1.05` | `[3150. 3360. 3937.5 12600.]` |
| 15% sales growth | `sales*1.15`, extra = `sales*0.15` | `[143750. 170200. 155250. 197800.]` |
| Grace marks then 10% scale | `(scores + 3) * 1.1` | `[52.8 64.9 77. 89.1 101.2]` |
| 12% hike + ₹50 packaging | `prices*0.12` → add → `+ 50` | `[608.88 944.88 1504.88 2288.88 2848.88]` |
| Targets vs actual | `np.linspace(20000,100000,9)`; `actual - targets` | `[-2000 -2000 -1000 -3000 -3000 -4000 -4000 0 5000]` |
| Branch inventory | `A + B`, `abs(A - B)`, `A + B + 20` | element-wise |

```python
A = np.array([120, 150, 180, 100, 200])
B = np.array([80, 130, 170, 120, 150])
A + B ; abs(A - B) ; A + B + 20
```

## 📐 5. Array Attributes

| Attribute | Meaning | 1D `[70 80 65 90 85]` | 2D 3×4 |
|-----------|---------|-----------------------|--------|
| `.ndim` | number of dimensions | `1` | `2` |
| `.shape` | size per dimension | `(5,)` | `(3, 4)` |
| `.size` | total elements | `5` | `12` |
| `len(a)` | length of **first** axis | `5` | `3` |
| `.dtype` | element type | `int64` | `int64` |

```python
a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
a.ndim     # 3
```

For a `(rows, cols)` array: `shape[0]` = rows (students), `shape[1]` = columns (subjects).

> ⚠️ **Gotcha:** `len()` ≠ `size` for 2D arrays. `len(data)=3`, `data.size=12`.

> 💡 Mixing an int array with a float (e.g. `a * 2.0`, or int + float array) gives a `float64` result.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| Scalar ops | Change every element at once |
| Array–array ops | Element-wise math (same length required) |
| `* 1.p` / `* 0.p` | Percentage increase / decrease |
| `ndim`, `shape`, `size`, `len` | Describe the array's structure |

## 📝 Practice (no solution in source)

1. A website gives 10% off, then 5% off the **already discounted** price on `[1000, 2000, 3000, 4000]`. Final prices?
   > 💡 Hint: chain the multipliers, `prices * 0.90 * 0.95`.
2. Revenue `[80000, 95000, 110000, 125000, 140000, 155000]` grows 12%. Find the increase and forecast, build a target with `np.linspace(80000, 160000, 6)`, then compare.
   > 💡 Hint: `increase = rev*0.12`, `forecast = rev*1.12`, `forecast - target`.
3. Production starts at 100 units and rises 50/day for 10 days, then +10%.
   > 💡 Hint: `np.arange(100, 600, 50)` gives 10 values, then `* 1.1`.

---
⬅️ [Previous](01_arrays_and_creation.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Indexing and Slicing](03_indexing_and_slicing.md)
