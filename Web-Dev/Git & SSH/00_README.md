<div align="center">

# 🐙 Git & GitHub Learning Roadmap
### *From Local Commits to Secure Remote Collaboration*

![Progress](https://img.shields.io/badge/Steps_Covered-8-blue) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen) ![Focus](https://img.shields.io/badge/Focus-Version_Control-F05032?logo=git&logoColor=white)

</div>

---

## 📍 Progress Map

| # | Step | Focus | File | Status |
|---|-------|-------|------|:---:|
| 1️⃣ | 🟢 **Configuration** | `git config`, Setting identity | [`01_configuration.md`](./01_configuration.md) | ✅ |
| 2️⃣ | 🔵 **Local Repository** | `git init`, The `.git` folder | [`02_local_repository.md`](./02_local_repository.md) | ✅ |
| 3️⃣ | 🟡 **Add & Commit Cycle** | `status`, `add`, `commit` | [`03_add_commit_cycle.md`](./03_add_commit_cycle.md) | ✅ |
| 4️⃣ | 🟠 **Connecting to GitHub** | `remote`, `branch`, `push` | [`04_connecting_to_github.md`](./04_connecting_to_github.md) | ✅ |
| 5️⃣ | 🔴 **Collaboration & Fetching** | `clone`, `pull`, Best practices | [`05_collaboration_fetching.md`](./05_collaboration_fetching.md) | ✅ |
| 6️⃣ | 🟣 **SSH Authentication** | Generating keys, Secure connections | [`06_ssh_authentication.md`](./06_ssh_authentication.md) | ✅ |
| 7️⃣ | 🩵 **Git Commands Reference** | Full cheat sheet of commands | [`07_git_commands_reference.md`](./07_git_commands_reference.md) | ✅ |
| 8️⃣ | 💜 **GitHub CLI Reference** | `gh` CLI commands | [`08_github_cli_reference.md`](./08_github_cli_reference.md) | ✅ |

---

## 📖 The Daily Workflow Quick-Look

```bash
git pull                          # 1. Download the latest changes
[make your edits]                 # 2. Write your code
git add .                         # 3. Stage your changes
git commit -m "describe changes"  # 4. Save a local snapshot
git push                          # 5. Upload to GitHub
```

---

### 🛠️ MLOps Perspective: Why Git is Mandatory
> [!IMPORTANT]
> Version control is the absolute baseline of MLOps. If you aren't tracking your code, you don't have a pipeline.
> - **Reproducibility:** You must be able to recreate exactly what code generated a specific ML model version. Git provides that history.
> - **Data & Models:** While Git handles code, tools like DVC (Data Version Control) extend Git to track huge datasets and model weights using identical commands (`dvc add`, `dvc commit`).
> - **CI/CD:** Pushing code to GitHub is the trigger for automated model training, testing, and deployment via GitHub Actions or GitLab CI.

---

<div align="center">

### 🎉 Roadmap Complete!
*From a plain folder to a fully version-controlled, securely-authenticated GitHub workflow.*

</div>
