<div align="center">

# <span style="color:#C0392B">🔴 Level 5 — Advanced Logic: HAVING & Subqueries</span>

![Level](https://img.shields.io/badge/Level-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Deep_Analytical_Power-C0392B)

</div>

---

## ⚖️ `HAVING` — Filter *After* Aggregation

| `WHERE` | `HAVING` |
|---|---|
| Filters individual rows **before** grouping | Filters groups **after** aggregation |
| ❌ Can't use `COUNT()`, `SUM()`, etc. | ✅ Built for aggregate conditions |

```sql
-- Suppliers with at least 3 products
SELECT SupplierID, COUNT(*) AS no_of_products
FROM e1.products
GROUP BY SupplierID
HAVING no_of_products >= 3

-- WHERE + GROUP BY + HAVING together
SELECT method, SUM(amount) AS total_volume
FROM e1.payments
WHERE Status = "Success"
GROUP BY method
HAVING total_volume > 100000
```

---

## 📦 Subqueries — Queries Inside Queries

### 1️⃣ Dynamic Comparison
```sql
SELECT * FROM e1.products
WHERE MRP > (SELECT AVG(MRP) FROM e1.products)
```

### 2️⃣ `IN` Operator with a Subquery
```sql
SELECT * FROM e1.products
WHERE SupplierID IN (
  SELECT SupplierID FROM e1.products
  GROUP BY SupplierID
  HAVING COUNT(*) >= 5
)
```

### 3️⃣ Subquery as a Table (in `FROM`)
```sql
SELECT AVG(product_count) AS avg_products_per_supplier
FROM (
  SELECT SupplierID, COUNT(*) AS product_count
  FROM e1.products
  GROUP BY SupplierID
)
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `HAVING` | Filter grouped/aggregated results |
| Subquery (in `WHERE`) | Compare against a dynamically calculated value |
| Subquery (with `IN`) | Filter against a generated list of values |
| Subquery (in `FROM`) | Treat query results as a temporary table |

> [!TIP]
> **Unlocks:** most active customers, unusual pricing, top-tier suppliers, and more.

---

### 🛠️ MLOps Perspective: Advanced Data Pipelines
> [!IMPORTANT]
> Subqueries are heavily used in creating complex features and `dbt` (data build tool) pipelines, which are core to MLOps. In production, you often need to stack subqueries or CTEs (Common Table Expressions) to clean data, compute aggregations, and join them together before feeding the final dataset to a model training container.

---

<div align="center">

⬅️ [Previous: Level 4 — Aggregations](./04_aggregations.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🔜 Coming Next: **Level 6 — JOINs** *(not yet covered in source material)*

</div>
