<div align="center">

# <span style="color:#E07B00">🟠 Step 4 — Connecting and Pushing to GitHub</span>

![Step](https://img.shields.io/badge/Step-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Local_to_Remote-E07B00)

</div>

---

## 1️⃣ Create a Remote Repository on GitHub

| Action | Detail |
|---|---|
| Click `+` (top-right) | Select **New repository** |
| Name it | e.g., `my-first-project` |
| Visibility | Choose **Public** or **Private** |

> [!WARNING]
> **Important:** Since you already have a local project, do **NOT** check the boxes for README, `.gitignore`, or license — this prevents conflicts on your first push.

Click **Create repository**.

---

## 2️⃣ Copy Your Repository's URL

On the new repo page → click **Code** → select **SSH** or **HTTPS** → copy the URL:

```
git@github.com:YOUR-USERNAME/YOUR-REPOSITORY.git
```

---

## 3️⃣ Link Your Local Project to GitHub

```bash
git remote add origin <PASTE-YOUR-REPOSITORY-URL>
```

Verify the link:

```bash
git remote -v
```

---

## 4️⃣ Push Your Work Online

```bash
git branch -M main          # ensure your branch is named "main"
git push -u origin main      # upload your commits
```

| Flag | Meaning |
|:---:|---|
| `-M` | Force-renames your branch to `main` |
| `-u` | "Upstream" — remembers this connection so future pushes are just `git push` |

> [!TIP]
> Once complete, refresh your GitHub page — your files are live!

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| GitHub repo (blank, no README) | Prevents merge conflicts on first push |
| `git remote add origin <url>` | Links your local repo to GitHub |
| `git remote -v` | Verifies the remote link |
| `git branch -M main` | Standardizes your default branch name |
| `git push -u origin main` | Uploads commits + remembers the connection |

---

### 🛠️ MLOps Perspective: Pushing Code to Trigger CI/CD
> [!IMPORTANT]
> `git push` is the primary trigger for MLOps automation:
> - **Continuous Integration (CI):** Pushing code triggers GitHub Actions to run unit tests on your Python code, lint it, and ensure your ML model compiles.
> - **Continuous Deployment (CD):** Pushing to the `main` branch can trigger an automatic deployment pipeline that packages your model into a Docker container and deploys it to a Kubernetes cluster via AWS or GCP.
> - A simple `git push` is how a model goes from your laptop to serving millions of users.

---

<div align="center">

⬅️ [Previous: Step 3 — Add & Commit Cycle](./03_add_commit_cycle.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 5 — Collaboration & Fetching](./05_collaboration_fetching.md)

</div>
