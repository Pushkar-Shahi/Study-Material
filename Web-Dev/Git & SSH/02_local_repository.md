<div align="center">

# <span style="color:#1E6FEB">🔵 Step 2 — Creating Your First Local Repository</span>

![Step](https://img.shields.io/badge/Step-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Initialization-1E6FEB)

</div>

---

## 📂 Navigate to Your Project

```bash
cd path/to/your-project
```

---

## 🚀 Initialize the Repository

```bash
git init
```

---

## 🧠 What Actually Happens?

| Effect | Description |
|---|---|
| 🔄 **Transforms your folder** | Turns an ordinary folder into a local Git repository |
| 📁 **Creates a hidden folder** | Adds a `.git` folder inside your project |
| 🧠 **The `.git` folder is "the brain"** | Stores all project history, configuration, and version tracking data |

> [!TIP]
> As long as the `.git` folder exists, Git is actively watching your files.

---

## ✅ Verify It's Active

```bash
git status
```

Confirms Git is initialized and shows the current state of your files (tracked, untracked, modified, etc.).

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `cd path/to/your-project` | Navigate into the folder you want to track |
| `git init` | Turns a folder into a Git repository |
| `.git` folder | Git's hidden database — history, config, tracking data |
| `git status` | Confirms Git is active and shows current file states |

---

### 🛠️ MLOps Perspective: Local vs. Cloud Tracking
> [!IMPORTANT]
> The concept of `.git` (a hidden local database) is identical to how ML tracking tools work.
> - When you run `mlflow init` or `dvc init`, they create hidden folders (`.mlruns` or `.dvc`) right next to your `.git` folder.
> - These folders act as the "brain" for your ML experiments (tracking hyperparameters and datasets) just like `.git` tracks code.
> - In MLOps, you treat your entire project folder as an isolated environment where code, data, and models are all tracked locally before syncing to the cloud.

---

<div align="center">

⬅️ [Previous: Step 1 — Configuration](./01_configuration.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 3 — Add & Commit Cycle](./03_add_commit_cycle.md)

</div>
