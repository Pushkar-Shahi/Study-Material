<div align="center">

# <span style="color:#D4A017">🟡 Step 3 — Organizing Data</span>

![Step](https://img.shields.io/badge/Step-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Lists_%26_Tables-D4A017)

</div>

---

## 📋 1. HTML Lists

| List Type | Tag | Use Case | Item Tag |
|---|:---:|---|:---:|
| **Unordered** | `<ul>` | Order doesn't matter (shopping list) | `<li>` |
| **Ordered** | `<ol>` | Order matters (recipe steps) | `<li>` |
| **Description** | `<dl>` | Terms & definitions | `<dt>` / `<dd>` |

```html
<ul>
    <li>Milk</li>
    <li>Eggs</li>
</ul>

<ol>
    <li>Preheat oven</li>
    <li>Mix ingredients</li>
</ol>

<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
</dl>
```

---

## 🗃️ 2. HTML Tables

Used to display data in **rows and columns**.

| Tag | Purpose |
|:---:|---|
| `<table>` | Main container for the entire table |
| `<tr>` | Table Row — a horizontal row of cells |
| `<td>` | Table Data — an individual cell |
| `<th>` | Table Header — bold, centered header cell |
| `<thead>` | Groups header row(s) |
| `<tbody>` | Groups main content rows |

```html
<table>
  <thead>
    <tr><th>Name</th><th>Age</th></tr>
  </thead>
  <tbody>
    <tr><td>Aditya</td><td>21</td></tr>
  </tbody>
</table>
```

---

## 🔗 3. Merging Cells

| Attribute | Direction | Purpose |
|:---:|---|---|
| `colspan` | ↔️ Horizontal | Merge cells **across columns** |
| `rowspan` | ↕️ Vertical | Merge cells **across rows** |

```html
<tr>
  <td colspan="2">Merged across 2 columns</td>
</tr>
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `<ul>` / `<ol>` / `<dl>` | Group one-dimensional related items |
| `<table>` / `<tr>` / `<td>` / `<th>` | Structure grid-based data |
| `<thead>` / `<tbody>` | Organize table into header + content sections |
| `colspan` / `rowspan` | Merge table cells across columns/rows |

---

### 🛠️ MLOps Perspective: Tables & Dashboards
> [!IMPORTANT]
> HTML tables are the foundation of ML monitoring dashboards.
> - When you display a Pandas DataFrame in a Jupyter Notebook, Pandas is rendering a `<table>` tag behind the scenes.
> - Tools like Weights & Biases (W&B) or MLflow use HTML tables to display hyperparameter sweep results, metrics, and model version histories.
> - Understanding `colspan` and `rowspan` helps you format automated metric reports sent via email.

---

<div align="center">

⬅️ [Previous: Step 2 — HTML Basics](./02_html_basics.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 4 — Multimedia & Semantic Layout](./04_multimedia_semantic.md)

</div>
