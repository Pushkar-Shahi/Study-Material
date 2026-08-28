<div align="center">

# <span style="color:#3498DB">🟦 Level 2 — Installation & Setup</span>

![Level](https://img.shields.io/badge/Level--2-3498DB?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Python%20Env%20%26%20Docker-3498DB?style=flat-square)

</div>

---

## 🆚 Two Ways to Run Airflow

| Method | Best For | Isolation |
|--------|----------|-----------|
| 🐍 Python Virtual Environment | Quick local testing, learning the CLI | Process-level (venv) |
| 🐳 Docker | Reproducible environments, avoiding "works on my machine" issues | Full container isolation |

---

## 🐍 A. Run Airflow in a Python Environment

| Step | Action |
|------|--------|
| 1 | Ensure Python **3.6+** |
| 2 | Create a project folder & virtual environment |
| 3 | Install Airflow via pip (match constraints to your Python version) |
| 4 | Set `AIRFLOW_HOME` and run `airflow db init` |
| 5 | Create an admin user, then start the webserver + scheduler |

```bash
# 1–2: Prepare environment
python3 -m venv py_env
source py_env/bin/activate

# 3: Install Airflow (match constraints file to your Python version)
pip install apache-airflow

# 4: Initialize database
export AIRFLOW_HOME=$(pwd)
airflow db init

# 5: Create user, then run these in SEPARATE terminals
airflow users create
airflow webserver -p 8080
airflow scheduler
```

Once both services are running, access the UI at **`localhost:8080`**.

> ⚠️ **Gotcha:** If you hit install errors, you may need system tools like `gcc` or the macOS Command Line Tools.

---

## 🐳 B. Run Airflow in Docker

| Step | Action |
|------|--------|
| 1 | Install Docker Desktop (includes Docker Compose); verify with `docker --version` |
| 2 | Create a project folder & download the official `docker-compose.yaml` |
| 3 | Create `dags`, `logs`, and `plugins` folders |
| 4 | Run `docker-compose up airflow-init` (sets up DB + default admin user `airflow`/`airflow`) |
| 5 | Launch in detached mode: `docker-compose up -d` |
| 6 | Access UI at `0.0.0.0:8080` or `localhost:8080` |

```bash
docker --version
mkdir dags logs plugins
docker-compose up airflow-init
docker-compose up -d
```

`docker-compose up -d` runs the webserver, scheduler, **and a Postgres database** as containers.

> 💡 **Tip:** Docker is often preferred because it solves the "it works on my machine" problem by keeping the environment fully isolated.

---

## 📦 C. Installing Python Packages in Docker (2 Ways)

| Method | When to Use |
|--------|-------------|
| Extending the official image | ✅ Recommended for **99% of use cases** — fast and easy |
| Customizing the image from source | Only if you need deep build control or to optimize image size |

**1. Extending the official image**

```dockerfile
# Dockerfile
FROM apache/airflow
COPY requirements.txt .
RUN pip install -r requirements.txt
```

```bash
docker build -t my-airflow-image .
# then point docker-compose.yaml to this new local image
```

**2. Customizing the image**

- Clone the official Airflow GitHub repository
- Place `requirements.txt` inside the repo's `docker-context-files` folder
- Build from the root directory — Airflow automatically detects and installs the dependencies

---

## 🔐 D. Linux Permissions

If running Airflow in Docker **on Linux**, set `AIRFLOW_UID` and `AIRFLOW_GID` in a `.env` file so the container has correct permissions to access your local folders.

```ini
# .env
AIRFLOW_UID=50000
AIRFLOW_GID=0
```

---

## ⚙️ E. Executor Types

| Executor | Notes |
|----------|-------|
| CeleryExecutor | Default in the official `docker-compose.yaml` |
| LocalExecutor | Recommended for **simpler local environments** |
| KubernetesExecutor | Important for MLOps deployments — see [Level 9](09_ecosystem_integrations.md) |

> ⚠️ **Gotcha:** The official Docker setup defaults to CeleryExecutor, which is more than most local/learning environments need — consider switching to LocalExecutor.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| `venv` / `AIRFLOW_HOME` | Isolated Python setup for a local install |
| `docker-compose up airflow-init` | Initializes DB + creates default admin user |
| `docker-compose up -d` | Launches webserver, scheduler, Postgres as containers |
| Extending the image | Recommended way to add Python packages in Docker |
| `AIRFLOW_UID` / `AIRFLOW_GID` | Required on Linux for correct folder permissions |
| CeleryExecutor / LocalExecutor / KubernetesExecutor | Task execution backends |

---

⬅️ [Previous: Introduction & Core Concepts](01_introduction_core_concepts.md) | [🏠 Roadmap](00_README.md) | ➡️ [Next: Architecture & Task Lifecycle](03_architecture_task_lifecycle.md)
