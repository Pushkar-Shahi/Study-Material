<div align="center">

# <span style="color:#2E8B57">🟢 Section 1 — Installation & Setup</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Tooling-2E8B57)

</div>

---

## 📦 1. Prerequisites (Node.js & npm)

Tailwind relies on Node.js and its package manager (`npm`) to process and compile CSS.
- **Node.js**: The JavaScript runtime environment that runs Tailwind.
- **npm**: Used to download and install the Tailwind package into your project.

---

## ⚙️ 2. Project Initialization

Before installing Tailwind, you must initialize an npm project. This creates a `package.json` file to track dependencies.

```bash
npm init -y
```

---

## 📥 3. Installing Tailwind

Install Tailwind CSS and its Command Line Interface (CLI).

```bash
npm install tailwindcss @tailwindcss/cli
```
> [!NOTE]
> This creates a `node_modules` folder where the actual Tailwind code lives.

---

## 🔗 4. Linking Tailwind to Your CSS

You don't write CSS in Tailwind; you import its engine. Create an `input.css` file and add:

```css
@import "tailwindcss";
```

This tells the compiler, *"Inject all of Tailwind's utility classes here."*

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `node -v` | Confirms Node.js is installed and version-compatible |
| `npm init -y` | Creates `package.json` for your project |
| `npm install tailwindcss @tailwindcss/cli` | Installs Tailwind's core + CLI tool |
| `input.css` with `@import "tailwindcss"` | Source file that pulls in Tailwind |
| `<link>` in `<head>` | Connects the compiled CSS to your HTML |
| `--watch` | Keeps the CLI running to auto-rebuild on save |

---

### 🛠️ MLOps Perspective: Package Management & Node.js
> [!NOTE]
> The Node/npm ecosystem is conceptually identical to Python's `pip` and `requirements.txt`:
> - `npm install` is like `pip install`.
> - `package.json` is your `requirements.txt` / `pyproject.toml`.
> - `node_modules` is essentially your virtual environment (`venv`).
> When configuring CI/CD pipelines (e.g., GitHub Actions) for a full-stack ML application, you will often need a build step that runs `npm install` alongside `pip install` to prepare the frontend assets before deploying to AWS/GCP.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 2 — The Build Process](./02_build_process.md)

</div>
