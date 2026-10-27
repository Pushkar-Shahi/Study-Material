<div align="center">

# <span style="color:#2980B9">🟦 Level 14: Student Placement Case Study</span>
![Level](https://img.shields.io/badge/Level-14-2980B9) ![Theme](https://img.shields.io/badge/Theme-Case_Study-E67E22) ![NumPy](https://img.shields.io/badge/NumPy-30x11-013243)

</div>

## 📋 1. Dataset (30 students, 11 numeric columns)

| Col | Field | Col | Field |
|:---:|-------|:---:|-------|
| 0 | Student_ID | 6 | Statistics |
| 1 | Attendance % | 7 | NumPy |
| 2 | Study_Hours | 8 | Communication |
| 3 | Internet_Hours | 9 | Mock_Interview |
| 4 | Python | 10 | Placement (1 = placed, 0 = not) |
| 5 | SQL | | |

> 💡 `np.column_stack((ids, attendance, study, internet, marks[5 cols], mock, placement))` = 1+1+1+1+5+1+1 = **11** columns. Marks alone (`marks`) is a separate `(30, 5)` array.

Setup: `attendance[[4,11]]`, `marks[2,2]`, `marks[14,1]`, `mock_interview[18]` are set to `np.nan` for practice.

## 🔍 2. Dataset Overview

```python
numeric_data.ndim     # 2
numeric_data.shape    # (30, 11)
numeric_data.size     # 330
numeric_data.dtype    # float64
numeric_data[:5]      # first five student records
```

## ✂️ 3. Slicing Questions (rows are students; ID 1004 = row 3)

| Task | Code | Result |
|------|------|--------|
| First 5 students, first 3 subjects | `marks[:5, :3]` | 5×3 block (contains one `nan`) |
| All marks of student 1004 | `marks[3, :]` or `marks[3]` | `[92. 88. 90. 94. 86.]` |
| 1004's first three subjects | `marks[3, :3]` | `[92. 88. 90.]` |
| Last two subjects of first 5 | `marks[:5, -2:]` | 5×2 block |
| Python, SQL, NumPy of first 10 | `marks[:10, [0, 1, 3]]` | 10×3 |

## 🧮 4. Totals and Percentages (missing ≠ zero)

```python
total_marks    = np.nansum(marks, axis=1)
valid_subjects = np.sum(~np.isnan(marks), axis=1)       # 4 for rows 2 and 14, else 5
percentage     = (total_marks / (valid_subjects * 100)) * 100
```

Examples: row 0 → `85.8`, row 2 → `58.75`, row 14 → `59.5`.

## 🎁 5. Bonus and Categories

| Requirement | Code |
|-------------|------|
| +5 Python marks if attendance ≥ 90 (missing → no bonus), capped at 100 | `eligible = (~np.isnan(attendance)) & (attendance >= 90)`<br>`python_marks[eligible] = np.minimum(python_marks[eligible] + 5, 100)` |
| Attendance: High ≥85, Moderate 70–<85, Low <70, Unknown missing | `np.select([isnan, >=85, >=70], ["Unknown","High","Moderate"], default="Low")` |
| Study bands: <2 Low, 2–4 Medium, >4 High | `np.where(study < 2, "Low", np.where(study <= 4, "Medium", "High"))` |

> ⚠️ `python_marks = marks[:, 0]` is a **view**, so the bonus also updates `marks` (see [Level 12](12_select_fancy_indexing_and_views.md)).

## 🔄 6. Reshape

```python
python_first_15 = marks[:15, 0]
python_first_15.reshape(3, 5)     # shape (3, 5)
```

## 🕳️ 7. Missing-Value Report

```python
np.isnan(attendance).sum()           # missing attendance
np.isnan(marks).sum(axis=0)          # missing marks per subject
np.isnan(mock_interview).sum()       # missing mock scores
np.isnan(marks).sum(axis=1)          # missing per student
```

> ❌ **Source issues (flagged):**
> - The "Write a program to determine the number of students…" text was pasted into a code cell → `SyntaxError`.
> - The missing-value cells have no captured output (see [Level 11](11_missing_values_and_nan.md) Practice for the expected counts).

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `column_stack` | Build one 2D table from fields |
| Slice + fancy index | Retrieve students/subjects |
| `nansum` + valid count | Fair totals with missing data |
| `np.select` / `np.where` | Category columns |
| `np.minimum` cap | Keep marks ≤ 100 |
| `isnan().sum(axis)` | Data-quality report |

## 📝 Practice

The source stops after the data-quality report. Extension ideas using only tools above:

1. Compare average mock-interview score of placed (`placement == 1`) vs not placed students. 
   > 💡 Hint: `mock_interview[placement == 1]` and `[placement == 0]`, then a mean that skips `nan` values (e.g. filter with `~np.isnan`).
2. Percentage of students with attendance **Low**. 
   > 💡 Hint: `np.sum(attendance_category == "Low") * 100 / 30`.

---
⬅️ [Previous](13_applied_case_studies.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Functional Programming Basics](15_functional_programming_basics.md)
