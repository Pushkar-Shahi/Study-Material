<div align="center">

# 🔗 SQL Joins & Reporting Practice
### *AI & Machine Learning by Aditya Jain Sir — Lectures 38–40 (Earnest)*

![Progress](https://img.shields.io/badge/Sections-5-blue) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen) ![Platform](https://img.shields.io/badge/Platform-Google_BigQuery-4285F4?logo=googlebigquery&logoColor=white)

</div>

---

## 📊 Table of Contents

| # | Section | Focus |
|---|-------|-------|
| 1️⃣ | 🟩 [Basic Sales Joins](#-section-1--basic-sales-joins) | Product/Category/Supplier sales via INNER JOIN |
| 2️⃣ | 🟦 [Finding Missing Relationships](#-section-2--finding-missing-relationships) | LEFT/RIGHT JOIN — no-sale products & never-ordered customers |
| 3️⃣ | 🟨 [Multi-Table Customer Reports](#-section-3--multi-table-customer-reports) | Orders + successful payments, HAVING filters |
| 4️⃣ | 🟧 [Multi-Table Product Reports](#-section-4--multi-table-product-reports) | Top 10 products, category MRP report, full supplier report |
| 5️⃣ | 🟥 [Unsolved Practice Problems](#-section-5--unsolved-practice-problems) | DPP prompts to solve yourself |

---

## 🗂️ The Tables in Play

```
e1.customers   e1.orders   e1.payments
e1.products    e1.categories   e1.suppliers   e1.order_items
```

**Key relationships:**
```
customers.CustomerID  →  orders.CustomerID
orders.OrderID        →  payments.OrderID
orders.OrderID        →  order_items.OrderID
products.ProductID    →  order_items.ProductID
products.CategoryID   →  categories.CategoryID
products.SupplierID   →  suppliers.SupplierID
```

---

<br>

## <span style="color:#2E8B57">🟩 Section 1 — Basic Sales Joins</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_INNER_JOIN_Fundamentals-2E8B57)

### 🎯 The Goal

Calculate total sales by joining `products` with `order_items`, then rolling that up by category and by supplier.

### 1️⃣ Product-Wise Sales With Product Name

**Task:** For every product, find the total sales value from `order_items`.

```sql
select
  p.ProductID,
  p.ProductName,
  sum(oi.Total) as total_sales
from `e1.products` as p
inner join `e1.order_items` as oi
  on p.ProductID = oi.ProductID
group by p.ProductName, p.ProductID
```

| Clause | Purpose |
|---|---|
| `inner join` | Only includes products that actually have order items |
| `sum(oi.Total)` | Aggregates all sales for that product |
| `group by` | One row per product |

### 2️⃣ Category-Wise Total Sales

**Task:** Roll up sales to the category level.

```sql
select
  c.CategoryID,
  c.CategoryName,
  sum(o.Total) as total_sales
from `e1.products` as p
inner join `e1.order_items` as o
  on p.ProductID = o.ProductID
inner join `e1.categories` as c
  on c.CategoryID = p.CategoryID
group by c.CategoryID, c.CategoryName
order by total_sales desc;
```

> 🔗 **Join chain:** `order_items → products → categories`

### 3️⃣ Supplier-Wise Total Sales

**Task:** Roll up sales to the supplier level.

```sql
select
  s.SupplierID,
  s.SupplierName,
  sum(o.Total) as total_sales
from `e1.products` as p
inner join `e1.order_items` as o
  on p.ProductID = o.ProductID
inner join `e1.suppliers` as s
  on s.SupplierID = p.SupplierID
group by s.SupplierID, s.SupplierName
order by total_sales desc;
```

> 🔗 **Join chain:** `order_items → products → suppliers`

### 🧭 Summary Table

| Query | Join Chain | Grouped By |
|---|---|---|
| Product-wise sales | products ↔ order_items | ProductID, ProductName |
| Category-wise sales | order_items ↔ products ↔ categories | CategoryID, CategoryName |
| Supplier-wise sales | order_items ↔ products ↔ suppliers | SupplierID, SupplierName |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#1E6FEB">🟦 Section 2 — Finding Missing Relationships</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_LEFT_%2F_RIGHT_JOIN-1E6FEB)

### 🎯 The Goal

Use `LEFT JOIN` (and `RIGHT JOIN`) to find records that **have no match** on the other side — the classic "what's missing" pattern.

### 1️⃣ Products With No Sales

**Task:** Find products that have never appeared in an order.

```sql
select
  p.ProductID,
  p.ProductName,
  sum(oi.Total) as sales
from `e1.products` as p
left join `e1.order_items` as oi
  on p.ProductID = oi.ProductID
where oi.ProductID is null
group by p.ProductID, p.ProductName
```

| Step | Why |
|---|---|
| `left join` | Keeps **every** product, even with no matching order_items |
| `where oi.ProductID is null` | Filters down to only the products with **no match** |

### 2️⃣ Customers Who Registered But Never Ordered

```sql
select
  c.Name,
  c.CustomerID,
  o.CustomerID,
  o.OrderID
from `e1.customers` as c
left join `e1.orders` as o
  on c.CustomerID = o.CustomerID
where o.OrderID is null
```

> 💡 Same pattern: `LEFT JOIN` + `WHERE ... IS NULL` = "find the ones with no match."

### 3️⃣ Order Count Per Customer — Including Zero Orders

**Task:** Show every customer's order count, even customers with **0** orders.

**Using `LEFT JOIN`:**

```sql
select
  c.CustomerID,
  c.Name,
  count(o.OrderID) as no_of_orders
from `e1.customers` as c
left join `e1.orders` as o
  on c.CustomerID = o.CustomerID
group by c.CustomerID, c.Name
order by no_of_orders asc
```

**Using `RIGHT JOIN`** (equivalent result, flipped table order):

```sql
select
  c.CustomerID,
  c.Name,
  count(o.OrderID) as no_of_orders
from `e1.orders` as o
right join `e1.customers` as c
  on c.CustomerID = o.CustomerID
group by c.CustomerID, c.Name
order by no_of_orders asc
```

> ⚠️ `count(o.OrderID)` counts only **non-null** OrderIDs, so customers with no orders correctly show `0`.

### 🧭 Summary Table

| Pattern | Use Case |
|---|---|
| `LEFT JOIN` + `WHERE right_table.key IS NULL` | Find rows with **no match** (missing relationships) |
| `LEFT JOIN` + `COUNT(right_table.key)` | Count matches per row, **including zero** |
| `RIGHT JOIN` | Same as `LEFT JOIN` with tables swapped — a matter of readability preference |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#D4A017">🟨 Section 3 — Multi-Table Customer Reports</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Three-Table_Joins_%2B_HAVING-D4A017)

### 🎯 The Task

> For every customer, calculate: **Customer ID, Customer name, Number of orders placed, Total amount paid through successful payments only.**
> Display only customers whose successful payment amount is **greater than ₹50,000**. Sort highest → lowest.

### 🔍 Step 1 — Explore the Tables

```sql
select * from `e1.customers` limit 5
select * from `e1.orders`    limit 5
select * from `e1.payments`  limit 5
```

**Relationship map:**
```
c.CustomerID → o.CustomerID
p.OrderID    → o.OrderID
```

### ✅ The Full Query

```sql
select
  c.customerID,
  c.name,
  count(distinct o.orderID) as no_of_orders,
  sum(p.amount) as total_paid
from `e1.customers` as c
inner join `e1.orders` as o
  on c.customerID = o.customerID
inner join `e1.payments` as p
  on p.orderID = o.orderID
where p.status = "Success"
group by c.customerID, c.name
having total_paid > 50000
order by total_paid desc
```

### 🧩 Breaking It Down

| Clause | Purpose |
|---|---|
| `inner join ... orders` | Connects each customer to their orders |
| `inner join ... payments` | Connects each order to its payment records |
| `where p.status = "Success"` | Filters to **only successful** payments **before** aggregating |
| `count(distinct o.orderID)` | Avoids inflating order count from multiple payment rows per order |
| `having total_paid > 50000` | Filters **after** aggregation — can't use `WHERE` on a `SUM()` |
| `order by total_paid desc` | Highest spenders first |

> ⚠️ **Why `DISTINCT` in the count?** Joining orders → payments can create multiple rows per order (if there were retries or multiple payment attempts). `COUNT(DISTINCT o.orderID)` prevents double-counting orders.

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| 3-table join (customers → orders → payments) | Connects customer identity to their financial activity |
| `WHERE` before `GROUP BY` | Filters raw rows (e.g., only successful payments) |
| `HAVING` after `GROUP BY` | Filters aggregated results (e.g., total_paid > 50000) |
| `COUNT(DISTINCT ...)` | Prevents inflated counts from join fan-out |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#E07B00">🟧 Section 4 — Multi-Table Product Reports</span>

![Section](https://img.shields.io/badge/Section-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Four-Table_Joins_%2B_COALESCE-E07B00)

### 1️⃣ Top 10 Products by Total Sales Value

**Task:** Display ProductID, ProductName, CategoryName, SupplierName, number of order-item appearances, total quantity sold, total sales value, and average selling price. Only products with total sales **> ₹1,00,000**.

```sql
select
  p.ProductID,
  p.ProductName,
  c.CategoryName,
  s.SupplierName,
  count(oi.OrderID) as no_of_records,
  sum(oi.Quantity) as total_qty,
  sum(oi.Total) as total_sales,
  avg(oi.sellingprice) as avg_selling_price
from `e1.products` as p
inner join `e1.categories` as c
  on p.CategoryID = c.CategoryID
inner join `e1.suppliers` as s
  on p.SupplierID = s.SupplierID
inner join `e1.order_items` as oi
  on p.ProductID = oi.ProductID
group by
  p.ProductID, p.ProductName, c.CategoryName, s.SupplierName
having total_sales > 100000
order by total_sales desc
limit 10
```

> 🔗 **4-table join:** `products ↔ categories ↔ suppliers ↔ order_items`

### 2️⃣ Category Report — Filtered by Product MRP

**Task:** Only consider products with MRP **> ₹20,000**. For every category: CategoryID, CategoryName, number of qualifying products, average/max/min MRP. Only categories with **more than 2** qualifying products, sorted by avg MRP.

```sql
select
  c.CategoryID,
  c.CategoryName,
  count(p.ProductID) as no_of_products,
  round(avg(p.MRP),2) as avg_mrp,
  max(p.MRP) as max_mrp,
  min(p.MRP) as min_mrp
from `e1.categories` as c
inner join `e1.products` as p
  on c.CategoryID = p.CategoryID
where p.MRP > 20000
group by c.CategoryID, c.CategoryName
having no_of_products > 2
order by avg_mrp desc
```

> ⚠️ **Order matters:** `WHERE p.MRP > 20000` filters individual products **before** grouping; `HAVING no_of_products > 2` filters the **grouped result**.

### 3️⃣ Full Supplier Report — Including Zero-Sales Suppliers

**Task:** For every supplier: SupplierID, SupplierName, number of products supplied, average MRP, total sales, total quantity sold. **Include suppliers with no sales at all** — show 0 instead of NULL.

```sql
select
  s.SupplierID,
  s.SupplierName,
  count(distinct p.ProductID) as prd_cnt,
  avg(p.MRP) as avg_mrp,
  coalesce(sum(oi.Total),0) as total_sales,
  coalesce(sum(oi.Quantity),0) as total_qty
from `e1.suppliers` as s
left join `e1.products` as p
  on s.SupplierID = p.SupplierID
left join `e1.order_items` as oi
  on p.ProductID = oi.ProductID
group by s.SupplierID, s.SupplierName
order by total_sales desc
```

| Clause | Purpose |
|---|---|
| `left join` (both) | Keeps suppliers even with no products, or products with no sales |
| `coalesce(sum(...), 0)` | Converts `NULL` sums (from suppliers with zero matching rows) into `0` |

### 🧭 Summary Table

| Query | Key Technique |
|---|---|
| Top 10 products | 4-table `INNER JOIN` + `HAVING` + `LIMIT` |
| Category MRP report | `WHERE` (row filter) + `HAVING` (group filter) together |
| Full supplier report | `LEFT JOIN` chain + `COALESCE()` to replace NULLs with 0 |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#C0392B">🟥 Section 5 — Unsolved Practice Problems</span>

![Section](https://img.shields.io/badge/Section-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Test_Yourself-C0392B)

### 📝 About This Section

These prompts appear in the source **without** worked solutions — they're meant for you to solve using the patterns from Sections 1–4. Each includes a hint pointing to the relevant technique.

### 1️⃣ Warehouse Sales Report

> For every warehouse, calculate: WarehouseID, Warehouse name, Number of orders handled, Total quantity of products sold, Total sales value. **Include warehouses even if they have no orders.** Display only warehouses where total sales value **> ₹2,00,000**. Sort highest → lowest.

💡 **Hint:** `LEFT JOIN` (to include zero-order warehouses) + `COALESCE()` + `HAVING` — same pattern as the Full Supplier Report in Section 4.

### 2️⃣ Customers Above Average Spending

> Calculate total sales value generated by every customer. Display only customers whose total spending is **greater than the average customer spending**. Show CustomerID, Customer name, Total spending — sorted highest to lowest.

💡 **Hint:** You'll need a **subquery** (or CTE) to first calculate each customer's total spending, then compare each customer against the average of those totals.

```sql
-- Skeleton
select CustomerID, Name, total_spending
from (
  -- calculate each customer's total spending here
) t
where total_spending > (
  -- calculate the AVERAGE of total_spending here
)
order by total_spending desc
```

### 3️⃣ Products Above Their Category's Average Sales

> For every product, calculate its total sales value. Display only products whose total sales value is **greater than the average total sales value of products in the same category**. Show ProductID, ProductName, CategoryName, TotalSales — sorted highest to lowest.

💡 **Hint:** This is trickier than #2 — the "average" here is **per category**, not overall. You'll likely need a subquery that computes average sales **grouped by category**, then join it back to per-product sales.

### 4️⃣ Order Value Classification

> For every order, calculate the total order value (sum of `Total` from `order_items`). Classify each order as:
> - **High Value** → ≥ ₹50,000
> - **Medium Value** → ₹20,000–₹49,999
> - **Low Value** → < ₹20,000
>
> Display: OrderID, OrderDate, CustomerName, TotalOrderValue, OrderCategory. Show highest-value orders first.

💡 **Hint:** This needs a `CASE WHEN ... THEN ... END` expression alongside your join and `GROUP BY`.

```sql
-- Skeleton
select
  o.OrderID,
  o.OrderDate,
  c.Name as CustomerName,
  sum(oi.Total) as TotalOrderValue,
  case
    when sum(oi.Total) >= 50000 then 'High Value'
    when sum(oi.Total) >= 20000 then 'Medium Value'
    else 'Low Value'
  end as OrderCategory
from `e1.orders` as o
-- join customers and order_items, then group by, then order by
```

### 5️⃣ Category-Level Sales Report (Filtered)

> Create a category-level report: CategoryID, CategoryName, number of products in the category, number of *different* products sold, total quantity sold, total sales value, average selling price. **Only consider order-item records where SellingPrice > ₹10,000.** Display only categories where total sales value **> ₹5,00,000**. Sort highest → lowest.

💡 **Hint:** Notice this needs **two different product counts** — total products in the category (regardless of sales) vs. distinct products actually sold. That likely means combining a `LEFT JOIN` with `COUNT(DISTINCT ...)` carefully, plus a `WHERE` filter on `SellingPrice` before aggregating.

### 🔁 DPP Review Set (Same Patterns, Fresh Practice)

The source also repeats these as a standalone practice set — solve them again without looking back to check retention:

| # | Prompt | Related Pattern |
|---|---|---|
| 1 | Top 10 products by total sales value (full detail columns) | Section 4, Query 1 |
| 2 | Category report filtered by MRP > ₹20,000, >2 qualifying products | Section 4, Query 2 |
| 3 | Customers who never ordered — include **City and State** this time | Section 2, Query 2 |
| 4 | Full supplier report including zero-sales suppliers | Section 4, Query 3 |

### 🧭 Summary Table

| Problem | Core Technique Needed |
|---|---|
| Warehouse report | LEFT JOIN + COALESCE + HAVING |
| Above-average customer spending | Subquery comparing against an AVG() |
| Above-average category sales | Subquery grouped by category |
| Order value classification | CASE WHEN |
| Filtered category sales report | WHERE + COUNT(DISTINCT) + HAVING |

[⬆ Back to top](#-table-of-contents)

---

<div align="center">

### 🎉 Roadmap Complete!
*From single inner joins to four-table reports with HAVING, COALESCE, and unsolved challenges to test yourself.*

</div>
