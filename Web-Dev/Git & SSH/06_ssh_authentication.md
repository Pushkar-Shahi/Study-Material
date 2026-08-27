<div align="center">

# <span style="color:#8E44AD">🟣 Step 6 — Secure Password-Free SSH Connections</span>

![Step](https://img.shields.io/badge/Step-6-8E44AD) ![Theme](https://img.shields.io/badge/Theme-Purple_%E2%80%94_Cryptographic_Auth-8E44AD)

</div>

---

## 🔑 What Is SSH and How Does It Work?

SSH uses a pair of cryptographic keys generated together:

| Key | Lives Where | Analogy |
|---|---|---|
| 🔐 **Private Key** (`id_ed25519`) | Strictly on your computer — never shared | A physical key in your pocket |
| 🔓 **Public Key** (`id_ed25519.pub`) | Uploaded to GitHub | The lock that matches your key |

> [!NOTE]
> Whenever your computer talks to GitHub, GitHub uses your public key to verify you hold the matching private key. If they match → **instant authentication**.

---

## 🍏 Option A: macOS SSH Setup

| Step | Command |
|:---:|---|
| 1️⃣ Open Terminal | `Cmd + Space` → type "Terminal" |
| 2️⃣ Check existing keys | `ls -al ~/.ssh` *(skip to step 5 if `id_ed25519` already exists)* |
| 3️⃣ Generate a new key | `ssh-keygen -t ed25519 -C "your-email@example.com"` |
| 4️⃣ Start the SSH agent | `eval "$(ssh-agent -s)"` |
| ➕ Add key to keychain | `ssh-add --apple-use-keychain ~/.ssh/id_ed25519` |
| 5️⃣ Copy public key | `pbcopy < ~/.ssh/id_ed25519.pub` |

> [!TIP]
> Press Enter to accept the default file location. You can set a passphrase, or press Enter twice to leave it empty.
> If you skipped the passphrase, just run `ssh-add ~/.ssh/id_ed25519` instead of the keychain command.

---

## 🪟 Option B: Windows SSH Setup

| Step | Command |
|:---:|---|
| 1️⃣ Open Git Bash | — |
| 2️⃣ Check existing keys | `ls -al ~/.ssh` *(skip to step 5 if keys exist)* |
| 3️⃣ Generate a new key | `ssh-keygen -t ed25519 -C "your-email@example.com"` |
| 4️⃣ Enable SSH agent | Run PowerShell **as Administrator**: |
| | `Get-Service -Name ssh-agent \| Set-Service -StartupType Manual` |
| | `Start-Service ssh-agent` |
| ➕ Add your key | `ssh-add ~/.ssh/id_ed25519` |
| 5️⃣ Copy public key | `cat ~/.ssh/id_ed25519.pub \| clip` |

---

## 🌐 Adding Your Key to GitHub (Both Platforms)

| Step | Action |
|:---:|---|
| 1️⃣ | Log in to GitHub |
| 2️⃣ | Profile picture (top-right) → **Settings** |
| 3️⃣ | Sidebar → **SSH and GPG keys** |
| 4️⃣ | Click green **New SSH key** button |
| 5️⃣ | Give it a Title (e.g., "My MacBook") |
| 6️⃣ | Leave Key type as **Authentication Key** |
| 7️⃣ | Paste your copied key into the field |
| 8️⃣ | Click **Add SSH key** |

---

## ✅ Testing Your Connection

```bash
ssh -T git@github.com
```

- First time? Terminal will ask to continue → type `yes` and press Enter.
- Success looks like:
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Private key | Stays on your machine — never shared |
| Public key | Uploaded to GitHub — the "lock" |
| `ssh-keygen -t ed25519` | Generates a new key pair |
| `ssh-add` | Registers your key with the SSH agent |
| GitHub → SSH and GPG keys | Where you paste your public key |
| `ssh -T git@github.com` | Tests that authentication works |

---

### 🛠️ MLOps Perspective: SSH Keys to Access Remote GPUs
> [!IMPORTANT]
> The exact same SSH keys you generate to talk to GitHub are used to connect to remote ML servers:
> - You cannot train a 70B parameter LLM on your laptop; you need a cluster of GPUs on AWS (EC2) or Google Cloud (Compute Engine).
> - You don't use passwords to log into these servers — you use SSH.
> - When you launch an EC2 instance, you inject your `id_ed25519.pub` public key into the server. Then, you use `ssh ubuntu@<ip-address>` to securely log in and start training your models.

---

<div align="center">

⬅️ [Previous: Step 5 — Collaboration & Fetching](./05_collaboration_fetching.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Git Commands Reference](./07_git_commands_reference.md)

### 🎉 You've completed the core Git & GitHub Roadmap!
*Two command-reference cheat sheets follow for quick lookup.*

</div>
