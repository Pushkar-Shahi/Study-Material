<div align="center">

# <span style="color:#2E8B57">🟢 Step 1 — Introducing Yourself to Git (Configuration)</span>

![Step](https://img.shields.io/badge/Step-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Identity_Setup-2E8B57)

</div>

---

## ❓ Why Configure Git First?

Before Git tracks your files, it needs to know **who** is making the changes so it can label your work correctly. This is called setting your **commit identity**.

> [!NOTE]
> You only need to do this **once per computer**.

---

## 🛠️ The Two Setup Commands

Run these in your terminal (macOS) or Git Bash (Windows):

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

| Command | Sets |
|---|---|
| `user.name` | The name attached to your commits |
| `user.email` | The email attached to your commits |

> [!TIP]
> Use the **same email** you used to sign up for your GitHub account.

---

## ✅ Verify Your Setup

```bash
git config --global --list
```

This displays your saved configuration so you can confirm it stuck.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `git config --global user.name` | Attaches your name to every commit |
| `git config --global user.email` | Attaches your email to every commit |
| `git config --global --list` | Verifies your saved configuration |
| One-time setup | Only needs to be done once per machine |

---

### 🛠️ MLOps Perspective: Auditing & Blame
> [!NOTE]
> Setting your Git identity is critical in corporate ML environments:
> - **Auditing:** If a data scientist introduces a bug in a PyTorch training loop, teams use `git blame` to see exactly who made the change and when.
> - **Cloud Instances:** When training models on AWS EC2 or GCP Compute Engine, you will often need to set up `git config` on those remote servers before pushing logs or automated code updates.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Step 2 — Local Repository](./02_local_repository.md)

</div>
