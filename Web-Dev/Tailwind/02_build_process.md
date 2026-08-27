<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — The Build Process</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Compiling_CSS-1E6FEB)

</div>

---

## ⚙️ The Core Command

```bash
npx @tailwindcss/cli -i input.css -o output.css --watch
```

This single command drives the entire compilation pipeline.

---

## 🔄 Input vs. Output

| Flag | File | Role |
|:---:|---|---|
| `-i` | `input.css` | Contains `@import "tailwindcss";` — tells the compiler to pull in Tailwind's core styles |
| `-o` | `output.css` | The **final** generated CSS file — this is what you link in your HTML `<head>` |

```
input.css  →  [Tailwind Compiler]  →  output.css  →  linked in HTML
```

---

## 👀 Watch Mode

Adding `--watch` keeps the CLI **active** in your terminal.

> [!TIP]
> Every time you save a change in your HTML or CSS, Tailwind performs an **incremental rebuild** to update `output.css` instantly.

```bash
npx @tailwindcss/cli -i input.css -o output.css --watch
```

---

## 🚀 Production Build

When you're ready to launch, add the `--minify` flag for a smaller, optimized CSS file:

```bash
npx @tailwindcss/cli -i input.css -o output.css --minify
```

---

## 📜 Simplify with npm Scripts

Add a `"dev"` script to your `package.json`:

```json
{
  "scripts": {
    "dev": "npx @tailwindcss/cli -i input.css -o output.css --watch"
  }
}
```

Now you can just run:
```bash
npm run dev
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `-i input.css` | Source file with the Tailwind import |
| `-o output.css` | Compiled CSS file linked in your HTML |
| `--watch` | Auto-rebuilds on every save |
| `--minify` | Optimized, smaller CSS for production |
| `npm run dev` | Shortcut script to start the build process |

---

### 🛠️ MLOps Perspective: Build Processes & CI/CD
> [!IMPORTANT]
> The Tailwind build process is a perfect micro-example of a CI/CD pipeline step:
> - **Compilation:** Transforming `input.css` into `output.css` is analogous to compiling a custom CUDA kernel or building a Docker container for a model.
> - **Minification:** The `--minify` flag reduces payload size for production. In MLOps, this is similar to model quantization/pruning (e.g., using ONNX Runtime or TensorRT) — reducing the footprint of the model so inference is faster over the network.
> - When deploying a web app that serves ML models, the CI/CD pipeline will automatically run the Tailwind build script before packing the static assets into a Docker image.

---

<div align="center">

⬅️ [Previous: Section 1 — Installation & Setup](./01_installation_setup.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — Styling Basics](./03_styling_basics.md)

</div>
