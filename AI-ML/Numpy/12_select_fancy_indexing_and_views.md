<div align="center">

# <span style="color:#8E44AD">🟪 Level 12: np.select, Fancy Indexing and Views</span>
![Level](https://img.shields.io/badge/Level-12-8E44AD) ![Theme](https://img.shields.io/badge/Theme-Selection-F1C40F) ![NumPy](https://img.shields.io/badge/NumPy-select-013243)

</div>

## 🎛️ 1. `np.select`: many conditions, many choices

`np.select(conditions, choices, default=...)` picks the choice of the **first** true condition.

```python
conditions = [
    np.isnan(attendance),     # 1st: missing
    attendance >= 85,         # 2nd: high
    attendance >= 70          # 3rd: moderate
]
choices = ["Unknown", "High", "Moderate"]
attendance_category = np.select(conditions, choices, default="Low")
# ['High' 'Moderate' 'Low' 'High' 'Unknown' 'Moderate' 'High' ...]
```

| Rule | Category |
|------|----------|
| attendance missing | `Unknown` |
| ≥ 85 | `High` |
| 70 to below 85 | `Moderate` |
| below 70 (nothing matched) | `Low` (the `default`) |

### 🆚 vs nested `np.where`

| | Nested `np.where` | `np.select` |
|--|-------------------|-------------|
| Style | tiers inside tiers | flat lists of conditions and choices |
| Good for | 2–3 tiers | many tiers |
| Example in source | study bands | attendance categories |

```python
study_band = np.where(study_hours < 2, "Low",
             np.where(study_hours <= 4, "Medium", "High"))   # <2 Low, 2-4 Medium, >4 High
```

> ⚠️ **Order matters:** the `nan` test is first. A comparison with `nan` is always `False`, so without the first test a missing value would fall through to the `Low` default.

## 🎯 2. Fancy Indexing: pick specific rows/columns by list

```python
marks[:10, [0, 1, 3]]    # first 10 students; only Python, SQL, NumPy columns
marks[[0, 2]]            # rows 0 and 2 (see [Level 13](13_applied_case_studies.md))
```

| Syntax | Selects |
|--------|---------|
| `a[:, 1:4]` | a **range** of columns (slice) |
| `a[:, [0, 1, 3]]` | **specific** columns, in the order given |

## 🧢 3. Capping with `np.minimum`

```python
python_marks[eligible] = np.minimum(python_marks[eligible] + 5, 100)
```

| Piece | Role |
|-------|------|
| `python_marks[eligible]` | only eligible students |
| `+ 5` | bonus |
| `np.minimum(…, 100)` | element-wise smaller of value and 100, so no mark exceeds 100 |

Example: `96 + 5 = 101` becomes `100`.

## 🪟 4. Views: a slice is not a copy

```python
python_marks = marks[:, 0]          # a VIEW of column 0
python_marks[eligible] = ...        # also changes marks!
```

Evidence in the source: after the bonus step, the first 15 Python marks read from `marks` became `[93 75 55 97 45 | 70 85 60 100 68 | 80 40 95 72 58]` (88→93, 92→97, 96→100 capped, 90→95).

> ⚠️ **Gotcha:** modifying a slice assigned to a new name changes the original array. This was intended here ("award a bonus"), but surprising if you wanted to keep the originals.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `np.select` | Multi-way labels with a `default` |
| `a[:, [i, j]]` | Pick non-contiguous columns |
| `np.minimum(x, cap)` | Cap values from above |
| View vs copy | Slices share memory with the original |

---
⬅️ [Previous](11_missing_values_and_nan.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Applied Case Studies](13_applied_case_studies.md)
