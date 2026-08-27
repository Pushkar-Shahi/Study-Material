<div align="center">

# <span style="color:#E07B00">🟠 Level 4 — Data Summarization (Aggregations)</span>

![Level](https://img.shields.io/badge/Level-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Rows_to_Insight-E07B00)

</div>

---

## 🧮 Aggregate Functions

| Function | What it Does | Example Use |
|---|---|---|
| `COUNT()` | Counts rows | Total number of products |
| `SUM()` | Adds values | Total sales value |
| `AVG()` | Averages values | Average selling price |
| `MIN()` | Smallest value | Minimum payment amount |
| `MAX()` | Largest value | Maximum payment amount |

---

## 🗃️ `GROUP BY` — Break Totals Into Categories

```sql
SELECT CategoryID, COUNT(*) AS total_products
FROM e1.products
GROUP BY CategoryID
```

| Grouping Style | Example |
|---|---|
| By category | `GROUP BY CategoryID` |
| By product | `GROUP BY ProductID` |
| By multiple columns | `GROUP BY CustomerID, Status` |

---

## 📊 Full Example — Product Sales Summary

```sql
SELECT
  ProductID,
  COUNT(*)              AS total_orders,
  SUM(total)             AS total_sales,
  MAX(total)              AS max_sale,
  MIN(total)              AS min_sale,
  ROUND(AVG(total), 2)    AS avg_sale
FROM `e1.order_items`
GROUP BY ProductID
```

> [!NOTE]
> **One query → full statistical snapshot per product.**

---

## 📝 Summary Table

| Keyword | Purpose |
|---|---|
| `COUNT/SUM/AVG/MIN/MAX` | Summarize a column into a single value |
| `GROUP BY` | Apply that summary per category instead of the whole table |

---

### 🛠️ MLOps Perspective: Feature Engineering
> [!IMPORTANT]
> Aggregations are the backbone of **Feature Engineering**.
> When predicting customer churn, the model needs features like `total_orders`, `avg_sale_value`, and `days_since_last_purchase`. You will write massive `GROUP BY customer_id` queries to roll up raw transactional rows into a single vector of features for each customer!

---

<div align="center">

⬅️ [Previous: Level 3 — Filtering & Sorting](./03_filtering_sorting.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 5 — Advanced Logic](./05_advanced_logic.md)

</div>
