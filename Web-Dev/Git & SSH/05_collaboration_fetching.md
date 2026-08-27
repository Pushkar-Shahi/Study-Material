<div align="center">

# <span style="color:#C0392B">🔴 Step 5 — Collaboration & Fetching Code</span>

![Step](https://img.shields.io/badge/Step-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Working_With_Others-C0392B)

</div>

---

## 1️⃣ Getting a Project — `git clone`

If a project **already exists** on GitHub and you want a copy, don't use `git init` — **clone** it instead.

> [!NOTE]
> Cloning downloads the entire repository — including its full version history — and **automatically links** it to GitHub for you.

```bash
git clone git@github.com:YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

> [!TIP]
> Run `git remote -v` inside the cloned folder — Git has already linked it to GitHub for you.

---

## 2️⃣ Getting the Latest Changes — `git pull`

If someone else pushed new code (or you pushed from another computer), your local copy is now out of date.

```bash
git pull
```

This downloads and **merges** the new changes directly into your local files.

---

## 🌟 The Golden Rule of Collaboration

> [!WARNING]
> **Always run `git pull` before you start typing any new code.**
> This ensures you're building on the latest version and avoids annoying merge conflicts later.

---

## 🔄 The Complete Collaboration Loop

```bash
git pull                          # 1. Download the latest changes
[make your edits]                 # 2. Write your code
git add .                         # 3. Stage your changes
git commit -m "describe your work" # 4. Save a local snapshot
git push                          # 5. Upload to GitHub
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `git clone <url>` | Download an existing repo + link it to GitHub |
| `git pull` | Fetch and merge the latest remote changes |
| Golden Rule | Always `pull` before you start new work |
| Collaboration Loop | pull → edit → add → commit → push |

---

### 🛠️ MLOps Perspective: Collaborative Data Science
> [!NOTE]
> `git pull` prevents disasters in ML teams:
> - **Jupyter Notebook Conflicts:** If you and a coworker edit the same Jupyter Notebook without pulling first, the resulting merge conflict is almost impossible to fix manually (because notebooks are raw JSON).
> - **Feature Branches:** In MLOps, Data Scientist A works on a `feature/random-forest` branch, and Data Scientist B works on `feature/xgboost`. They use `git pull` to fetch each other's branches and test them locally to see which model performs better before merging.

---

<div align="center">

⬅️ [Previous: Step 4 — Connecting to GitHub](./04_connecting_to_github.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 6 — SSH Authentication](./06_ssh_authentication.md)

</div>
