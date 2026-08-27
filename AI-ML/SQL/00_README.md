<div align="center">

# 🗺️ SQL Learning Roadmap
### *From Zero to Aggregations & Subqueries — BigQuery Edition*

![Progress](https://img.shields.io/badge/Levels_Covered-5-blue) ![Status](https://img.shields.io/badge/Status-In_Progress-yellow) ![Platform](https://img.shields.io/badge/Platform-Google_BigQuery-4285F4?logo=googlebigquery&logoColor=white)

</div>

---

## 📍 Progress Map

| # | Level | Focus | File | Status |
|---|-------|-------|------|:---:|
| 1️⃣ | 🟢 **Fundamentals** | Data, Databases, BigQuery | [`01_fundamentals.md`](./01_fundamentals.md) | ✅ |
| 2️⃣ | 🔵 **Basic Queries** | SELECT, DISTINCT, LIMIT | [`02_basic_queries.md`](./02_basic_queries.md) | ✅ |
| 3️⃣ | 🟡 **Organizing Data** | WHERE, ORDER BY | [`03_filtering_sorting.md`](./03_filtering_sorting.md) | ✅ |
| 4️⃣ | 🟠 **Analyzing Data** | Aggregations, GROUP BY | [`04_aggregations.md`](./04_aggregations.md) | ✅ |
| 5️⃣ | 🔴 **Advanced Logic** | HAVING, Subqueries | [`05_advanced_logic.md`](./05_advanced_logic.md) | ✅ |
| 6️⃣ | 🔜 **JOINs & Beyond** | Not yet covered | — | ⏳ |

---

## 📖 Quick-Reference Cheat Sheet

| Color | Level | Keywords |
|:---:|---|---|
| 🟢 | Fundamentals | *(conceptual — no syntax)* |
| 🔵 | Basic Queries | `SELECT`, `DISTINCT`, `LIMIT` |
| 🟡 | Filtering & Sorting | `WHERE`, `ORDER BY`, `ASC`, `DESC` |
| 🟠 | Aggregations | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP BY` |
| 🔴 | Advanced Logic | `HAVING`, Subqueries, `IN` |

---

### 🛠️ MLOps Perspective: Why SQL Matters
> [!IMPORTANT]
> As an aspiring MLOps Engineer, SQL is just as important as Python. Your machine learning models are only as good as the data they are trained on, and that data lives in Data Warehouses like BigQuery.
> - **Feature Stores:** The queries you write will eventually become automated pipelines (using tools like `dbt` or Airflow) that feed into Feature Stores.
> - **Compute Pushdown:** Moving data to Python is slow. Pushing computations (like aggregations) down to the SQL engine saves massive amounts of time and memory in MLOps pipelines.

---

<div align="center">

### 🔜 Coming Next: **Level 6 — JOINs** *(not yet covered in source material)*
*INNER JOIN • LEFT JOIN • RIGHT JOIN • FULL JOIN*

</div>
