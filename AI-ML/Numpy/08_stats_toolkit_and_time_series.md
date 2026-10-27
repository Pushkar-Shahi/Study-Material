<div align="center">

# <span style="color:#2980B9">🟦 Level 8: Stats Toolkit and Time Series</span>
![Level](https://img.shields.io/badge/Level-8-2980B9) ![Theme](https://img.shields.io/badge/Theme-Statistics-27AE60) ![NumPy](https://img.shields.io/badge/NumPy-stats-013243)

</div>

## 📊 1. Spread and Position

| Function | Meaning | Example (`[10 20 30 40 50]`) |
|----------|---------|------------------------------|
| `np.var(a)` | variance | `200.0` |
| `np.std(a)` | standard deviation | `14.1421…` |
| `np.percentile(a, p)` | value below which p% of data falls | `p=75` → `40.0` |
| `np.sort(a)` | ascending copy | `[10 20 30 40 50]` |

> 💡 **variance = std²**. The notebook computes it as `np.square(np.std(a))`, and `np.var` gives the same number.

## 🌡️ 2. Worked Example: Sensor Temperatures (20 readings)

```python
avg_t = np.mean(temperature)      # 35.12
median_t = np.median(temperature) # 35.05
stdt = np.std(temperature)        # 5.4104
var = np.square(stdt)             # 29.2726
```

| Task | Code | Result |
|------|------|--------|
| More than 1 std above mean | `temperature[temperature > avg_t + stdt]` | `[42.3 41.7 44.2 43.1]` |
| Deviation from mean | `deviation = np.abs(temperature - avg_t)` | e.g. `6.62, 3.92, …` |
| Largest 5 deviations | `np.sort(deviation)[-5:]` | `[7.18 7.22 7.98 8.22 9.08]` |
| Round readings | `np.round(temperature)` | `28. 31. 30. 36. …` |
| Label (≥40 Critical, ≥35 Warning, else Normal) | nested `np.where` | 5 Critical |
| % Critical | `c*100/n` | `25.0` |
| 4×5 reshape → row means | `np.mean(new_t, axis=1)` | `[32.64 36.14 36.92 34.78]` |

> ⚠️ **Gotcha:** `np.sort(deviation)[-5:]` returns the five largest **deviations**, not the original **readings**. To get the readings, you need the *positions* of those deviations (e.g. `np.argsort`, not covered in the source).

> ⚠️ **Rounding gotcha:** `np.round` rounds exact halves to the nearest **even** number: `28.5 → 28.`, `30.5 → 30.`, `34.5 → 34.`

## 🧮 3. Percentiles in Practice

| Data | Code | Result |
|------|------|--------|
| Campaign revenue | `np.percentile(revenue, 75)` | `16500.0`; `revenue[revenue > rev75]` → `[18000 24000]` |
| Order prices | `np.percentile(price, 25)` / `75` | `787.5` / `1900.0` |
| Image pixels | `np.percentile(image, 75)` | `100.0`; `image[image > p75]` → empty `[]` |

> 💡 The image result is empty because pixels were **capped at 100** earlier. The 75th percentile already equals the maximum.

## 🔬 4. Log and Exponent

```python
arr = np.array([10, 20, 30, 40, 50])
np.log10(arr)   # [1. 1.30103 1.47712125 1.60205999 1.69897]
np.log(arr)     # natural log [2.30258509 2.99573227 3.40119738 3.68887945 3.91202301]
np.exp(arr)     # e^x, huge values like 2.2e+04 … 5.2e+21 (e ≈ 2.72)
```

## 📈 5. Day-to-Day Change (Time Series)
Shift the array against itself with slices.

```python
prices = np.array([820,835,810,850,875,860,890,910,895,930,945,920,960,975,990])
diff = prices[1:] - prices[:-1]     # [ 15 -25  40  25 -15  30  20 -15  35  15 -25  40  15  15]
abs_move = np.abs(diff)             # size of each movement
pct = np.round(diff*100 / prices[:-1], 2)   # % change vs previous day
```

| Task | Code | Result |
|------|------|--------|
| Largest movement | `np.max(abs_move)` | `40` |
| Days up > 2% | `np.where(pct > 2, "Yes", "No")` | indexes `2 3 5 6 8 11` |
| Those % values | `pct[pct > 2]` | `[4.94 2.94 3.49 2.25 3.91 4.35]` |
| Max / min / range of % | `np.max`, `np.min`, `mx - mn` | `4.94`, `-2.99`, `7.93` |
| 3×5 reshape, row means | `prices.reshape(3,5)` → `np.mean(…, axis=1)` | `[838. 897. 958.]` |

> ⚠️ **Source bug:** "average movement" was computed as `np.mean(diff)` = `12.14`, which averages **signed** changes (ups cancel downs). Use `np.mean(abs_move)` ≈ `23.57`. The largest-movement answer (`40`) happens to be the same either way.

> ⚠️ **Name shadowing:** `range = mx - mn` overwrites Python's built-in `range()`. Use `price_range` instead, or later `for i in range(...)` will fail.

> 💡 A change array is one element **shorter** than the original (14 changes for 15 prices). Index `i` of `diff` means "day i → day i+1".

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `var`, `std` | Measure spread |
| `mean ± std` threshold | Flag unusual values |
| `percentile` | Quartiles and top-N% cut-offs |
| `np.sort` | Order values (returns values, not positions) |
| `log`, `log10`, `exp` | Logarithmic / exponential transforms |
| `a[1:] - a[:-1]` | Consecutive differences |
| Change ÷ previous × 100 | Percentage change |

---
⬅️ [Previous](07_broadcasting.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Joining and Splitting Arrays](09_joining_and_splitting_arrays.md)
