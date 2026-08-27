<div align="center">

# <span style="color:#E07B00">🟠 Step 4 — Multimedia & Semantic Layout</span>

![Step](https://img.shields.io/badge/Step-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Meaning_%26_Media-E07B00)

</div>

---

## 🏗️ Semantic Layout Tags

Semantic tags give **meaning** to your code — helping search engines and screen readers understand each part of the page (instead of using generic `<div>` containers everywhere).

| Tag | Purpose |
|:---:|---|
| `<header>` | Top section of the page |
| `<footer>` | Bottom section of the page |
| `<nav>` | Navigation links |
| `<main>` | Primary, unique content of the document |
| `<article>` | Independent content (e.g., a blog post) |
| `<section>` | Thematic grouping of content |
| `<aside>` | Sidebars or indirectly-related content |

```html
<header>...</header>
<nav>...</nav>
<main>
  <article>...</article>
  <aside>...</aside>
</main>
<footer>...</footer>
```

---

## 🎬 Multimedia Tags

| Tag | Purpose | Key Attributes |
|:---:|---|---|
| `<img>` | Display images | `src` (path), `alt` (accessibility text) |
| `<video>` | Embed video | `controls` (play/pause/volume) |
| `<audio>` | Embed audio | `controls` |
| `<iframe>` | Embed content from another site | `src` (e.g., YouTube, Google Maps) |

```html
<img src="photo.jpg" alt="A mountain view">

<video controls>
  <source src="movie.mp4" type="video/mp4">
</video>

<iframe src="https://www.youtube.com/embed/xyz"></iframe>
```

> [!WARNING]
> Always include `alt` text on `<img>` — it's essential for accessibility and SEO.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Semantic tags | Give structural meaning instead of generic `<div>`s |
| `<header>`/`<nav>`/`<main>`/`<footer>` | Define the major layout regions of a page |
| `<article>` vs `<section>` | Independent content vs. thematic grouping |
| `<img>`, `<video>`, `<audio>` | Bring media into the page |
| `<iframe>` | Embed external content |

---

### 🛠️ MLOps Perspective: Model Explainability
> [!NOTE]
> Multimedia tags are vital for displaying ML outputs:
> - **Computer Vision Models:** You'll use `<img>` to display original images next to bounded-box output images from YOLO or mask predictions.
> - **Generative AI:** When serving a diffusion model, the response will be an `<img>` tag, or `<audio>`/`<video>` tags for generated media.
> - **iFrames:** You will frequently use `<iframe>` to embed external monitoring graphs (like Grafana dashboards or Kibana logs) directly into an internal developer portal.

---

<div align="center">

⬅️ [Previous: Step 3 — Organizing Data](./03_organizing_data.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 5 — User Interaction (Forms)](./05_forms.md)

</div>
