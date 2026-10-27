<div align="center">

# 🔢 NumPy Essentials and Python Problem Solving
**From Python lists to vectorized data analysis, real-world case studies and interview-style algorithms**

![Levels](https://img.shields.io/badge/Levels-18-blue) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen) ![Language](https://img.shields.io/badge/Language-Python-3776AB) ![Library](https://img.shields.io/badge/Library-NumPy-013243)

*Notes from Earners AI & ML (Aditya Jain Sir), Lectures 49–70*

</div>

---

## 🧭 How This Folder Works
Read the levels **in order**. Each level builds on the previous ones, and every file links to the previous and next level at the bottom.

| Track | Levels | What you get |
|-------|:------:|--------------|
| 🔹 NumPy Core | 1–6 | Arrays, arithmetic, slicing, stats, filtering, reshape |
| 🔸 NumPy Applied | 7–14 | Broadcasting, stats toolkit, joining, random, NaN, selection, two case studies |
| 🐍 Python Problem Solving | 15–18 | Functions, comprehensions, array and string algorithms (no NumPy) |

> 💡 Flags inside the files: ❌ = bug or inconsistency found in the original notebook (with the working version), ⚠️ = gotcha, 💡 = tip.

## 🗺️ Progress Map

### 🔹 NumPy Core
| Level | Focus | File | Status |
|:-----:|-------|------|:------:|
| 🟩 1 | Arrays, creation functions, dtype | [01_arrays_and_creation](01_arrays_and_creation.md) | ✅ |
| 🟦 2 | Vectorized arithmetic, shape attributes | [02_arithmetic_and_attributes](02_arithmetic_and_attributes.md) | ✅ |
| 🟨 3 | Indexing and slicing (1D and 2D) | [03_indexing_and_slicing](03_indexing_and_slicing.md) | ✅ |
| 🟧 4 | Math functions and statistics | [04_math_and_statistics](04_math_and_statistics.md) | ✅ |
| 🟥 5 | Boolean filtering and `np.where` | [05_boolean_filtering_and_where](05_boolean_filtering_and_where.md) | ✅ |
| 🟪 6 | Reshape, flatten, 3D arrays, mixed case studies | [06_reshape_and_flatten](06_reshape_and_flatten.md) | ✅ |

### 🔸 NumPy Applied
| Level | Focus | File | Status |
|:-----:|-------|------|:------:|
| 🟩 7 | Broadcasting: scalar, same-shape, column + matrix | [07_broadcasting](07_broadcasting.md) | ✅ |
| 🟦 8 | var/std, percentile, sort, log/exp, day-to-day change | [08_stats_toolkit_and_time_series](08_stats_toolkit_and_time_series.md) | ✅ |
| 🟨 9 | `concatenate`, `vstack`, `hstack`, `column_stack`, `split` | [09_joining_and_splitting_arrays](09_joining_and_splitting_arrays.md) | ✅ |
| 🟧 10 | `np.random`: random, randint, uniform, choice, seed | [10_random_numbers](10_random_numbers.md) | ✅ |
| 🟥 11 | NaN, `isnan`, `nansum`, valid counts, float dtype | [11_missing_values_and_nan](11_missing_values_and_nan.md) | ✅ |
| 🟪 12 | `np.select`, fancy indexing, `np.minimum`, views | [12_select_fancy_indexing_and_views](12_select_fancy_indexing_and_views.md) | ✅ |
| 🟩 13 | Applied case studies (finance, ops, HR, marketing, images) | [13_applied_case_studies](13_applied_case_studies.md) | ✅ |
| 🟦 14 | Student placement capstone (30 × 11 dataset) | [14_student_placement_case_study](14_student_placement_case_study.md) | ✅ |

### 🐍 Python Problem Solving
| Level | Focus | File | Status |
|:-----:|-------|------|:------:|
| 🟨 15 | Functions as values, higher-order functions, list problems | [15_functional_programming_basics](15_functional_programming_basics.md) | ✅ |
| 🟧 16 | List comprehensions (simple, filtered, if-else, nested) | [16_list_comprehensions](16_list_comprehensions.md) | ✅ |
| 🟥 17 | Missing number, two-sum, `enumerate`, merge sorted | [17_array_algorithms_and_dictionaries](17_array_algorithms_and_dictionaries.md) | ✅ |
| 🟪 18 | Palindrome, anagram, first unique, longest word | [18_string_algorithms](18_string_algorithms.md) | ✅ |

## ⚡ Quick-Reference Cheat Sheet

| | Level | Key terms |
|:-:|-------|-----------|
| 🟩 | 1 | `np.array` `zeros` `ones` `full` `arange` `linspace` `dtype` `astype` |
| 🟦 | 2 | `+ - * / **` `ndim` `shape` `size` `len` |
| 🟨 | 3 | `a[i]` `a[r,c]` `a[s:e:step]` `a[::-1]` `a[:, c]` |
| 🟧 | 4 | `sqrt` `power` `abs` `round` `floor` `ceil` `trunc` `sum` `mean` `median` `std` `argmax` `axis` |
| 🟥 | 5 | `arr[mask]` `&` `\|` `~` `np.where` |
| 🟪 | 6 | `reshape` `-1` `flatten` 3D arrays |
| 🟩 | 7 | `(3,4) + (3,1)` scalar + array, loop vs vectorized |
| 🟦 | 8 | `np.var` `np.std` `np.percentile` `np.sort` `np.log` `np.exp` `a[1:] - a[:-1]` |
| 🟨 | 9 | `concatenate(axis)` `vstack` `hstack` `column_stack` `reshape(-1,1)` `split` |
| 🟧 | 10 | `random` `rand` `randint` `uniform` `choice(replace=)` `seed` |
| 🟥 | 11 | `np.nan` `np.isnan` `~` `np.nansum` `set_printoptions` |
| 🟪 | 12 | `np.select(conds, choices, default)` `a[:, [0,1,3]]` `np.minimum` view vs copy |
| 🟩 | 13 | derived columns, tiered `np.where`, compound masks, `axis`, `argmax`, capping |
| 🟦 | 14 | slicing, masks, bonus rules, bands, reshape, missing counts |
| 🟨 | 15 | `def`, function as argument, HOF, loop-based list algorithms |
| 🟧 | 16 | `[x for x in L if c]` `[a if c else b for x in L]` nested `for` |
| 🟥 | 17 | sum formula, `dict` lookup, `enumerate`, two pointers |
| 🟪 | 18 | `[::-1]` `isalnum` `replace` `lower` `split` frequency `dict` |

## 📦 Datasets Used

| Dataset | Shape / columns | Used in |
|---------|-----------------|---------|
| Bank `transactions` | 15 values (+ / −) | Level 13 |
| Factory `production` | 4 machines × 6 days | Level 13 |
| `loan_amount`, `interest_rate` | 8 each | Level 13 |
| `employees` | ID, Salary, Experience, Annual_Sales | Levels 5, 13 |
| `points` | 8 × `[x, y]` | Level 13 |
| `patients` | ID, Heart_Rate, Oxygen, Recovery | Level 13 |
| `campaigns` | ID, Impressions, Clicks, Conversions, Cost, Revenue | Level 13 |
| `orders` | ID, Quantity, Price, Rating | Levels 10, 13 |
| `prices` (15 days) | daily stock-like prices | Level 8 |
| Student placement | 30 × 11 numeric table (with `nan`) | Levels 11, 12, 14 |

## 🧰 Setup

```python
import numpy as np   # NumPy = Numerical Python
np.set_printoptions(suppress=True, precision=2)   # optional: plain decimals (used from Level 11)
```

> 💡 Every NumPy code cell in these notes assumes this import. Levels 15–18 use plain Python only.

> ⚠️ **Recurring gotcha:** problem text pasted into a code cell causes `SyntaxError` (`₹`, `→`, `×`). Keep problem statements in text cells or `#` comments.

> ⚠️ **Name shadowing:** never assign to `range`, `sum`, `max` etc. (seen in Level 8); later loops will break.

## 🔜 Still to Come
`lambda`, `filter()` and `reduce()` are listed in the Level 15 outline but were not demonstrated in the source notes.
