<div align="center">

# <span style="color:#6E5494">💜 Reference — GitHub CLI (`gh`) Cheat Sheet</span>

![Reference](https://img.shields.io/badge/Type-Reference-6E5494) ![Theme](https://img.shields.io/badge/Theme-Purple_Grey_%E2%80%94_gh_CLI-6E5494)

</div>

---

## 🔐 Authentication

| Command | Description |
|---|---|
| `gh auth login` | Signs in to GitHub from the terminal |
| `gh auth status` | Checks whether you are logged in |
| `gh auth logout` | Signs out of GitHub CLI |

---

## 📁 Repositories

| Command | Description |
|---|---|
| `gh repo create` | Creates a new GitHub repository |
| `gh repo clone` | Clones a GitHub repo using the CLI |
| `gh repo view` | Opens repository details in terminal or browser |
| `gh repo fork` | Creates your own fork of a repository |

---

## 🐛 Issues

| Command | Description |
|---|---|
| `gh issue create` | Creates a new issue |
| `gh issue list` | Lists issues in a repository |
| `gh issue view` | Shows a specific issue |
| `gh issue close` | Closes an issue |
| `gh issue comment` | Adds a comment to an issue |

---

## 🔀 Pull Requests

| Command | Description |
|---|---|
| `gh pr create` | Opens a pull request |
| `gh pr list` | Lists pull requests |
| `gh pr view` | Shows pull request details |
| `gh pr checkout` | Checks out a pull request branch locally |
| `gh pr merge` | Merges a pull request |
| `gh pr close` | Closes a pull request without merging |
| `gh pr review` | Submits a review on a pull request |
| `gh pr comment` | Adds a comment to a pull request |

---

## 📦 Releases

| Command | Description |
|---|---|
| `gh release create` | Creates a new GitHub release |
| `gh release list` | Lists releases |
| `gh release view` | Shows release details |

---

## 📝 Gists

| Command | Description |
|---|---|
| `gh gist create` | Creates a GitHub Gist |
| `gh gist list` | Lists your gists |
| `gh gist view` | Shows a gist |

---

## 🔍 Search

| Command | Description |
|---|---|
| `gh search issues` | Searches issues on GitHub |
| `gh search prs` | Searches pull requests |
| `gh search repos` | Searches repositories |
| `gh search code` | Searches code on GitHub |

---

## 🤖 GitHub Actions (Workflows & Runs)

| Command | Description |
|---|---|
| `gh workflow list` | Lists GitHub Actions workflows |
| `gh workflow run` | Runs a workflow manually |
| `gh workflow view` | Shows a workflow |
| `gh run list` | Lists GitHub Actions runs |
| `gh run view` | Shows a specific run |
| `gh run watch` | Watches a workflow run live |

---

## ⚙️ Extensions, Aliases & API

| Command | Description |
|---|---|
| `gh alias set` | Creates your own shortcut command |
| `gh extension install` | Installs a GitHub CLI extension |
| `gh api` | Calls the GitHub API from terminal |

---

## 📝 Quick Category Index

| Category | Commands |
|---|---|
| 🔐 Auth | `login`, `status`, `logout` |
| 📁 Repos | `create`, `clone`, `view`, `fork` |
| 🐛 Issues | `create`, `list`, `view`, `close`, `comment` |
| 🔀 PRs | `create`, `list`, `view`, `checkout`, `merge`, `close`, `review`, `comment` |
| 📦 Releases | `create`, `list`, `view` |
| 📝 Gists | `create`, `list`, `view` |
| 🔍 Search | `issues`, `prs`, `repos`, `code` |
| 🤖 Actions | `workflow list/run/view`, `run list/view/watch` |
| ⚙️ Power tools | `alias set`, `extension install`, `api` |

> [!TIP]
> All `gh` commands follow the pattern `gh <noun> <verb>` — e.g., `gh pr create`, `gh issue list` — making them easy to guess once you know the resource type.

---

### 🛠️ MLOps Perspective: Automating with the `gh` CLI
> [!IMPORTANT]
> The `gh` CLI is a superpower for MLOps engineers who write automation scripts (bash/Python):
> - **Triggering Training Pipelines:** You can write a bash script that uses `gh workflow run` to manually trigger a heavy GPU model training pipeline on AWS when a specific event occurs (e.g., when new data arrives in S3).
> - **Automated Reporting:** You can use `gh issue create` to automatically open a GitHub issue if a scheduled ML model starts showing data drift or failing performance metrics.
> - **Model Releases:** When a model is approved for production, a script can run `gh release create` to tag the exact code commit and upload the model weights as release assets.

---

<div align="center">

⬅️ [Previous: Git Commands Reference](./07_git_commands_reference.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 Full Git & GitHub Roadmap + Command References Complete!

</div>
