<div align="center">

# <span style="color:#2E8B57">🟢 Level 1 — Foundational Concepts</span>

![Level](https://img.shields.io/badge/Level-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Grounding_the_Basics-2E8B57)

</div>

---

## 🧠 Core Concepts

| Concept | Meaning | Example |
|---|---|---|
| 📊 **Data** | Collection of facts | `Rahul Sharma`, `$115,000`, `Nagpur` |
| 🗄️ **Database** | Organized collection of data | Customer records, order history |
| ⚙️ **DBMS** | Software that manages the database | MySQL, PostgreSQL |
| ☁️ **BigQuery** | Google's cloud-based data warehouse | Query via SQL, no server setup |
| 📑 **Table & Columns** | Data organized in rows/columns | `customer_id` uniquely IDs a row |
| 🗣️ **SQL** | Structured Query Language — how we "talk" to the database | — |

---

## 🌍 Real-World Tie-In

> Companies like **Amazon**, **Swiggy**, and **Netflix** run their entire operations on data structured exactly like this.

---

## 🔍 No-Code Peek

BigQuery lets you view table data without writing a single line of SQL — just use the **"Preview"** tab in the console.

---

### 🛠️ MLOps Perspective: The Database
> [!NOTE]
> In MLOps, BigQuery isn't just a storage location — it's the **Source of Truth**.
> When training models, you will connect directly to these Data Warehouses using libraries like `google-cloud-bigquery`. Understanding how data is partitioned and clustered at the foundational level determines how fast and cheaply you can extract your training datasets.

```mermaid
graph LR
    DB[(BigQuery Database)] -->|SQL Query| Extraction[Data Extraction]
    Extraction --> Pandas[(Pandas DataFrame)]
    Pandas --> Training[Model Training]
```

---

<div align="center">

⬅️ [Back to Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 2 — Basic Queries](./02_basic_queries.md)

</div>
