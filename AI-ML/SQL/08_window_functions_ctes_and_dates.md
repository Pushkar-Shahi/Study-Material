<div align="center">

# 🧮 SQL Part 2: Reports, Window Functions, CTEs & Dates
### *AI & Machine Learning by Aditya Jain Sir — Lectures 43–48*

![Status](https://img.shields.io/badge/Status-Complete-brightgreen) ![Platform](https://img.shields.io/badge/Platform-Google_BigQuery-4285F4?logo=googlebigquery&logoColor=white)

</div>

> 📎 Continues from **SQL_Notes_Combined.md** (Lec 39–42: joins, subqueries, CASE WHEN). The "coming next" topics from that file — window functions and CTEs — are covered here.

---

## 📊 Table of Contents

| # | Section | Focus |
|---|---------|-------|
| 1️⃣ | 🟩 [Aggregate Reports with HAVING](#-1--aggregate-reports-with-having) | GROUP BY + HAVING + ORDER BY across 2–3 tables |
| 2️⃣ | 🟦 [Inventory, Anti-Joins & Multi-Table Joins](#-2--inventory-anti-joins--multi-table-joins) | LEFT JOIN gaps, 4–5 table joins |
| 3️⃣ | 🟨 [CASE WHEN Classifications](#-3--case-when-classifications) | Tiers, stock levels, weekday/weekend |
| 4️⃣ | 🟧 [Subqueries & Derived Tables](#-4--subqueries--derived-tables) | Scalar, correlated, FROM-subquery |
| 5️⃣ | 🟥 [Window Functions](#-5--window-functions) | `OVER`, `PARTITION BY`, `ROW_NUMBER`, `RANK` |
| 6️⃣ | 🟪 [CTEs](#-6--ctes-common-table-expressions) | `WITH ... AS` |
| 7️⃣ | 🟦‍⬛ [Date Functions](#-7--date-functions) | `EXTRACT`, `DATE_TRUNC`, `DATE_DIFF`, `FORMAT_DATE` |
| 8️⃣ | ⬛ [Practice Prompts](#-8--practice-prompts-no-solution-in-source) | Unsolved problems with hints |

---

## 🗂️ New Tables (in addition to Part 1)

```
e1.employees   e1.inventory

orders.EmployeeID      →  employees.EmployeeID
inventory.WarehouseID  →  warehouses.WarehouseID
inventory.ProductID    →  products.ProductID
payments.Status        →  'Success' / 'Failed'
```

---

<br>

## <span style="color:#2E8B57">🟩 1 — Aggregate Reports with HAVING</span>

> 💡 **Recipe:** join the tables → `WHERE` (row filter) → `GROUP BY` → `HAVING` (group filter) → `ORDER BY`.

**Employee: orders handled + distinct customers**
```sql
select
  e.EmployeeID, e.Name, e.Department,
  count(distinct o.OrderID) as total_orders,
  count(distinct o.CustomerID) as different_customers
from `e1.orders` as o
inner join `e1.employees` as e on o.EmployeeID = e.EmployeeID
group by e.EmployeeID, e.Name, e.Department
having total_orders > 5
order by total_orders desc
```

**City report — customers, orders, sales, avg item value (sales > ₹3,00,000)**
```sql
select
  c.City,
  count(distinct c.CustomerID) as no_of_customers,
  count(distinct o.OrderID) as no_of_orders,
  sum(oi.Total) as total_sales,
  round(avg(oi.Total),2) as avg_item_value
from `e1.customers` as c
inner join `e1.orders` as o on c.CustomerID = o.CustomerID
inner join `e1.order_items` as oi on o.OrderID = oi.OrderID
group by c.City
having total_sales > 300000
order by total_sales desc
```

**Products with average selling price > ₹15,000**
```sql
select
  p.ProductID, p.ProductName,
  count(distinct oi.OrderID) as no_of_orders,
  sum(oi.Quantity) as total_qty,
  avg(oi.SellingPrice) as avg_selling_price
from `e1.products` as p
inner join `e1.order_items` as oi on p.ProductID = oi.ProductID
group by p.ProductID, p.ProductName
having avg_selling_price > 15000
order by avg_selling_price desc
```

**Category MRP spread (max − min)**
```sql
select
  c.CategoryName,
  count(distinct p.ProductID) as no_of_products,
  min(p.MRP) as min_mrp,
  max(p.MRP) as max_mrp,
  max(p.MRP) - min(p.MRP) as mrp_diff
from `e1.categories` as c
inner join `e1.products` as p on c.CategoryID = p.CategoryID
group by c.CategoryName
having mrp_diff > 10000
```
> ⚠️ The source problem says **> ₹10,000** but its code used `> 100` — I've used 10000 to match the problem statement.

**Payment method stats (successful only, > 10 transactions)**
```sql
select
  Method,
  count(*) as succ_trans,
  sum(Amount) as succ_amt,
  round(avg(Amount),2) as avg_amt,
  max(Amount) as max_amt
from `e1.payments`
where Status = "Success"
group by Method
having succ_trans > 10
order by avg_amt desc
```

**Top 15 products by quantity sold**
```sql
select
  p.ProductID, p.ProductName, c.CategoryName,
  sum(oi.Quantity) as total_qty,
  sum(oi.Total) as total_sales
from `e1.products` as p
inner join `e1.categories` as c on p.CategoryID = c.CategoryID
inner join `e1.order_items` as oi on p.ProductID = oi.ProductID
group by p.ProductID, p.ProductName, c.CategoryName
order by total_qty desc
limit 15
```

**Category with the highest average selling price** — `ORDER BY ... DESC LIMIT 1`
```sql
select
  c.CategoryID, c.CategoryName,
  round(avg(p.SellingPrice)) as avg_sp
from e1.categories as c
inner join e1.products as p on p.CategoryID = c.CategoryID
group by c.CategoryID, c.CategoryName
order by avg_sp desc
limit 1
```

**Category average discount (needs ≥ 5 products)** — aggregate a computed column
```sql
select
  c.CategoryName,
  count(p.ProductID) as prd_cnt,
  round(avg(p.MRP),2) as avg_mrp,
  round(avg(p.SellingPrice),2) as avg_sp,
  round(avg(p.MRP - p.SellingPrice),2) as avg_discount
from `e1.products` as p
inner join `e1.categories` as c on p.CategoryID = c.CategoryID
group by c.CategoryName
having prd_cnt >= 5
order by avg_discount desc
```

**Business-style reports (same shape, different filters)**

| Ask | Key lines |
|---|---|
| Categories with sales > ₹1,00,000 + distinct products sold | `sum(oi.Total)`, `count(distinct p.ProductID)`, `having total_sales > 100000` |
| Customers who spent > ₹50,000 (with City) | `group by c.CustomerID, c.Name, c.City` + `having total_spent > 50000` |
| Suppliers with sales > ₹2,00,000 | `suppliers → products → order_items`, `having total_sales > 200000` |
| Customers with ≥ 5 orders | `count(o.OrderID)`, `having no_of_orders >= 5` |
| Distinct products bought per customer | `count(distinct oi.ProductID)` |
| Customers on > 2 different order dates | `count(distinct o.OrderDate)`, `having no_of_orderdates > 2` |

> ⚠️ Every non-aggregated column in `SELECT` must also be in `GROUP BY` (that's why `City` appears in both above).

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#1E6FEB">🟦 2 — Inventory, Anti-Joins & Multi-Table Joins</span>

**Warehouse inventory report (avg stock per record > 100)**
```sql
select
  w.WarehouseID, w.Warehouse,
  count(i.WarehouseID) as count_records,
  sum(i.Stock) as total_stock,
  round(avg(i.Stock),2) as avg_stock,
  max(i.Stock) as max_stock
from `e1.warehouses` as w
inner join `e1.inventory` as i on w.WarehouseID = i.WarehouseID
group by w.WarehouseID, w.Warehouse
having avg_stock > 100
order by total_stock desc
```

**Products that have inventory but were never ordered** — INNER JOIN + LEFT JOIN anti-join
```sql
select
  p.ProductID, p.ProductName, p.SupplierID,
  count(i.WarehouseID) as no_of_records,
  sum(i.Stock) as total_stock
from `e1.products` as p
inner join `e1.inventory` as i on p.ProductID = i.ProductID
left join `e1.order_items` as oi on p.ProductID = oi.ProductID
where oi.ProductID is null
group by p.ProductID, p.ProductName, p.SupplierID
order by total_stock desc
```
> 🔁 The source sorted ascending here, but the problem asks highest → lowest, so I added `desc`.

**Customers who bought from ≥ 3 different categories**
```sql
select
  c.CustomerID, c.Name,
  count(distinct p.CategoryID) as no_diff_categories,
  sum(oi.Quantity) as total_qty,
  sum(oi.Total) as total_amt
from `e1.customers` as c
inner join `e1.orders` as o on c.CustomerID = o.CustomerID
inner join `e1.order_items` as oi on o.OrderID = oi.OrderID
inner join `e1.products` as p on oi.ProductID = p.ProductID
group by c.CustomerID, c.Name
having no_diff_categories >= 3
order by no_diff_categories desc
```

**Customers with failed payments** (check the values first: `select distinct status from e1.payments`)
```sql
select
  c.CustomerID, c.Name,
  count(distinct o.OrderID) as total_failed_orders,
  sum(oi.Total) as total_value
from `e1.customers` as c
inner join `e1.orders` as o on c.CustomerID = o.CustomerID
inner join `e1.payments` as p on o.OrderID = p.OrderID
inner join `e1.order_items` as oi on o.OrderID = oi.OrderID
where p.Status = "Failed"
group by c.CustomerID, c.Name
order by total_value desc
```

**Suppliers including those with no sales** — LEFT JOIN + COALESCE
```sql
select
  s.SupplierName,
  count(distinct p.ProductID) as no_of_prds,
  count(oi.OrderItemID) as no_of_oi_rcrds,
  coalesce(sum(oi.Quantity),0) as total_qty_sold,
  coalesce(sum(oi.Total),0) as total_sales_value
from `e1.suppliers` as s
left join `e1.products` as p on s.SupplierID = p.SupplierID
left join `e1.order_items` as oi on p.ProductID = oi.ProductID
group by s.SupplierName
order by total_sales_value desc
```

**Warehouses including those with no orders**
```sql
select
  w.Warehouse,
  count(distinct o.OrderID) as no_of_orders_handled,
  coalesce(sum(i.Stock),0) as total_inventory_stock,
  coalesce(round(avg(i.Stock),2),0) as avg_inventory_stock
from `e1.warehouses` as w
left join `e1.orders` as o on w.WarehouseID = o.WarehouseID
left join `e1.inventory` as i on w.WarehouseID = i.WarehouseID
group by w.Warehouse
```
> ⚠️ **Fan-out gotcha:** `orders` and `inventory` are both one-to-many from `warehouses` but unrelated to each other, so joining both multiplies rows. `count(distinct ...)` survives that, but `sum(i.Stock)` and `avg(i.Stock)` get inflated. For exact stock totals, aggregate inventory separately (subquery/CTE) and then join.

**Every order with customer, product, category (5-table join)**
```sql
select
  c.Name, p.ProductName, ct.CategoryName,
  oi.Quantity, oi.SellingPrice, oi.Total
from `e1.customers` as c
inner join `e1.orders` as o on c.CustomerID = o.CustomerID
inner join `e1.order_items` as oi on o.OrderID = oi.OrderID
inner join `e1.products` as p on oi.ProductID = p.ProductID
inner join `e1.categories` as ct on p.CategoryID = ct.CategoryID
```

**Sales by category *and* supplier** — group by two columns
```sql
select cat.CategoryName, s.SupplierName, sum(oi.Total) as total_sales
from `e1.categories` as cat
inner join `e1.products` as p on cat.CategoryID = p.CategoryID
inner join `e1.suppliers` as s on s.SupplierID = p.SupplierID
inner join `e1.order_items` as oi on p.ProductID = oi.ProductID
group by cat.CategoryName, s.SupplierName
order by total_sales desc
```

**All customers with order count, including 0** — `LEFT JOIN` + `count(o.OrderID)`
```sql
select c.CustomerID, c.Name, count(o.OrderID) as order_count
from `e1.customers` as c
left join `e1.orders` as o on c.CustomerID = o.CustomerID
group by c.CustomerID, c.Name
order by order_count desc
```

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#D4A017">🟨 3 — CASE WHEN Classifications</span>

**Supplier tiers by average MRP**
```sql
select
  s.SupplierName,
  count(p.ProductID) as no_of_products,
  avg(p.MRP) as avg_mrp,
  max(p.MRP) as max_mrp,
  min(p.MRP) as min_mrp,
  case
    when avg(p.MRP) >= 30000 then "Premium Supplier"
    when avg(p.MRP) >= 15000 then "Mid-Range Supplier"
    else "Budget Supplier"
  end as supplierCategory
from `e1.suppliers` as s
inner join `e1.products` as p on s.SupplierID = p.SupplierID
group by s.SupplierName
order by avg_mrp desc
```

**Warehouse stock classification (on `SUM`)**
```sql
select
  w.WarehouseID, w.Warehouse,
  sum(i.Stock) as total_stock,
  round(avg(i.Stock),2) as avg_stock,
  case
    when sum(i.Stock) >= 5000 then "High Stock"
    when sum(i.Stock) >= 2500 then "Medium Stock"
    else "Low Stock"
  end as StockClassification
from `e1.warehouses` as w
inner join `e1.inventory` as i on w.WarehouseID = i.WarehouseID
group by w.WarehouseID, w.Warehouse
order by total_stock desc
```

**Weekend vs. weekday orders** — `CASE` as the `GROUP BY` key
```sql
select
  case
    when extract(DAYOFWEEK from orderDate) in (1,7) then 'Weekend'
    else 'Weekday'
  end as Day_type,
  count(*) as order_count
from `e1.orders`
group by Day_type
```

**First half vs. second half of the year** — orders count, then sales
```sql
select
  case when extract(MONTH from orderdate) <= 6 then 'First Half'
       else 'Second Half' end as year_type,
  sum(oi.total) as total_sales
from `e1.orders` as o
inner join `e1.order_items` as oi on o.OrderID = oi.OrderID
group by year_type
order by total_sales desc
```
(For the plain order count, drop the join and use `count(*)`.)

> 💡 `CASE` can wrap an aggregate (`sum(i.Stock)`) in `SELECT`, or sit in `GROUP BY` as the bucket label. Put the **most specific / highest threshold first**.

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#E07B00">🟧 4 — Subqueries & Derived Tables</span>

**Scalar subquery — products above the overall average MRP**
```sql
select p.ProductID, p.ProductName, c.CategoryName, p.MRP
from `e1.products` as p
inner join `e1.categories` as c on p.CategoryID = c.CategoryID
where p.MRP > (select avg(MRP) from `e1.products`)
order by p.MRP desc
```

**Correlated subquery — highest-MRP product in each category**
```sql
select c.CategoryName, p.ProductID, p.ProductName, p.MRP
from `e1.products` as p
inner join `e1.categories` as c on p.CategoryID = c.CategoryID
where p.MRP = (
  select max(p2.MRP)
  from `e1.products` as p2
  where p2.CategoryID = p.CategoryID
)
order by c.CategoryName
```

**Derived table + conditional count — employee report**

Per-order totals must be computed **first** (a subquery in `FROM`), because "orders above ₹50,000" is itself a `SUM()` per order.
```sql
select
  e.EmployeeID, e.Name, e.Department,
  count(distinct o.OrderID) as orders_handled,
  count(distinct case when OrderTotals.order_value > 50000
                      then o.OrderID end) as HighValueOrders,
  sum(OrderTotals.order_value) as total_sales
from `e1.employees` as e
inner join `e1.orders` as o on e.EmployeeID = o.EmployeeID
inner join (
  select OrderID, sum(Total) as order_value
  from `e1.order_items`
  group by OrderID
) as OrderTotals on o.OrderID = OrderTotals.OrderID
group by e.EmployeeID, e.Name, e.Department
having orders_handled >= 5
order by total_sales desc
```

> 🧩 **Pattern:** `count(distinct case when <cond> then id end)` = "count only the rows meeting a condition" (non-matching rows become `NULL`, which `count` ignores).

> ⚠️ **Heads-up on the "employees with a ₹75,000+ order" problem:** the source solution filters on the employee's *total* (`having sum(oi.Total) > 75000`), which is not the same as "at least one order over ₹75,000". For the strict meaning, use the derived-table pattern above and `where OrderTotals.order_value > 75000` before grouping.

| Subquery type | Where it sits | Example use |
|---|---|---|
| Scalar | `WHERE` / `HAVING` | Compare to an overall average |
| Correlated | `WHERE`, references outer row | Max per group |
| Derived table | `FROM (...) as alias` | Aggregate first, then aggregate again |

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#C0392B">🟥 5 — Window Functions</span>

**The idea:** `GROUP BY` collapses rows; a window function computes an aggregate/rank **while keeping every row**.

```sql
function() over(partition by column order by column)
```

| Part | Meaning |
|---|---|
| `partition by` | Restart the calculation for each group (optional) |
| `order by` | Order inside each partition (needed for ranking) |
| empty `over()` | The whole table is one window |

### Aggregates over a window

```sql
-- Total sales of the product beside every row
select ProductID, OrderID, Total,
  sum(Total) over(partition by ProductID) as product_total_sales
from `e1.order_items`

-- Average selling price of that product beside every row
select ProductID, SellingPrice,
  avg(SellingPrice) over(partition by ProductID) as prd_avg_price
from `e1.order_items`

-- Number of records for that product beside every row
select ProductID, OrderID,
  count(*) over(partition by ProductID) as no_of_records
from `e1.order_items`
```

**Percent of total** — `over()` with no partition = grand total
```sql
select OrderID, ProductID, Total, overall_sales,
  round((Total*100)/overall_sales, 4) as perc_total_sales
from (
  select OrderID, ProductID, Total,
    sum(Total) over() as overall_sales
  from `e1.order_items`
)
```

### Ranking functions

```sql
-- Row number across the whole table
select OrderID, ProductID, Total,
  row_number() over(order by Total desc) as sales_rank
from `e1.order_items`

-- Restart numbering for each product
select ProductID, OrderID, Total,
  row_number() over(partition by ProductID order by Total desc) as prd_row_number
from `e1.order_items`

-- Rank products within each supplier by selling price
select s.supplierName, p.productName, p.SellingPrice,
  rank() over(partition by s.supplierID order by p.SellingPrice desc) as selling_rank
from `e1.products` as p
inner join `e1.suppliers` as s on p.supplierID = s.supplierID
```

### 🆚 `row_number()` vs `rank()` vs `dense_rank()`

Given sales: P001 = 10000, P002 = 9000, P003 = 9000, P004 = 7000

| Product | Sales | `row_number()` | `rank()` | `dense_rank()` |
|---|---:|:---:|:---:|:---:|
| P001 | 10000 | 1 | 1 | 1 |
| P002 | 9000 | 2 | 2 | 2 |
| P003 | 9000 | 3 | 2 | 2 |
| P004 | 7000 | 4 | **4** | **3** |

> 💡 `row_number` never ties · `rank` ties then **skips** numbers · `dense_rank` ties **without skipping**.

### Numbering each customer's orders chronologically

```sql
select CustomerID, OrderID, OrderDate,
  row_number() over(partition by CustomerID order by OrderDate, OrderID) as order_number
from `e1.orders`
order by CustomerID, order_number
```
> ⚠️ Add a tie-breaker (`OrderID`) to `ORDER BY` so two orders on the same date always number in a stable order.

### 🧭 Summary Table

| Function | Purpose |
|---|---|
| `sum/avg/count() over(partition by ...)` | Group-level aggregate beside every row |
| `sum() over()` | Grand total beside every row (for % of total) |
| `row_number()` | Unique sequence 1, 2, 3… |
| `rank()` / `dense_rank()` | Ranking with ties (gaps / no gaps) |
| `partition by` | "Restart for each group" |

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#8E44AD">🟪 6 — CTEs (Common Table Expressions)</span>

A CTE is a **named temporary result** defined with `WITH ... AS (...)` and used by the query right after it — a cleaner alternative to nesting a subquery in `FROM`.

```sql
with product_sales as (
  select ProductID, sum(Total) as total_sales
  from `e1.order_items`
  group by ProductID
)
select
  ProductID, total_sales,
  rank() over(order by total_sales desc) as sales_rank
from product_sales
```

Swap `rank()` for `dense_rank()` to avoid gaps after ties.

**CTE + join — customers whose first order was in their signup month**
```sql
with first_orders as (
  select CustomerID, min(orderdate) as first_order_date
  from `e1.orders`
  group by CustomerID
)
select c.CustomerID, c.Name, c.SignupDate, f.first_order_date
from `e1.customers` as c
inner join first_orders as f on c.CustomerID = f.CustomerID
where date_trunc(c.SignupDate, MONTH) = date_trunc(f.first_order_date, MONTH)
order by c.SignupDate
```

| Why use a CTE | Benefit |
|---|---|
| Aggregate first, then rank/filter | Window functions can't be used directly with `GROUP BY` results in the same level — CTE separates the steps |
| Readability | Name each step instead of deep nesting |

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#008B8B">🟦‍⬛ 7 — Date Functions</span>

BigQuery dates are `YYYY-MM-DD` (e.g., `2024-01-15`).

| Function | Purpose | Example |
|---|---|---|
| `current_date()` | Today's date | `select current_date() as today` |
| `date_sub(d, interval n unit)` | Date n units before `d` | `date_sub(current_date(), interval 1000 day)` |
| `extract(part from d)` | Pull out YEAR / MONTH / DAY / DAYOFWEEK | `extract(year from orderDate)` |
| `date_trunc(d, unit)` | Snap a date to the start of its month/year | `date_trunc('2024-03-15', MONTH)` → `2024-03-01` |
| `date_diff(d1, d2, unit)` | `d1 − d2` in the given unit | `date_diff(DATE '2024-01-20', DATE '2024-01-10', DAY)` → `10` |
| `format_date(fmt, d)` | Date → text | `'%A'` = full day name, `'%B'` = full month name |

> ⚠️ `extract(DAYOFWEEK ...)`: **1 = Sunday, 7 = Saturday** — so weekend = `in (1,7)`.

**Recent signups (last 1000 days)**
```sql
select Name, SignupDate
from `e1.customers`
where SignupDate >= date_sub(current_date(), interval 1000 day)
```

**Days each customer has been registered**
```sql
select CustomerID, SignupDate,
  date_diff(current_date(), SignupDate, DAY) as days
from `e1.customers`
```

**Orders per year / per month / per year-month**
```sql
select extract(year from orderDate) as order_year, count(*) as no_of_orders
from `e1.orders`
group by order_year
order by order_year desc

select extract(year from orderDate) as order_year,
       extract(month from orderDate) as order_month,
       count(*) as no_of_orders
from `e1.orders`
group by order_year, order_month
order by order_year desc, order_month desc
```
> ⚠️ Grouping by **month alone** merges every year's January together — add `year` to the `GROUP BY` for a true monthly timeline.

**Monthly sales** — `date_trunc` gives one clean date per month
```sql
select date_trunc(OrderDate, MONTH) as sales_month, sum(oi.Total) as total_sales
from `e1.orders` as o
inner join `e1.order_items` as oi on o.OrderID = oi.OrderID
group by sales_month
order by sales_month
```

**Weekend orders by day name (Saturday / Sunday)**
```sql
select format_date('%A', OrderDate) as day_name, count(*) as order_count
from `e1.orders`
where extract(DAYOFWEEK from orderDate) in (1,7)
group by day_name
order by order_count desc
```

**Signups per calendar month, any year (all Januaries together)**
```sql
select
  extract(MONTH from signupdate) as signup_month,
  format_date('%B', signupdate) as Month_Name,
  count(*) as customer_count
from `e1.customers`
group by signup_month, Month_Name
```

**Busiest signup weekday**
```sql
select extract(DAYOFWEEK from signupdate) as day_num,
       format_date('%A', signupdate) as day_name,
       count(*) as no_of_signup
from `e1.customers`
group by day_num, day_name
order by no_of_signup desc
```

**Orders in the first 7 days of each month**
```sql
select date_trunc(OrderDate, MONTH) as order_month,
       format_date('%B', OrderDate) as month_name,
       count(*) as no_of_orders
from `e1.orders`
where extract(DAY from orderDate) <= 7
group by order_month, month_name
```

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#2C3E50">⬛ 8 — Practice Prompts (no solution in source)</span>

| Prompt | Hint |
|---|---|
| Classify each **inventory row** — `Stock >= 200` High, `50–199` Medium, `< 50` Low; show WarehouseID, ProductID, Stock, Status; sort by WarehouseID, Stock desc | `CASE WHEN` on the raw `Stock` column (no `GROUP BY`) + `ORDER BY WarehouseID, Stock desc` |
| Total sales for **each calendar week** | `date_trunc(OrderDate, WEEK)` + join `order_items` + `sum(Total)` |
| Group customers into **signup cohorts** by month — signup month + number of customers | `date_trunc(SignupDate, MONTH)` + `count(*)` + `group by` |

---

<div align="center">

### 🎉 End of Part 2
*Aggregate reports → anti-joins → CASE tiers → subqueries → window functions → CTEs → date analysis.*

</div>
