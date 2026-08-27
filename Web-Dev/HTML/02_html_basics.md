<div align="center">

# <span style="color:#1E6FEB">🔵 Step 2 — HTML Basics</span>

![Step](https://img.shields.io/badge/Step-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Page_Structure-1E6FEB)

</div>

---

## 🧱 What Is HTML?

**HTML (HyperText Markup Language)** is the standard language used to structure web pages.

| Term | Meaning |
|---|---|
| **Hyper**Text | Text that links to other pages |
| **Markup** | Using tags to tell the browser what kind of content it's rendering |

---

## 🏷️ Tags, Elements, and Attributes

| Term | Definition | Example |
|---|---|---|
| **Tag** | Keyword in angle brackets | `<p>` |
| **Element** | Opening tag + content + closing tag | `<h1>Title</h1>` |
| **Attribute** | Extra property on an opening tag | `lang="en"` |

---

## 💀 The HTML Boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <!-- Visible content goes here -->
</body>
</html>
```

| Part | Purpose |
|---|---|
| `<!DOCTYPE html>` | Declares this as an HTML5 document |
| `<html lang="en">` | Root element containing everything |
| `<head>` | Invisible info — page `<title>`, viewport settings |
| `<body>` | All visible content — text, images, buttons |

---

## 📝 Core Content Tags

### Headings
```html
<h1>Main Title</h1>
<h2>Subtitle</h2>
```
- Six levels: `<h1>` → `<h6>`
- ✅ Best practice: only **one `<h1>`** per page

### Paragraphs
```html
<p>This is a standard block of text.</p>
```

---

## 📦 Block vs. Inline Elements

| Type | Behavior | Examples |
|---|---|---|
| **Block** | Takes full width, starts new line | `<h1>`, `<p>`, `<div>` |
| **Inline** | Only as wide as its content | `<span>`, `<a>` |

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Tag vs. Element vs. Attribute | The three building blocks of HTML syntax |
| Boilerplate | Standard skeleton every HTML file needs |
| `<head>` vs. `<body>` | Invisible metadata vs. visible content |
| Headings & Paragraphs | Core text content markers |
| Block vs. Inline | How elements occupy space on the page |

---

### 🛠️ MLOps Perspective: Web Interfaces
> [!NOTE]
> Even if you use Python libraries like Gradio or Streamlit to build ML demos quickly, they are just generating HTML under the hood. 
> - If you need to embed a Gradio app into your company's existing website, you'll use an `<iframe>` (an HTML element).
> - When generating automated PDF reports from model training runs, you will often render HTML first and convert it to PDF.

---

<div align="center">

⬅️ [Previous: Step 1 — How the Web Works](./01_how_the_web_works.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 3 — Organizing Data](./03_organizing_data.md)

</div>
