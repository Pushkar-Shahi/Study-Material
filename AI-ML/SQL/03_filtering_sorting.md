<div align="center">

# <span style="color:#D4A017">🟡 Level 3 — Filtering & Sorting</span>

![Level](https://img.shields.io/badge/Level-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Refining_the_View-D4A017)

</div>

---

## 🔬 `WHERE` — Filter Rows

```sql
SELECT * FROM e1.products WHERE MRP > 500
SELECT * FROM e1.products WHERE SellingPrice < MRP
SELECT * FROM e1.payments WHERE Status = "Success"
```

| Filter Type | Example |
|---|---|
| Numeric | `WHERE MRP > 500` |
| Comparison between columns | `WHERE SellingPrice < MRP` |
| Text / status | `WHERE Status = "Success"` |
| Calculated condition | Discount % > 10% |

---

## 🔼 `ORDER BY` — Sort Results

```sql
SELECT * FROM e1.products ORDER BY ProductName ASC     -- A->Z / low->high
SELECT * FROM e1.products ORDER BY SellingPrice DESC    -- expensive first
SELECT * FROM e1.customers ORDER BY City ASC, Age DESC  -- multi-level sort
```

| Clause | Direction | Behavior |
|---|:---:|---|
| `ASC` | 🔼 | Default — low->high / A->Z |
| `DESC` | 🔽 | Reverse — high->low / Z->A |

> [!TIP]
> You can sort by **multiple columns** — e.g., city alphabetically, then age within each city.

---

## 📝 Summary Table

| Keyword | Purpose |
|---|---|
| `WHERE` | Filter individual rows before results are returned |
| `ORDER BY` | Sort the final result set |
| `ASC` / `DESC` | Control sort direction |

---

### 🛠️ MLOps Perspective: Time-Based Splits
> [!IMPORTANT]
> The `WHERE` clause is critical for **preventing data leakage** in Machine Learning.
> When constructing a dataset, you must split your data temporally (e.g., train on data before 2023, test on 2023 data). You will heavily rely on `WHERE date_column < '2023-01-01'` to guarantee that no future data leaks into your model's training set.

---

<div align="center">

⬅️ [Previous: Level 2 — Basic Queries](./02_basic_queries.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 4 — Aggregations](./04_aggregations.md)

</div>
