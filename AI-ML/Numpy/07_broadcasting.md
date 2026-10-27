<div align="center">

# <span style="color:#27AE60">🟩 Level 7: Broadcasting</span>
![Level](https://img.shields.io/badge/Level-7-27AE60) ![Theme](https://img.shields.io/badge/Theme-Broadcasting-27AE60) ![NumPy](https://img.shields.io/badge/NumPy-shapes-013243)

</div>

## 💡 1. What Is Broadcasting?
NumPy **stretches** a smaller array so it can be combined with a bigger one, without writing a loop.

## 🔁 2. Scalar + Array (loop vs vectorized)

```python
marks = np.array([70, 80, 90])

updated_marks = np.zeros(len(marks), dtype=int)   # manual loop version
for i in range(len(marks)):
    updated_marks[i] = marks[i] + 5

updated_marks = marks + 5                         # broadcasting: same result [75 85 95]
```

| Approach | Lines | Result |
|----------|:-----:|--------|
| Loop + `np.zeros` + index | 4 | `[75 85 95]` |
| `marks + 5` | 1 | `[75 85 95]` |

## ➕ 3. Same-Shape Arrays (no stretching)

```python
a = np.array([70, 80, 90]);  b = np.array([10, 20, 30])
a + b      # [ 80 100 120]   element by element
```

## 🧱 4. Column Vector + Matrix

```python
a = np.arange(1, 13).reshape(3, 4)     # shape (3, 4)
b = np.arange(1, 4).reshape(3, 1)      # shape (3, 1)  one value per row
a + b
# [[ 2  3  4  5]
#  [ 7  8  9 10]
#  [12 13 14 15]]
```

| Row of `a` | Value from `b` | Result |
|-----------|:--------------:|--------|
| `[1 2 3 4]` | `1` | `[2 3 4 5]` |
| `[5 6 7 8]` | `2` | `[7 8 9 10]` |
| `[9 10 11 12]` | `3` | `[12 13 14 15]` |

> 💡 The single column of `b` is **repeated across all 4 columns** of `a`. `reshape(3, 1)` (or `reshape(-1, 1)`) is how you create such a column.

> ⚠️ Compare with [Level 2](02_arithmetic_and_attributes.md): two **1D** arrays of different lengths (`(4,)` and `(3,)`) fail with `ValueError: operands could not be broadcast together`. Broadcasting works when the dimensions line up, like `(3,4)` and `(3,1)`.

## 🧭 Summary Table

| Combination | Behavior |
|-------------|----------|
| array + scalar | scalar applied to every element |
| array + same-shape array | element-wise |
| `(3,4)` + `(3,1)` | column repeated across columns |
| `(4,)` + `(3,)` | ❌ `ValueError` |

---
⬅️ [Previous](06_reshape_and_flatten.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Stats Toolkit and Time Series](08_stats_toolkit_and_time_series.md)
