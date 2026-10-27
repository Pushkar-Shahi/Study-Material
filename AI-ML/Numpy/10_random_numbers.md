<div align="center">

# <span style="color:#E67E22">🟧 Level 10: Random Numbers</span>
![Level](https://img.shields.io/badge/Level-10-E67E22) ![Theme](https://img.shields.io/badge/Theme-np.random-E67E22) ![NumPy](https://img.shields.io/badge/NumPy-random-013243)

</div>

> 💡 Random outputs below are **examples**; yours will differ unless you set a seed.

## 🎲 1. Function Overview

| Function | Output | Range |
|----------|--------|-------|
| `np.random.random()` | one float | `0 ≤ x < 1` |
| `np.random.random(n)` | `n` floats | same |
| `np.random.random((r, c))` | `r×c` floats | same |
| `np.random.rand(r, c)` | `r×c` floats | same (dimensions as separate args) |
| `np.random.randint(a, b)` | one int | `a` **inclusive**, `b` **exclusive** |
| `np.random.randint(a, b, n)` | `n` ints | same |
| `np.random.randint(a, b, (r, c))` | `r×c` ints | same |
| `np.random.uniform(a, b)` | one float | between `a` and `b` |
| `np.random.uniform(a, b, size)` | floats | `size` can be `n` or `(r, c)` |
| `np.random.choice(arr, k)` | `k` picks from `arr` | with replacement by default |

> ❌ `np.random.random(3, 4)` → `TypeError: random() takes at most 1 positional argument (2 given)`. Use `np.random.random((3, 4))` or `np.random.rand(3, 4)`.

## 🔢 2. Random Floats

```python
np.random.random(10)                 # 10 values in [0, 1)
np.random.random(12).reshape(3, 4)   # random matrix
np.random.uniform(20, 30, (3, 4))    # 3x4 floats between 20 and 30
```

### Probability simulation
```python
probabilities = np.random.random(20)
high = probabilities[probabilities > 0.5]
perc = len(high) * 100 / 20          # e.g. 45.0
```

## 🎯 3. Random Integers

```python
np.random.randint(1, 11)             # one int, 1..10
np.random.randint(1, 11, 5)          # five ints
np.random.randint(1, 11, (5, 4))     # 5x4 matrix (same idea: randint(...,20).reshape(5,4))
marks = np.random.randint(0, 101, 10)   # 0..100
```

### Dice simulation
```python
dice = np.random.randint(1, 7, 10)             # faces 1..6
prob5 = len(dice[dice == 5]) * 100 / 10        # empirical % of fives, e.g. 40.0
```

> ⚠️ The **stop value is excluded**: use `randint(1, 7)` for a die, `randint(0, 101)` for 0–100.

## 🌱 4. Reproducibility: `seed`

```python
np.random.seed(42)
np.random.randint(1, 11, 5)     # [7 4 8 5 7]   every time
np.random.seed(100)
np.random.randint(1, 11, 5)     # [9 9 4 8 8]   every time
np.random.seed(42)
np.random.randint(1, 100, 10)   # [52 93 15 72 61 21 83 87 75 75]
```

| Without seed | With seed |
|--------------|-----------|
| New numbers each run | Same sequence each run |

> 💡 Call `seed(...)` **right before** generating, since each call consumes the sequence.

## 🎁 5. Random Choice

```python
colors = np.array(["Red", "Blue", "Green", "White"])
np.random.choice(colors)                         # one color
np.random.choice(colors, 3)                      # may repeat, e.g. ['Green' 'Green' 'White']
np.random.choice(colors, 3, replace=False)       # no repeats (lucky draw)
np.random.choice(students, 3, replace=False)     # pick 3 distinct students
```

| `replace` | Meaning |
|-----------|---------|
| `True` (default) | the same item can be picked again |
| `False` | each item picked at most once |

## 🏗️ 6. Mini Project: 20-row Orders Dataset

```python
np.random.seed(100)
order_id   = np.arange(1, 21)
quantity   = np.random.randint(1, 11, 20)
unit_price = np.random.randint(500, 2000, 20)
discount   = np.random.randint(0, 36, 20)
rating     = np.random.randint(1, 6, 20)

data = np.column_stack((order_id, quantity, unit_price, discount, rating))
revenue = quantity * unit_price
data = np.column_stack((data, revenue))      # add 6th column
data[17]                                     # order 18 -> [18 10 1389 33 3 13890]
```

> ⚠️ The call **order matters** with a seed: changing the sequence of `randint` calls changes every column.

> 💡 This revenue uses quantity × price only; the `discount` column (percent, 0–35) is not applied.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `random` / `rand` | Floats in [0, 1) |
| `randint(a, b, size)` | Integers, `b` excluded |
| `uniform(a, b, size)` | Floats in a range |
| `choice(..., replace=)` | Sampling from a list |
| `seed(n)` | Repeatable results |
| Dataset building | `column_stack` of random columns |

---
⬅️ [Previous](09_joining_and_splitting_arrays.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Missing Values and NaN](11_missing_values_and_nan.md)
