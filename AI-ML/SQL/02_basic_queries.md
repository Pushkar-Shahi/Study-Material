<div align="center">

# <span style="color:#1E6FEB">🔵 Level 2 — Basic Querying & Data Selection</span>

![Level](https://img.shields.io/badge/Level-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_First_Contact_with_Data-1E6FEB)

</div>

---

## 🎯 `SELECT` — Choose Your Data

```sql
SELECT * FROM e1.customers            -- everything
SELECT Name, City FROM e1.customers   -- specific columns
```

| Mode | Syntax | Use Case |
|---|---|---|
| Select All | `SELECT *` | Quick full view of a table |
| Select Specific | `SELECT col1, col2` | Only pull what you need |

---

## 🛑 `LIMIT` — Restrict Results

```sql
SELECT * FROM e1.customers LIMIT 10   -- just the top 10 rows
```

> [!TIP]
> Handy for previewing large tables without pulling thousands of rows.

---

## 💎 `DISTINCT` — Unique Values Only

```sql
SELECT DISTINCT City FROM e1.customers                  -- unique cities
SELECT DISTINCT method, status FROM e1.payments          -- unique pairs
```

| Type | Example | Result |
|---|---|---|
| Single column | `DISTINCT City` | Each city listed once |
| Multiple columns | `DISTINCT method, status` | Every unique combination |

---

## 📝 Summary Table

| Keyword | Purpose |
|---|---|
| `SELECT` | Pull data from a table |
| `LIMIT` | Cap the number of rows returned |
| `DISTINCT` | Remove duplicate values |

---

### 🛠️ MLOps Perspective: Data Loading
> [!WARNING]
> **Never use `SELECT *` in an automated ML Pipeline!**
> When building pipelines, schemas can evolve (new columns get added). `SELECT *` will break your downstream pandas code. Always `SELECT` explicit columns so your ML models get exactly the features they expect.
>
> Also, use `LIMIT` heavily during Exploratory Data Analysis (EDA) in Jupyter Notebooks to avoid crashing your kernel when querying massive BigQuery tables!

---

<div align="center">

⬅️ [Previous: Level 1 — Fundamentals](./01_fundamentals.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 3 — Filtering & Sorting](./03_filtering_sorting.md)

</div>
