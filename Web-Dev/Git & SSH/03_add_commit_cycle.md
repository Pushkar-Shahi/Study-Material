<div align="center">

# <span style="color:#D4A017">🟡 Step 3 — Saving Your Work Locally (Add & Commit)</span>

![Step](https://img.shields.io/badge/Step-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Staging_%26_Snapshots-D4A017)

</div>

---

## 📦 The Shipping-Box Analogy

| Git Action | Like... |
|---|---|
| **Staging** (`git add`) | Placing items inside a box |
| **Committing** (`git commit`) | Taping the box shut and labeling it |

---

## 1️⃣ Staging Your Files — `git add`

When you create or modify files, Git notices they're **"untracked"** or **"modified"**. You must tell Git which ones to include in your next save.

```bash
git add index.html        # stage a single file
git add .                 # stage all files and changes
```

> [!WARNING]
> `git add` only **prepares** your files — it does **not** permanently save them or upload them to GitHub.

---

## 2️⃣ Committing Your Changes — `git commit`

Once staged, take a permanent **snapshot** of your project. Every commit needs a short, descriptive message.

```bash
git commit -m "Add homepage layout"
```

> [!NOTE]
> This snapshot is saved securely in your **local** repository's history (`.git` folder) — it's still only on your computer, not on the internet yet.

---

## 🔁 The Daily Loop

Once comfortable, your local routine boils down to:

```bash
git status              # 1. See what's modified
git add .                # 2. Stage all changes
git commit -m "message"   # 3. Save your snapshot
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `git add <file>` | Stage a specific file |
| `git add .` | Stage all changes at once |
| `git commit -m "..."` | Save a permanent, labeled snapshot |
| `git status` | Check what's staged/modified/untracked |

---

### 🛠️ MLOps Perspective: Tying Code to Experiments
> [!NOTE]
> The Add & Commit cycle is the heartbeat of Machine Learning reproducibility:
> - **Code + Model Coupling:** You should commit your training script (`train.py`) at the exact same time you save your model weights using an artifact tracker (like MLflow or DVC).
> - **Commit Messages:** Writing "Updated model" is a bad commit message. Writing "Switched to Adam optimizer, LR=0.001, fixed overfitting" allows you to track exactly which code change improved your model's F1 score.

---

<div align="center">

⬅️ [Previous: Step 2 — Local Repository](./02_local_repository.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 4 — Connecting to GitHub](./04_connecting_to_github.md)

</div>
