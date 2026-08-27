<div align="center">

# <span style="color:#008B8B">🩵 Reference — Git Commands Cheat Sheet</span>

![Reference](https://img.shields.io/badge/Type-Reference-008B8B) ![Theme](https://img.shields.io/badge/Theme-Teal_%E2%80%94_Full_Command_Index-008B8B)

</div>

---

## 🛠️ Setup & Initialization

| Command | Description |
|---|---|
| `git config` | Sets your Git identity and preferences |
| `git init` | Creates a new Git repository in the current folder |
| `git clone` | Downloads a remote repository to your machine |

---

## 📸 Snapshotting (Status, Stage, Save)

| Command | Description |
|---|---|
| `git status` | Shows changed, staged, and untracked files |
| `git add` | Stages files for the next commit |
| `git commit` | Saves staged changes as a snapshot |

---

## ☁️ Syncing With a Remote

| Command | Description |
|---|---|
| `git push` | Uploads local commits to GitHub |
| `git pull` | Fetches and merges changes from GitHub |
| `git fetch` | Downloads remote updates **without** merging them |
| `git remote` | Manages remote repository connections |
| `git remote -v` | Shows remote URLs for fetch and push |

> [!TIP]
> `git fetch` vs `git pull`: `fetch` downloads updates but leaves your local branch untouched; `pull` = `fetch` + `merge` in one step.

---

## 🌿 Branching & Merging

| Command | Description |
|---|---|
| `git branch` | Lists, creates, or deletes branches |
| `git switch` | Moves to another branch |
| `git checkout` | Older command for switching branches or restoring files |
| `git merge` | Combines one branch into another |
| `git rebase` | Rewrites commits onto a new base branch |

> [!WARNING]
> `git switch` is the modern, safer replacement for `git checkout` when changing branches.

---

## 🔍 Inspecting History

| Command | Description |
|---|---|
| `git log` | Shows commit history |
| `git diff` | Shows line-by-line differences in files or commits |
| `git show` | Displays details of a commit, tag, or object |
| `git blame` | Shows who last changed each line of a file |
| `git reflog` | Shows where `HEAD` has pointed recently |
| `git bisect` | Helps find the commit that introduced a bug |

---

## ⏪ Undoing Changes

| Command | Description |
|---|---|
| `git restore` | Restores files from the index or a commit |
| `git reset` | Moves `HEAD` and optionally un-stages or removes commits |
| `git revert` | Creates a **new** commit that undoes a previous commit |
| `git stash` | Temporarily saves unfinished changes |

> [!WARNING]
> **Safety note:** `git reset` can rewrite history (risky on shared branches). `git revert` is the safer choice for undoing changes that are already pushed.

---

## ⚡ Advanced & Maintenance

| Command | Description |
|---|---|
| `git tag` | Marks important commits, usually for releases |
| `git cherry-pick` | Applies a specific commit onto the current branch |
| `git submodule` | Manages nested Git repositories |
| `git gc` | Cleans and optimizes the repository |

---

## 📝 Quick Category Index

| Category | Commands |
|---|---|
| 🛠️ Setup | `config`, `init`, `clone` |
| 📸 Snapshot | `status`, `add`, `commit` |
| ☁️ Sync | `push`, `pull`, `fetch`, `remote` |
| 🌿 Branching | `branch`, `switch`, `checkout`, `merge`, `rebase` |
| 🔍 Inspect | `log`, `diff`, `show`, `blame`, `reflog`, `bisect` |
| ⏪ Undo | `restore`, `reset`, `revert`, `stash` |
| ⚡ Advanced | `tag`, `cherry-pick`, `submodule`, `gc` |

---

### 🛠️ MLOps Perspective: Advanced Git Commands
> [!NOTE]
> MLOps engineers often rely on the Advanced/Undo commands when things break:
> - `git bisect` is magic for ML debugging. If your model suddenly starts failing to converge, but you don't know which code change caused it over the last 50 commits, `git bisect` will do a binary search through your commit history to find the exact commit that broke the training loop.
> - `git revert` is how you safely roll back a bad model deployment if an unexpected bug makes it to production.

---

<div align="center">

⬅️ [Previous: Step 6 — SSH Authentication](./06_ssh_authentication.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: GitHub CLI Reference](./08_github_cli_reference.md)

</div>
