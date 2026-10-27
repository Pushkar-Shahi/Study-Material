<div align="center">

# <span style="color:#E74C3C">🟥 Level 5: Boolean Filtering and np.where</span>
![Level](https://img.shields.io/badge/Level-5-E74C3C) ![Theme](https://img.shields.io/badge/Theme-Conditions-E74C3C) ![NumPy](https://img.shields.io/badge/NumPy-masks-013243)

</div>

## ⚖️ 1. Comparisons Produce Boolean Arrays

| Operator | Meaning |
|:--------:|---------|
| `>` `<` `>=` `<=` | ordering |
| `==` | equal |
| `!=` | not equal |

```python
marks = np.array([70, 80, 65, 90, 75])
marks > 75      # [False  True False  True False]   <- a "mask"
```

## 🔎 2. Boolean Masking (Filtering)

Loop approach vs NumPy:

```python
# loop
b = []
for elem in a:
    if elem > 75: b.append(elem)
```

```python
marks[marks > 75]                            # [80 90]
marks[[False, True, False, True, False]]     # same, with an explicit mask
temperature[temperature >= 32]               # [35 37]
```

## 🔗 3. Combining Conditions

| Logic | Python keyword (❌ fails on arrays) | NumPy operator (✅) |
|-------|-----------------------------------|--------------------|
| AND | `and` | `&` |
| OR | `or` | `\|` |
| NOT | `not` | `~` |

```python
prices = np.array([499, 799, 1299, 2499, 3999, 599])
prices[(prices >= 600) & (prices <= 1000)]   # [799]
prices[(prices < 600) | (prices > 1000)]     # [ 499 1299 2499 3999 599]
prices[~(prices > 900)]                      # [499 799 599]
```

> ❌ `prices[(prices >= 600) and (prices <= 1000)]` → `ValueError: The truth value of an array ... is ambiguous`.

> ⚠️ **Always wrap each condition in parentheses** when using `&`, `|`.

## 🧱 4. Filtering 2D Data

| Goal | Code |
|------|------|
| All cells > 70 | `marks[marks > 70]` → flat 1D result |
| Values > 200 in first row | `sales[0][sales[0] > 200]` → `[300]` |
| Prices of products > ₹1000 | `prices = products[:,1]; prices[prices > 1000]` |
| **Whole rows** by a column test | `employees[employees[:,1] > 50000]` |

```python
employees[employees[:,1] > 50000]
# [[103 62000 6]
#  [105 75000 8]
#  [106 55000 5]]
```

> 💡 To keep full rows, build the mask from **one column**, then index the **whole array** with it.

## 🔀 5. `np.where(condition, value_if_true, value_if_false)`

```python
marks = np.array([45, 72, 88, 31, 65, 90])
np.where(marks > 75, "Good", "Average")
# ['Average' 'Average' 'Good' 'Average' 'Average' 'Good']

np.where(marks < 50, marks + 5, marks)        # grace marks -> [50 72 88 36 65 90]
np.where(prices > 1000, prices*0.9, prices)   # selective 10% discount
```

### 🪜 Nested `where` (multi-category)

```python
np.where(marks >= 90, "Excellent",
         np.where(marks < 50, "Fail", "Pass"))

np.where(sales >= 800000, "Top Performer",
         np.where(sales >= 500000, "Good Performer", "Needs Improvement"))
```

### 🧩 Combined conditions + `where`

| Scenario | Mask | Result |
|----------|------|--------|
| Loan: salary ≥ 50000 **and** score ≥ 700 | `(salary>=50000) & (credit>=700)` | `Approve/Reject` → `[Approve Reject Reject Approve Reject]` |
| Free shipping: order ≥ 1000 **or** premium | `(order>1000) \| (premium==True)` | `[Paid Free Free Paid Free]` |
| Commission 5% if sales ≥ 150000 else 2% | `np.where(sales>=150000, sales*0.05, sales*0.02)` | `[2400. 9000. 1800. 12500. 8000.]` |
| Rating: >200000 Excellent, >150000 Good, else Needs Improvement | nested `where` | `[NI Good NI Excellent Good]` |

### 🎓 Student classification (ID column excluded)

```python
students = np.array([[101,78,85,92],[102,45,55,60],[103,91,88,95],[104,62,70,68],[105,35,42,50]])
avg_m = np.mean(students[:, 1:], axis=1)      # skip the ID column!
np.where(avg_m >= 85, "Excellent",
  np.where(avg_m >= 60, "Good",
    np.where(avg_m >= 50, "Pass", "Fail")))
# ['Excellent' 'Pass' 'Excellent' 'Good' 'Fail']
```

Using row masks with stats: `std_avg = np.mean(marks, axis=1)`; `marks[std_avg > 75]` returns the rows of students above 75 average; `marks[np.argmax(std_avg)]` returns the top student's row.

> ⚠️ **Gotcha:** `np.mean(students, axis=1)` would include the ID (101…) and give wrong averages. Slice `[:, 1:]` first.

> ❌ **Source inconsistencies (flagged):**
> - Comment says `marks > 70 → "Good"` but the code uses `> 75`. Working version: `> 75`.
> - Free-shipping text says "order value >= ₹1,000" but the code uses `> 1000`. For the sample data both give the same result; use `>=` to match the rule.
> - Category text "Sales ≥ 150000 → good" but code uses `> 150000`; same sample output.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `arr > x` | Create boolean mask |
| `arr[mask]` | Keep only matching items |
| `&`, `\|`, `~` | AND / OR / NOT on masks |
| `np.where(c, a, b)` | Choose per element (labels or values) |
| Nested `where` | Multiple categories |
| `arr[arr[:,k] > v]` | Filter whole rows by a column |

## 📝 Practice (only the first item was solved in source)

`employees = [[101,35000,2],[102,48000,4],[103,62000,6],[104,40000,3],[105,75000,8],[106,55000,5]]` (ID | Salary | Experience)

1. Employees with more than 4 years of experience. 
   > 💡 Hint: `employees[employees[:,2] > 4]`
2. Salary > 50000 **and** experience > 4. 
   > 💡 Hint: combine masks with `&`, wrapped in parentheses.
3. Average salary of the group from item 2. 
   > 💡 Hint: `np.mean(result[:,1])`
4. Employee with the highest salary. 
   > 💡 Hint: `employees[np.argmax(employees[:,1])]`
5. Employees below the median salary. 
   > 💡 Hint: `employees[employees[:,1] < np.median(employees[:,1])]`

---
⬅️ [Previous](04_math_and_statistics.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Reshape and Flatten](06_reshape_and_flatten.md)
