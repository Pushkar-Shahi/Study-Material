<div align="center">

# <span style="color:#27AE60">🟩 Level 1: Arrays and Creation</span>
![Level](https://img.shields.io/badge/Level-1-27AE60) ![Theme](https://img.shields.io/badge/Theme-Creation-27AE60) ![NumPy](https://img.shields.io/badge/NumPy-ndarray-013243)

</div>

## 🤔 1. Why NumPy?
Python lists don't support element-wise math.

```python
marks = [55, 90, 40, 70, 80]
marks + 5        # TypeError: can only concatenate list (not "int") to list
```

```python
marks = np.array([55, 90, 40, 70, 80])
marks + 10       # [ 65 100  50  80  90]
```

| Python list | NumPy array |
|-------------|-------------|
| Needs a `for` loop to change every item | One expression changes every item |
| `+` concatenates | `+` adds element-wise |
| Can mix types freely | One dtype for the whole array |

## 🏗️ 2. Creating Arrays from Data

```python
np.array([4, 6, 8, 2, 1])            # from list  -> [4 6 8 2 1]
np.array((4, 6, 3, 1))               # from tuple -> [4 6 3 1]
np.array([[2,4,5],[6,3,1],[5,7,2]])  # 2D from nested list
np.array(["AJ", "Riya", "Raj"])      # string array
np.array([True, False, False])       # bool array
type(np.array([1]))                  # numpy.ndarray
```

> ⚠️ **Mixed types get coerced.** `np.array([3, 5.6, "AJ", True])` gives `['3' '5.6' 'AJ' 'True']`, everything becomes a string.

## 🧱 3. Built-in Creation Functions

| Function | Example | Result |
|----------|---------|--------|
| `np.zeros(n)` | `np.zeros(5)` | `[0. 0. 0. 0. 0.]` |
| `np.zeros((r,c))` | `np.zeros((4,3))` | 4×3 of `0.` |
| `np.ones(n)` | `np.ones(4)` | `[1. 1. 1. 1.]` |
| `np.full(n, v)` | `np.full(6, 2)` | `[2 2 2 2 2 2]` |
| `np.full((r,c), v)` | `np.full((3,4), 2)` | 3×4 of `2` |
| `np.arange(stop)` | `np.arange(5)` | `[0 1 2 3 4]` |
| `np.arange(start, stop)` | `np.arange(1,11)` | `1 … 10` |
| `np.arange(start, stop, step)` | `np.arange(2,21,3)` | `[ 2 5 8 11 14 17 20]` |
| `np.linspace(start, stop, n)` | `np.linspace(0,10,5)` | `[ 0. 2.5 5. 7.5 10.]` |

### 🆚 `arange` vs `linspace`

| | `arange` | `linspace` |
|--|----------|-----------|
| You choose | the **step** | the **count** of values |
| Stop value | excluded | **included** |
| Even numbers 0–10 | `np.arange(0,11,2)` → `[0 2 4 6 8 10]` | `np.linspace(0,10,6)` → `[0. 2. 4. 6. 8. 10.]` |
| dtype | `int64` | `float64` |

> 💡 "Exactly N equally spaced values" → `linspace`. "Every k-th number" → `arange`.

## 🏷️ 4. Data Types (`dtype`)

```python
a = np.array([True, False]);  a.dtype      # bool
b = np.array([4, 6, 3.5]);    b.dtype      # float64 (ints promoted to float)
np.array([10,20,30], dtype=float)          # [10. 20. 30.]
np.array([10.5, 4.7, 7], dtype=int)        # [10  4  7]   (truncated)
np.array([2,4,0,7,0], dtype=bool)          # [ True True False True False]
```

| Rule | Detail |
|------|--------|
| Float → int | Decimal part is **cut off** (10.5 → 10) |
| Int → bool | `0` → `False`, any non-zero → `True` |
| `.astype(int)` | Makes a converted copy; original unchanged |
| Int + float arrays | Result is `float64` |

```python
arr = np.array([10.5, 20.7, 30.9])
arr.astype(int)                  # [10 20 30]
np.array(["AJ","Raj"], dtype=int)  # ValueError: invalid literal for int()
```

> ⚠️ Strings that aren't numbers can't be cast to `int`.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `np.array` | Convert list/tuple to ndarray |
| `zeros` / `ones` / `full` | Pre-filled arrays |
| `arange` | Range with a step (stop excluded) |
| `linspace` | Fixed count, evenly spaced (stop included) |
| `dtype` / `astype` | Inspect or convert element type |

---
🏠 [Roadmap](00_README.md) | ➡️ [Next: Arithmetic and Attributes](02_arithmetic_and_attributes.md)
