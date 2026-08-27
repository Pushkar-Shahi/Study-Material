<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — Layout</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Positioning_Elements-1E6FEB)

</div>

---

## 📺 1. The `display` Property

Defines an element's behavior and how much space it occupies.

| Value | Behavior | Respects Box Model? | Examples |
|---|---|:---:|---|
| **Block** | Full width, starts new line | ✅ | `<div>`, `<h1>` |
| **Inline** | Only as wide as content, no new line | ❌ (ignores width/height/vertical margin) | `<span>` |
| **Inline-block** | Stays inline **but** allows width/height/margin/padding | ✅ | Hybrid use cases |

```css
.box {
    display: inline-block;
    width: 100px;
    height: 50px;
}
```

---

## 📍 2. Positioning

The `position` property moves elements **out of the normal document flow**.

| Value | Behavior |
|---|---|
| **Static** | Default — follows normal page flow, ignores `top`/`left` |
| **Relative** | Moves relative to its own original position |
| **Absolute** | Removed from flow, positioned relative to nearest **positioned** ancestor |
| **Fixed** | Pinned to the browser window (viewport) — stays put on scroll |
| **Sticky** | Toggles between relative and fixed based on scroll position |

```css
.modal {
    position: fixed;
    top: 0;
    left: 0;
}
```

---

## 🏗️ 3. Advanced Layout Systems

| System | Dimensions | Best For |
|---|:---:|---|
| **Flexbox** | 1D (row *or* column) | Aligning items, distributing space in a container |
| **Grid** | 2D (rows *and* columns) | Complex, structured layouts |

### 🛠️ Handy Grid Functions
| Function | Purpose |
|---|---|
| `repeat()` | Create repeating column/row patterns |
| `minmax()` | Set a size range for responsive columns |

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, minmax(200px, 1fr));
}
```

> [!NOTE]
> Also relevant: **CSS Units** like `px`, `rem`, and `%` — foundational for sizing anything you build.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `display` | Controls how an element occupies space |
| `position` | Controls how an element is placed relative to normal flow |
| Flexbox | One-dimensional alignment and spacing |
| Grid | Two-dimensional row + column layout system |

---

### 🛠️ MLOps Perspective: Grid & Flexbox for Dashboards
> [!IMPORTANT]
> Flexbox and Grid are the secrets to building professional ML dashboards:
> - **Model Comparisons:** Want to display the output of Model A next to Model B side-by-side? That's a Flexbox row layout.
> - **Metric Dashboards:** Tools like Grafana rely heavily on Grid layouts to structure rows and columns of graphs and logs. Understanding Grid helps you design custom metric displays that don't look cluttered.

---

<div align="center">

⬅️ [Previous: Section 1 — Foundations](./01_foundations.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — Dynamic Effects](./03_dynamic_effects.md)

</div>
