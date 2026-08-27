<div align="center">

# <span style="color:#D4A017">🟡 Section 3 — Styling Basics</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Utility_Classes-D4A017)

</div>

---

## 🎨 Colors & Backgrounds

Tailwind uses a **numeric scale from 50 to 950** for color shades.

```html
<div class="bg-red-50">Lightest red</div>
<div class="bg-red-950">Darkest red</div>
<p class="text-gray-900">Dark text</p>
<p class="text-white">White text</p>
```

| Scale | Meaning |
|:---:|---|
| `50` | Lightest shade |
| `500` | Base/medium shade |
| `950` | Darkest shade |

---

## 🔠 Typography

| Class | Purpose |
|---|---|
| `text-4xl` | Text size |
| `font-bold` | Text weight |
| `text-lg` | Readability-friendly size |

```html
<h1 class="text-4xl font-bold">Big Bold Heading</h1>
<p class="text-lg">Readable body text</p>
```

---

## 📏 Spacing (Padding & Margin)

| Class | Effect |
|---|---|
| `p-8` | Padding on **all sides** |
| `px-6` | **Horizontal** padding |
| `mb-4` | Margin on the **bottom** |

```html
<div class="p-8 px-6 mb-4">Spaced content</div>
```

> [!NOTE]
> Spacing values are based on a standard scale (e.g., `1` unit ≈ `0.25rem`).

---

## 📐 Layout & Shapes

| Class | Effect |
|---|---|
| `min-h-screen` | Container covers full device height |
| `rounded-lg` | Rounded corners on buttons/boxes |

```html
<div class="min-h-screen rounded-lg">Full-height rounded container</div>
```

---

## 🖱️ Interactivity

Style different **states** using prefixes.

```html
<button class="bg-red-500 hover:bg-red-700 transition-colors">
    Hover me
</button>
```

| Prefix | Trigger |
|---|---|
| `hover:` | Only applies when the user hovers |
| `transition-colors` | Makes state changes smooth, not instant |

---

## 🛠️ Custom Variables

Define your own CSS variables for project-specific needs:

```css
:root {
    --color-primary: #3490dc;
}
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `bg-*` / `text-*` | Apply background and text colors |
| `text-4xl` / `font-bold` | Control typography size and weight |
| `p-*` / `px-*` / `mb-*` | Add padding and margin shorthand |
| `min-h-screen` / `rounded-lg` | Layout sizing and shape utilities |
| `hover:*` + `transition-colors` | Smooth interactive state changes |
| Custom CSS variables | Reusable project-specific values |

---

### 🛠️ MLOps Perspective: Rapid UI Prototyping
> [!IMPORTANT]
> When integrating an ML model into a web interface (e.g., a FastAPI backend rendering Jinja templates), utility classes are a lifesaver.
> - You don't need to invent class names like `.model-prediction-container` and write 20 lines of CSS.
> - You simply write `<div class="p-4 bg-gray-100 rounded-lg text-lg">` and instantly have a clean box to display inference results.
> - This keeps you focused on what matters: the machine learning pipeline, rather than CSS syntax errors.

---

<div align="center">

⬅️ [Previous: Section 2 — The Build Process](./02_build_process.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 4 — Responsive Design](./04_responsive_design.md)

</div>
