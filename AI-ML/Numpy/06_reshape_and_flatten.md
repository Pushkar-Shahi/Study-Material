<div align="center">

# <span style="color:#8E44AD">🟪 Level 6: Reshape and Flatten</span>
![Level](https://img.shields.io/badge/Level-6-8E44AD) ![Theme](https://img.shields.io/badge/Theme-Restructure-8E44AD) ![NumPy](https://img.shields.io/badge/NumPy-reshape-013243)

</div>

## 🔄 1. `reshape(rows, cols)`
Rearranges the same elements into a new shape. Total size must stay equal.

```python
sales = np.array([120,150,180,200,220,250,270,300,320,350,380,400])   # (12,)
qtr_sales = sales.reshape(4, 3)       # 4 quarters x 3 months
# [[120 150 180]
#  [200 220 250]
#  [270 300 320]
#  [350 380 400]]
np.array([1,2,3,4,5,6]).reshape(2, 3)   # OK
```

> ❌ `np.array([1,2,3,4,5,6]).reshape(3,3)` → `ValueError: cannot reshape array of size 6 into shape (3,3)` (6 ≠ 9).

| Rule | Detail |
|------|--------|
| Size must match | `rows × cols == size` |
| Original unchanged | `reshape` returns a new view/array; `sales` stays `(12,)` |

## ➖ 2. The `-1` Placeholder
Let NumPy compute one dimension.

```python
marks.shape                # (20,)
marks.reshape(5, -1)       # (5, 4)
n_m.reshape(-1, 2)         # (10, 2)
n_m.reshape(-1, 3)         # ValueError: 20 is not divisible by 3
```

> 💡 Only **one** `-1` is allowed, and the other number must divide the size evenly.

## 📉 3. `flatten()` (2D → 1D)

```python
matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
a = matrix.flatten()
matrix.shape   # (3, 3)  unchanged
a.shape        # (9,)
```

Overall average of a 2D table, two equal ways:

```python
np.mean(sales)                 # 152.222...
np.mean(sales.flatten())       # 152.222...
np.mean(sales, axis=1)         # per row
np.mean(sales, axis=0)         # per column
```

## 🧊 4. 3D Arrays

```python
a = np.arange(30)
b = a.reshape(2, 5, 3)     # 2 blocks, each 5 rows x 3 cols
b[0]       # first 5x3 block
b[0, 1]    # [3 4 5]
```

## 🧩 5. Mixed Case Studies (all earlier levels together)

| Task | Code | Output |
|------|------|--------|
| Row sums of reshaped 4×5 marks | `np.sum(marks.reshape(4,5), axis=1)` | `[385 405 391 407]` |
| Revenue per product | `rev = quantity * price` | total `60550`, top index `4` |
| Revenue above average | `rev[rev > np.mean(rev)]` | `[8800 5400 7000 6500 7500]` |
| 10% off if price > 1000 | `np.where(price>1000, 0.9*price, price)` | selective discount |
| Price above median **and** qty ≥ 5 | `(price > med_p) & (quantity >= 5)` | price `[1300]` |
| 24 scores → 6 students × 4 tests | `scores.reshape(6,4)` | per-student mean `[77. 81.25 73. 81. 84.75 76.75]` |
| Best student index | `np.argmax(avg_st)` | `4` |
| % of scores above 80 | `len(scores[scores>80]) * 100 / len(scores)` | `45.83` |
| Last two tests per student | `new_s[:, -2:]` | 6×2 |
| 12-month sales: mean / median / std | `np.mean`, `np.median`, `np.std` | `170416.67`, `168500`, `32392.02` |

### 📈 Forecast pipeline

```python
mn_s, mx_s20 = np.min(sales), np.max(sales) * 1.2          # 120000 .. 270000
forecast = np.linspace(mn_s, mx_s20, 6)                    # 6 evenly spaced values
n_s = np.append(sales, forecast)                           # join: 12 + 6 = 18 values
ans = n_s.reshape(3, 6)
np.mean(ans, axis=1)                                       # [144166.67 196666.67 195000.]
np.where(n_s > np.median(n_s), "Yes", "No")
```

> 💡 `np.append(a, b)` joins two 1D arrays into one longer array (used here without a separate lesson).

> ❌ **Source inconsistency:** the task says "round to the **nearest rupee**" but the code used `np.round(forecast, 2)` (2 decimals). Working version: `np.round(forecast)` (no second argument). The values happen to be whole numbers so the output is unchanged.

> ⚠️ **Source observation:** the performance-label `np.where` on student averages returned `'Good'` for all six students, which is correct, since every average lies in 70–85.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `reshape(r, c)` | Change layout, same data |
| `reshape(-1, c)` | Auto-compute one dimension |
| `flatten()` | Collapse to 1D |
| `reshape(a, b, c)` | Build 3D arrays |
| Reshape + `axis` | Group flat data (e.g. quarters) and aggregate |

## 📝 Practice (HW, no solution in source)

Factory temperatures (20 readings):

```python
temperature = np.array([28.5,31.2,29.8,35.6,38.1,40.2,27.9,30.5,42.3,39.8,
                        36.4,33.2,29.1,41.7,44.2,31.8,34.5,37.6,26.9,43.1])
```

1. Mean, median, min, max. 
   > 💡 Hint: `np.mean/median/min/max`
2. Variance and standard deviation. 
   > 💡 Hint: `np.std`; variance is the square of the standard deviation.
3. Readings more than one std above the mean. 
   > 💡 Hint: `temperature[temperature > mean + std]`
4. Absolute difference from the mean. 
   > 💡 Hint: `np.abs(temperature - mean)`
5. Five readings with the largest deviation. 
   > 💡 Hint: build the deviation array, then repeatedly use `np.argmax`, or sort the deviations with `np.sort` ([Level 8](08_stats_toolkit_and_time_series.md); it returns values, not positions).
6. Round all readings to whole numbers. 
   > 💡 Hint: `np.round(temperature)`

<span style="color:gray">*Next up: [Level 7: Broadcasting](07_broadcasting.md), sorting and stats in [Level 8](08_stats_toolkit_and_time_series.md), joining/stacking in [Level 9](09_joining_and_splitting_arrays.md).*</span>

---
⬅️ [Previous](05_boolean_filtering_and_where.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Broadcasting](07_broadcasting.md)
