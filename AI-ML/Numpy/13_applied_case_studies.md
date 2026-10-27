<div align="center">

# <span style="color:#27AE60">🟩 Level 13: Applied Case Studies</span>
![Level](https://img.shields.io/badge/Level-13-27AE60) ![Theme](https://img.shields.io/badge/Theme-Real_World-2980B9) ![NumPy](https://img.shields.io/badge/NumPy-analysis-013243)

</div>

## 🧰 1. Pattern Cookbook

| Need | Pattern |
|------|---------|
| Column from 2D table | `col = table[:, k]` (`-1` = last) |
| Derived column | `revenue = qty * price`, `ROI = (rev - cost)*100/cost` |
| Tiered rule | `np.where(a >= x, "A", np.where(a >= y, "B", "C"))` |
| Selective change | `np.where(cond, new_value, old_value)` |
| Compound filter | `table[(c1) & (c2)]` / `\|` |
| "Best row" | `table[np.argmax(col)]` |
| Count / percent | `np.sum(mask)`, `np.sum(mask)*100/len(a)` |
| Row/column stats | `axis=1` per row, `axis=0` per column |
| Cap values | `np.where(a > 100, 100, a)` |

## 🏦 2. Finance

### Bank transactions (+ deposit, − withdrawal)
```python
deposits = transactions[transactions > 0]        # total 95500
withdrawals = transactions[transactions < 0]     # total -48000
net = np.sum(transactions)                       # 47500
abs_t = np.abs(transactions); avg_abs = np.mean(abs_t)   # 9566.67
transactions[abs_t > avg_abs]                    # [ 15000 -12000 25000 -18000 22000]
np.max(transactions), np.min(transactions)       # largest deposit 25000, largest withdrawal -18000
np.where(transactions > 0, "Credit", "Debit")
np.sum(abs_t > 10000) * 100 / len(abs_t)         # 33.33
np.sum(transactions.reshape(3,5), axis=1)        # [20500 0 27000]
```

### Loan portfolio
```python
annual_interest = (loan_amount * interest_rate) / 100   # [8500 23000 44000 75750 9480 33250 94500 39150]
np.sum(annual_interest)      # 327630.0
np.mean(annual_interest)     # 40953.75
np.argmax(annual_interest)   # 6
loan_amount[(loan_amount > 400000) & (interest_rate > 9)]   # [750000 900000]
```

| HW task | Result |
|---------|--------|
| Rate ≥ 10 High, ≥ 9 Medium, else Low | `[Low Medium Low High Low Medium High Low]` |
| Median loan | `400000.0` |
| Above median amount **and** above avg rate (9.15) | `[750000 900000]` |
| Std of rates | `0.8031` |

## 🏭 3. Operations

### Factory production (4 machines × 6 days)
```python
np.sum(production, axis=1)    # by machine [ 816  760 1005  643]
np.sum(production, axis=0)    # by day     [485 520 516 555 580 568]
machine_avg = np.mean(production, axis=1)
production[np.argmax(machine_avg)]      # best machine (index 2)
np.argmin(day_total)                    # lowest day -> 0
production[:, ::2]                      # alternate days
production[[0, 2], -3:]                 # machines 1 and 3, last 3 days
```

> 💡 `production[[0, 2]]` selects **specific rows** by a list of indexes.

> ⚠️ **Source inconsistency:** `overall_avg` (134.33) was computed on the **original** data, but the "High/Normal" labels were applied after the +5% update. For a consistent label, recompute the mean after the update.

### Inventory (4 stores × 5 products)
```python
np.sum(inventory, axis=1)              # [117 115 116 111]  -> store 1 highest
np.sum(inventory, axis=0)              # [ 56 178  41 125  59] -> product 3 lowest
inventory[inventory < 10]              # [8 5 6 9 7]; count = np.sum(inventory < 10) = 5
np.where(inventory < 10, "Reorder", "OK")
new_inv = np.round(np.where(inventory < 10, inventory*1.2, inventory))
np.median(new_inv)                     # 19.0
new_inv[:, -2:]                        # last two products
np.std(new_inv.flatten())              # 15.678
```

### Leads (4 campaigns × 5 channels)
| Task | Code | Result |
|------|------|--------|
| Total per campaign | `np.sum(leads, axis=1)` | `[ 77000 85000 84000 100000]` |
| Total per channel | `np.sum(leads, axis=0)` | `[54000 61000 62000 78000 91000]` |
| Best campaign / channel (1-based) | `np.argmax(...) + 1` | `4` / `5` |
| Average per campaign | `np.mean(leads, axis=1)` | `[15400 17000 16800 20000]` |
| Values above overall avg (17300) | `leads[leads > avg]` | 10 values |
| +10% if < 15000 | `np.where(leads < 15000, leads*1.1, leads)` | selective |
| High/Low vs median | `np.where(leads > np.median(leads), "High", "Low")` | label grid |
| Every second channel | `leads[:, 1::2]` | columns 2 and 4 |

### Delivery locations (`[x, y]`)
```python
x, y = points[:, 0], points[:, 1]
dist = np.sqrt(np.square(x) + np.square(y))   # [ 5. 13. 17. 25. 41. 37. 25. 10.]
avg_dist = np.mean(dist)                      # 21.625
points[dist > avg_dist]                       # [[7 24] [9 40] [12 35] [15 20]]
np.where(dist >= 30, "Long", np.where(dist >= 15, "Medium", "Short"))
```
Long deliveries = `25.0%`; `points.flatten()` has size `16`.

> 💡 The notebook printed the nearest/farthest **distance** (`5.0`, `41.0`). For the **location**, use `points[np.argmin(dist)]` and `points[np.argmax(dist)]`.

## 👥 4. HR and Health

### Employees (ID | Salary | Experience | Annual_Sales)
```python
salary, experience, sales = employees[:,1], employees[:,2], employees[:,3]
sts2 = np.round(sales / salary, 2)        # [10.71 11.08 7.89 10.56 11.09 11.53]
employees[np.argmax(sales)]               # [104 90000 8 950000]
employees[(experience >= 5) & (sales > 600000)]   # IDs 102, 104, 105, 106
bonus = np.where(sales >= 800000, 0.1*sales,
        np.where(sales >= 600000, 0.07*sales, 0.03*sales))   # [13500 50400 9000 95000 42700 83000]
np.sum(bonus)                             # 293600.0
np.mean(salary[sales >= 800000])          # 81000.0
np.median(salary)                         # 60000.0
employees[(salary > median_s) & (experience < 6)]   # empty (0, 4)
```

> ⚠️ Rounding the ratio to **0 decimals first** (`[11 11 8 11 11 12]`) loses detail. Round to 2 decimals directly from `sales / salary`.

### Patients (ID | Heart_Rate | Oxygen | Recovery)
```python
heart_rate, oxy_level, recovery = patients[:,1], patients[:,2], patients[:,3]
np.mean(heart_rate)      # 134.5
np.median(oxy_level)     # 87.5
patients[(heart_rate > avg_hr) & (oxy_level < 90)]   # IDs 104, 106, 108, 110
```

| Task | Result |
|------|--------|
| Recovery ≥97 Excellent, ≥95 Stable, else Monitor | 4 / 3 / 3 |
| Highest heart rate | `np.argmax(heart_rate)` → `5` (patient 106) |
| Std of oxygen | `5.2307`, mean `86.8` |

> ❌ **Source bug:** "oxygen levels more than 1 std **below** the mean" was coded as `oxy_level[oxy_level > (avg_oxy - std)]`, which returns values **above** the threshold. Working version: `oxy_level[oxy_level < avg_oxy - std]` → `[78 80]`.

## 📣 5. Marketing: Campaigns (ID | Impr | Clicks | Conv | Cost | Revenue)

| Metric | Formula | Code |
|--------|---------|------|
| CTR | Clicks ÷ Impressions × 100 | `ctr = clicks*100/impressions` |
| Conversion rate | Conversions ÷ Clicks × 100 | *(defined, not computed in source)* |
| ROI | (Revenue − Cost) ÷ Cost × 100 | `roi = (revenue - cost)*100/cost` |

```python
revenue, cost = campaigns[:, -1], campaigns[:, -2]
campaigns[np.argmax(revenue)]    # campaign 108
campaigns[np.argmax(roi)]        # campaign 108 (ROI 118.18)
np.mean(ctr), np.mean(roi)       # 6.933, 66.618
campaigns[(ctr > avg_ctr) & (roi > avg_roi)]   # campaigns 102, 104, 106, 108
```

HW: `np.where(roi >= 80, "Excellent", np.where(roi >= 40, "Good", "Poor"))` → `[Good Good Good Excellent Poor Excellent Poor Excellent]`; Excellent = `37.5%`.

## 🛒 6. E-commerce: Orders (ID | Quantity | Price | Rating)

```python
revenue = orders[:, 1] * orders[:, 2]
np.sum(revenue), np.mean(revenue), np.median(revenue)   # 73200, 6100.0, 5850.0
orders[np.argmax(revenue)]                              # order 112
new_price = np.where(price > 1000, price*0.9, price)    # 10% off above ₹1000
np.std(price)                                           # 772.80
np.percentile(price, 25), np.percentile(price, 75)      # 787.5, 1900.0
price[price > p75]                                      # [2500 2200 3000]
revenue.reshape(3, 4)  # row means [4050. 6375. 7875.]
```

> ❌ **Source typo:** the tier rule used `revenue >= 150000` while the problem says **15,000**. Working version: `np.where(revenue >= 15000, "High", np.where(revenue >= 7500, "Medium", "Low"))`. Results are unchanged here because the max revenue is 11,250 (no "High").

> ⚠️ **Dataset changed:** the first version had decimal ratings (4.5, 3.8 …) and conditions like `rating >= 4.5`. The later dataset has **integer** ratings (3 or 4), so the conditions became `rating >= 3` (→ `100.0%`) and `rating >= 4`.

> 💡 The generated 20-row dataset in [Level 10](10_random_numbers.md) computes `revenue = quantity * unit_price` and **ignores** its `discount` column.

## 🖼️ 7. Image Processing (6×6 grayscale)

```python
image[1:5, 1:5] = image[1:5, 1:5] * 1.2     # +20% to central 4x4
image = np.where(image > 100, 100, image)   # cap at 100
np.mean(image), np.min(image), np.max(image)   # 73.9167, 10, 100
image[image < np.mean(image)]               # pixels below average
flat = image.flatten(); flat.reshape(6, 6)  # round trip
```

> ⚠️ **Truncation:** `image` is an **int** array, so `35*1.2 = 42.0` stores `42`, but any decimal result would be cut off. Use `dtype=float` first if you need decimals.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| Column slicing | Give each field a name (`salary`, `sales`) |
| Tiered `np.where` | Categories and bonus rules |
| Compound masks | Multi-condition row selection |
| `argmax`/`argmin` + indexing | Retrieve the best/worst full row |
| `axis` stats | Per-row / per-column summaries |
| `np.where(cond, cap, a)` | Clamp or selectively update |

## 📝 Practice (not solved in source)

1. Patients: show the **last 3 patients**, then flatten the measurement data and compute its mean. 
   > 💡 Hint: `patients[-3:]`; `patients.flatten()` then `np.mean` (decide whether to drop the ID column first).
2. Campaigns: compute **conversion rate** per campaign. 
   > 💡 Hint: `conversions*100/clicks`, with `conversions = campaigns[:,3]`.
3. Orders: round the discounted prices to 2 decimals; total revenue of orders with rating ≥ 4 **and** revenue above average. 
   > 💡 Hint: `np.round(new_price, 2)`; `np.sum(revenue[(rating >= 4) & (revenue > avg_revenue)])`.
4. Orders HW: percentage of orders with `rating >= 4.5` (original dataset). 
   > 💡 Hint: `np.sum(rating >= 4.5) * 100 / len(rating)`.

---
⬅️ [Previous](12_select_fancy_indexing_and_views.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Student Placement Case Study](14_student_placement_case_study.md)
