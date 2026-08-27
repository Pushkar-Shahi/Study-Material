<div align="center">

# <span style="color:#E07B00">🟠 Section 4 — Responsiveness</span>

![Section](https://img.shields.io/badge/Section-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Adapting_to_Any_Screen-E07B00)

</div>

---

## 📱 1. Media Queries

The primary tool for responsiveness — apply CSS **only when certain conditions** (like viewport width) are met.

```css
@media (max-width: 575px) {
    body {
        font-size: 14px;
    }
}
```

> [!TIP]
> Example above targets small mobile devices to shrink font size or change layout.

---

## 📏 2. Standard Breakpoint Ranges

| Device Category | Width Range |
|---|---|
| 📱 Mobile Portrait | `0px — 575px` |
| 📱 Tablets | `768px — 991px` |
| 💻 Laptops / Small Desktops | `992px — 1199px` |
| 🖥️ Extra Large Screens | `1400px` and up |

> [!NOTE]
> These are the widths where a design "breaks" and needs layout adjustments.

---

## 🌊 3. Fluid Layouts with Relative Units

| Unit | Best For |
|---|---|
| `%` | Fluid grid widths, flexible columns |
| `rem` | Accessible typography, structural spacing |
| `vw` / `vh` | Scales based on % of browser window width/height |

```css
.container {
    width: 90%;
    padding: 2rem;
    height: 50vh;
}
```

> [!WARNING]
> Avoid fixed `px` for layout-critical sizing — relative units scale better across devices.

---

## 🛠️ 4. Responsive Grid & Flexbox

Modern layout systems **reduce the need** for complex media queries.

| Tool | Purpose |
|---|---|
| `minmax()` | Keeps a Grid column within a size range (e.g., min 200px, expand to fill) |
| `auto-fit` / `auto-fill` | Automatically wraps items into new rows as the screen shrinks |

```css
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `@media` | Apply CSS conditionally based on device/viewport |
| Breakpoints | Standard widths where layouts need to adapt |
| `%`, `rem`, `vw/vh` | Relative units that scale fluidly |
| `minmax()` + `auto-fit/auto-fill` | Self-adjusting Grid layouts with fewer media queries |

---

### 🛠️ MLOps Perspective: Mobile-First Dashboards
> [!IMPORTANT]
> The stakeholders looking at your ML model's performance (PMs, Executives) are often looking at them on their phones during a meeting.
> - If your Grafana or W&B dashboard is completely broken on a mobile screen, it doesn't matter how good the model is.
> - Understanding `@media` queries and fluid `%` units ensures your model tracking and data science visualizations scale correctly on every device.

---

<div align="center">

⬅️ [Previous: Section 3 — Dynamic Effects](./03_dynamic_effects.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full CSS Roadmap!

</div>
