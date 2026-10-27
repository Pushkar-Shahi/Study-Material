<div align="center">

# <span style="color:#E74C3C">🟥 Level 11: Missing Values and NaN</span>
![Level](https://img.shields.io/badge/Level-11-E74C3C) ![Theme](https://img.shields.io/badge/Theme-NaN-2980B9) ![NumPy](https://img.shields.io/badge/NumPy-isnan-013243)

</div>

## ❓ 1. Creating Missing Values

```python
attendance = np.array([95, 82, 68, 91, 55, ...], dtype=float)   # float array
attendance[[4, 11]] = np.nan      # two missing entries (list of indexes)
marks[2, 2] = np.nan              # one cell
marks[14, 1] = np.nan
mock_interview[18] = np.nan
```

| Point | Detail |
|-------|--------|
| Symbol | `np.nan` ("not a number") |
| Arrays use `dtype=float` | the notebook builds every numeric array as float before inserting `nan` |
| Display | `np.set_printoptions(suppress=True, precision=2)` shows plain decimals, 2 places |

> ⚠️ Joined with `column_stack`, one `float` column makes the **whole** `numeric_data` array `float64`, so IDs and placement display as `1001.` and `1.`.

## 🔎 2. Detecting NaN

```python
np.isnan(attendance)               # boolean mask, True where missing
np.isnan(attendance).sum()         # how many missing
np.isnan(marks).sum(axis=0)        # missing per subject (column)
np.isnan(marks).sum(axis=1)        # missing per student (row)
~np.isnan(marks)                   # NOT missing (valid)
```

| Expression | Meaning |
|------------|---------|
| `np.isnan(a)` | `True` where value is `nan` |
| `~np.isnan(a)` | `True` where value is a real number |
| `.sum()` on booleans | counts the `True` values |

## ➕ 3. Sums with NaN

| Call | Result on a row containing `nan` |
|------|----------------------------------|
| `np.sum(marks, axis=1)` | **`nan`** (rows 2 and 14 become `nan`) |
| `np.nansum(marks, axis=1)` | adds only valid values; `nan` treated as nothing, not as an error |

```python
total_marks = np.nansum(marks, axis=1)          # row 2 -> 235, row 14 -> 238
valid_subjects = np.sum(~np.isnan(marks), axis=1)   # [5 5 4 5 ... 4 ...]
percentage = (total_marks / (valid_subjects * 100)) * 100
# row 2: 235/(4*100)*100 = 58.75   row 14: 59.5   row 0: 85.8
```

> ⚠️ **Don't treat missing as zero.** Dividing by 500 for a student with a missing mark would punish them. The notebook divides by `valid_subjects * 100` (4 subjects → 400).

## ✅ 4. Safe Conditions with NaN

```python
eligible = (~np.isnan(attendance)) & (attendance >= 90)
```

> 💡 A comparison with `nan` is never true (`nan >= 90` is `False`), but the explicit `~np.isnan(...)` guard states the intent. The assignment says: "If attendance is missing, do not award a bonus automatically."

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `np.nan` | Mark missing data |
| `np.isnan` / `~np.isnan` | Find missing / valid values |
| `.sum()` on mask | Count missing values |
| `np.sum` vs `np.nansum` | `nan` spreads vs missing skipped |
| `valid_count` denominator | Fair averages/percentages |

## 📝 Practice (cell had no output in source)

Count missing values in attendance, in each subject, in mock interview, and per student. 
> 💡 Hint: by construction of the dataset you should get `2` for attendance, `[0 1 1 0 0]` per subject (SQL, Statistics), `1` for mock interview, and a `1` for students at rows 2 and 14.

---
⬅️ [Previous](10_random_numbers.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: np.select, Fancy Indexing and Views](12_select_fancy_indexing_and_views.md)
