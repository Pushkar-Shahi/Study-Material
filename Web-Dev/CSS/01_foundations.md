<div align="center">

# <span style="color:#2E8B57">🟢 Section 1 — Foundations</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Core_Syntax-2E8B57)

</div>

---

## 🎨 What Is CSS?

**CSS (Cascading Style Sheets)** manages the **visual style** of a webpage, while HTML provides the structure.

---

## 🔗 1. Types of CSS

| Type | Where It Lives | Example |
|---|---|---|
| **Inline** | Directly inside an HTML tag | `<p style="color:red;">` |
| **Internal** | Inside a `<style>` tag in `<head>` | `<style>p { color: red; }</style>` |
| **External** | Separate `.css` file, linked via `<link>` | `<link rel="stylesheet" href="style.css">` |

```html
<!-- External CSS -->
<link rel="stylesheet" href="style.css">
```

---

## 🎯 2. Selectors & Specificity

| Selector | Targets | Syntax |
|---|---|---|
| **Element** | Tags directly | `p { }`, `h1 { }` |
| **Class** | Multiple elements | `.myClass { }` |
| **ID** | One unique element | `#myID { }` |
| **Universal** | Every element on the page | `* { }` |

### ⚖️ Specificity Hierarchy
When multiple selectors target the same element, this order decides which wins:

```
Inline  >  ID  >  Class  >  Element
```

---

## 📦 3. The Box Model

Every CSS element is a rectangular box made of **four layers**:

| Layer | Description |
|---|---|
| 📝 **Content** | Innermost part — text or images |
| 🧽 **Padding** | Transparent space between content and border |
| 🖼️ **Border** | Visible frame around padding + content |
| ↔️ **Margin** | Outermost transparent space, separates from other elements |

```css
.box {
    padding: 10px;
    border: 2px solid black;
    margin: 20px;
}
```

> [!TIP]
> The Box Model determines **exactly how much space** an element occupies on screen — crucial for layout debugging.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Inline / Internal / External | Three ways to attach CSS to HTML |
| Element / Class / ID / Universal selectors | Different ways to target elements |
| Specificity | Rule for resolving conflicting styles |
| Box Model | Content + Padding + Border + Margin |

---

### 🛠️ MLOps Perspective: CSS in ML Frameworks
> [!NOTE]
> Even in Python-heavy ML environments, CSS selectors are essential:
> - **Web Scraping:** If you need to build a custom dataset by scraping the web (e.g., using Beautiful Soup or Selenium), you use CSS Selectors (`.class`, `#id`) to extract specific data.
> - **Streamlit/Gradio:** You can inject custom styles into these ML UI libraries using `<style>` blocks (Internal CSS) to override the default themes.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 2 — Layout](./02_layout.md)

</div>
