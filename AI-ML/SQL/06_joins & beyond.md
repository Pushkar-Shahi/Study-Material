<div align="center">

# 🧮 SQL: Joins, Subqueries & CASE WHEN
### *AI & Machine Learning by Aditya Jain Sir — Lectures 39–42*

![Status](https://img.shields.io/badge/Status-Complete-brightgreen) ![Platform](https://img.shields.io/badge/Platform-Google_BigQuery-4285F4?logo=googlebigquery&logoColor=white)

</div>

---

## 📊 Table of Contents

| # | Section | Focus |
|---|-------|-------|
| 1️⃣ | 🟩 [Basic Sales Joins](#-1--basic-sales-joins) | INNER JOIN — product/category/supplier sales |
| 2️⃣ | 🟦 [Finding Missing Relationships](#-2--finding-missing-relationships) | LEFT/RIGHT JOIN — no-sale products, never-ordered customers |
| 3️⃣ | 🟨 [Multi-Table Reports](#-3--multi-table-reports) | 3–4 table joins, HAVING, LIMIT |
| 4️⃣ | 🟧 [ALTER TABLE & Warehouse Report](#-4--alter-table--warehouse-report) | Renaming columns + full report |
| 5️⃣ | 🟥 [Subqueries: Comparing Against Averages](#-5--subqueries-comparing-against-averages) | Nested & correlated subqueries |
| 6️⃣ | 🟪 [CASE WHEN](#-6--case-when) | Age groups, gender labels, order value tiers |
| 7️⃣ | 🟦‍⬛ [Advanced Integrated Report](#-7--advanced-integrated-report) | Combining WHERE + HAVING + CASE together |

---

## 🗂️ Tables & Relationships

```
e1.customers   e1.orders    e1.payments    e1.warehouses
e1.products    e1.categories   e1.suppliers   e1.order_items

customers.CustomerID  →  orders.CustomerID
orders.OrderID        →  payments.OrderID
orders.OrderID        →  order_items.OrderID
orders.WarehouseID    →  warehouses.WarehouseID
products.ProductID    →  order_items.ProductID
products.CategoryID   →  categories.CategoryID
products.SupplierID   →  suppliers.SupplierID
```

---

<br>

## <span style="color:#2E8B57">🟩 1 — Basic Sales Joins</span>

**Product-wise sales**
```sql
select
  p.ProductID, p.ProductName,
  sum(oi.Total) as total_sales
from `e1.products` as p
inner join `e1.order_items` as oi on p.ProductID = oi.ProductID
group by p.ProductName, p.ProductID
```

**Category-wise sales**
```sql
select
  c.CategoryID, c.CategoryName,
  sum(o.Total) as total_sales
from `e1.products` as p
inner join `e1.order_items` as o on p.ProductID = o.ProductID
inner join `e1.categories` as c on c.CategoryID = p.CategoryID
group by c.CategoryID, c.CategoryName
order by total_sales desc
```

**Supplier-wise sales**
```sql
select
  s.SupplierID, s.SupplierName,
  sum(o.Total) as total_sales
from `e1.products` as p
inner join `e1.order_items` as o on p.ProductID = o.ProductID
inner join `e1.suppliers` as s on s.SupplierID = p.SupplierID
group by s.SupplierID, s.SupplierName
order by total_sales desc
```

> 🔗 All three follow the same shape: `INNER JOIN` products ↔ order_items, then optionally roll up one level further (category or supplier).

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#1E6FEB">🟦 2 — Finding Missing Relationships</span>

**Products with no sales**
```sql
select
  p.ProductID, p.ProductName,
  sum(oi.Total) as sales
from `e1.products` as p
left join `e1.order_items` as oi on p.ProductID = oi.ProductID
where oi.ProductID is null
group by p.ProductID, p.ProductName
```

**Customers who never ordered**
```sql
select c.Name, c.CustomerID, o.OrderID
from `e1.customers` as c
left join `e1.orders` as o on c.CustomerID = o.CustomerID
where o.OrderID is null
```

> 🔁 **Variant:** the same query is often asked with extra columns — swap in `c.City, c.State` alongside `c.Name` and sort with `order by c.Name` to get an alphabetical "never-ordered" customer list with location.

**Order count per customer, including zero**
```sql
select
  c.CustomerID, c.Name,
  count(o.OrderID) as no_of_orders
from `e1.customers` as c
left join `e1.orders` as o on c.CustomerID = o.CustomerID
group by c.CustomerID, c.Name
order by no_of_orders asc
```

> 💡 **The pattern:** `LEFT JOIN` + `WHERE right.key IS NULL` = "find what's missing." `LEFT JOIN` + `COUNT(right.key)` = "count matches, including zero."

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#D4A017">🟨 3 — Multi-Table Reports</span>

**Customer orders + successful payments only, > ₹50,000**
```sql
select
  c.customerID, c.name,
  count(distinct o.orderID) as no_of_orders,
  sum(p.amount) as total_paid
from `e1.customers` as c
inner join `e1.orders` as o on c.customerID = o.customerID
inner join `e1.payments` as p on p.orderID = o.orderID
where p.status = "Success"
group by c.customerID, c.name
having total_paid > 50000
order by total_paid desc
```

**Top 10 products by total sales value, > ₹1,00,000**
```sql
select
  p.ProductID, p.ProductName, c.CategoryName, s.SupplierName,
  count(oi.OrderID) as no_of_records,
  sum(oi.Quantity) as total_qty,
  sum(oi.Total) as total_sales,
  avg(oi.sellingprice) as avg_selling_price
from `e1.products` as p
inner join `e1.categories` as c on p.CategoryID = c.CategoryID
inner join `e1.suppliers` as s on p.SupplierID = s.SupplierID
inner join `e1.order_items` as oi on p.ProductID = oi.ProductID
group by p.ProductID, p.ProductName, c.CategoryName, s.SupplierName
having total_sales > 100000
order by total_sales desc
limit 10
```

**Category report — products with MRP > ₹20,000, >2 qualifying products**
```sql
select
  c.CategoryID, c.CategoryName,
  count(p.ProductID) as no_of_products,
  round(avg(p.MRP),2) as avg_mrp,
  max(p.MRP) as max_mrp, min(p.MRP) as min_mrp
from `e1.categories` as c
inner join `e1.products` as p on c.CategoryID = p.CategoryID
where p.MRP > 20000
group by c.CategoryID, c.CategoryName
having no_of_products > 2
order by avg_mrp desc
```

**Full supplier report — including zero-sales suppliers**
```sql
select
  s.SupplierID, s.SupplierName,
  count(distinct p.ProductID) as prd_cnt,
  avg(p.MRP) as avg_mrp,
  coalesce(sum(oi.Total),0) as total_sales,
  coalesce(sum(oi.Quantity),0) as total_qty
from `e1.suppliers` as s
left join `e1.products` as p on s.SupplierID = p.SupplierID
left join `e1.order_items` as oi on p.ProductID = oi.ProductID
group by s.SupplierID, s.SupplierName
order by total_sales desc
```

> ⚠️ `WHERE` filters rows **before** grouping; `HAVING` filters the **aggregated result** — you'll often need both together.

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#E07B00">🟧 4 — ALTER TABLE & Warehouse Report</span>

**Fix generic column names first:**
```sql
alter table `e1.warehouses` rename column string_field_0 to WarehouseID
alter table `e1.warehouses` rename column string_field_1 to Warehouse
```

**Then build the report — every warehouse included, even with zero orders:**
```sql
select
  w.WarehouseID, w.Warehouse,
  count(distinct o.OrderID) as no_of_orders,
  coalesce(sum(oi.Total),0) as total_sales,
  coalesce(sum(oi.Quantity)) as total_qty
from `e1.warehouses` as w
left join `e1.orders` as o on w.warehouseID = o.WarehouseID
left join `e1.order_items` as oi on o.OrderID = oi.OrderID
group by w.WarehouseID, w.Warehouse
having total_sales > 200000
order by total_sales desc
```

> 💡 Anchoring `FROM` on `warehouses` + `LEFT JOIN` out is what guarantees no warehouse gets dropped, even with no orders.

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#C0392B">🟥 5 — Subqueries: Comparing Against Averages</span>

**Customers above average customer spending**

> ⚠️ Average customer spending = average of *each customer's total*, not `AVG()` over raw order-item rows.

```sql
select
  c.CustomerID, c.Name,
  sum(oi.Total) as total_sales
from `e1.customers` as c
inner join `e1.orders` as o on c.CustomerID = o.CustomerID
inner join `e1.order_items` as oi on o.OrderID = oi.OrderID
group by c.CustomerID, c.Name
having total_sales > (
  select round(avg(total_sales),2)
  from (
    select o.CustomerID, sum(oi.Total) as total_sales
    from `e1.order_items` as oi
    inner join `e1.orders` as o on oi.OrderID = o.OrderID
    group by o.CustomerID
  )
)
order by total_sales desc
```

**Products above their own category's average sales (correlated subquery)**

```sql
select
  p.ProductID, p.ProductName, c.CategoryName,
  sum(oi.Total) as total_sales
from `e1.products` as p
inner join `e1.categories` as c on p.CategoryID = c.CategoryID
inner join `e1.order_items` as oi on p.ProductID = oi.ProductID
group by p.ProductID, p.ProductName, p.CategoryID, c.CategoryName
having total_sales > (
  select avg(total_sales)
  from (
    select p1.ProductID, sum(oi.Total) as total_sales
    from `e1.products` as p1
    inner join `e1.order_items` as oi on p1.ProductID = oi.ProductID
    where p1.CategoryID = p.CategoryID
    group by p1.ProductID
  )
)
order by total_sales desc
```

> ⚠️ `where p1.CategoryID = p.CategoryID` makes this **correlated** — the subquery re-runs per outer row, scoped to that row's category.

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#8E44AD">🟪 6 — CASE WHEN</span>

```sql
case
  when condition1 then result1
  when condition2 then result2
  else default_result
end
```

**Age group classification**
```sql
select
  CustomerID, Age, Name,
  case
    when Age >= 18 and Age <= 20 then "GenZ"
    when Age >= 21 and Age <= 40 then "Adult"
    else "Senior_Citizen"
  end as age_group
from `e1.customers` as c
```

**Gender relabeling**
```sql
select
  CustomerID, Name, Gender,
  case when Gender = 'M' then 'Male' else 'Female' end as Gender_New
from `e1.customers`
```

**Order value classification (High/Medium/Low)**
```sql
select
  o.OrderID, o.OrderDate, c.Name,
  sum(oi.Total) as total_sales,
  case
    when sum(oi.Total) >= 50000 then "High Value"
    when sum(oi.Total) >= 20000 then "Medium Value"
    else "Low Value"
  end as OrderCategory
from `e1.orders` as o
inner join `e1.customers` as c on o.CustomerID = c.CustomerID
inner join `e1.order_items` as oi on o.OrderID = oi.OrderID
group by o.OrderID, o.OrderDate, c.Name
order by total_sales desc
```

> ⚠️ Conditions are checked top-to-bottom — order overlapping ranges from most to least specific, or you'll misclassify rows. `CASE` can also wrap an aggregate like `SUM()`, not just raw columns.

[⬆ Top](#-table-of-contents)

---

<br>

## <span style="color:#008B8B">🟦‍⬛ 7 — Advanced Integrated Report</span>

**Category-level report combining WHERE + dual COUNT(DISTINCT) + HAVING**

```sql
select
  c.CategoryID, c.CategoryName,
  count(distinct p.ProductID) as total_products,
  count(distinct oi.ProductID) as different_products_sold,
  sum(oi.Quantity) as total_qty,
  sum(oi.Total) as total_sales,
  round(avg(oi.SellingPrice),2) as avg_selling_price
from `e1.categories` as c
inner join `e1.products` as p on p.CategoryID = c.CategoryID
inner join `e1.order_items` as oi on oi.ProductID = p.ProductID
where oi.SellingPrice > 10000
group by c.CategoryID, c.CategoryName
having total_sales > 500000
order by total_sales desc
```

**Discount % + high-performing products**

```
discount_percentage = (MRP - SellingPrice) * 100 / MRP
```

```sql
select
  p.ProductID, p.ProductName, c.CategoryName,
  p.MRP, p.SellingPrice,
  ((p.MRP - p.SellingPrice)*100)/p.MRP as discount_percentage,
  sum(oi.Total) as total_sales
from `e1.products` as p
inner join `e1.categories` as c on p.CategoryID = c.CategoryID
inner join `e1.order_items` as oi on p.ProductID = oi.ProductID
where p.MRP > 15000
group by p.ProductID, p.ProductName, c.CategoryName, p.MRP, p.SellingPrice
having
  ((p.MRP - p.SellingPrice)*100)/p.MRP > 20
  and total_sales > 75000
order by discount_percentage desc
```

> 💡 `HAVING` can chain multiple conditions with `AND`, just like `WHERE`.

[⬆ Top](#-table-of-contents)

---

<div align="center">

### 🎉 End of Notes
*Joins → missing relationships → multi-table reports → ALTER TABLE → subqueries → CASE WHEN → combined report.*

</div>
