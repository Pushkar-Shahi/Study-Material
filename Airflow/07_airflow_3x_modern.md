<div align="center">

# <span style="color:#8B5E3C">🟫 Level 7 — Airflow 3.x & Modern Capabilities</span>

![Level](https://img.shields.io/badge/Level--7-8B5E3C?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Beyond%20Traditional%20ETL-8B5E3C?style=flat-square)

</div>

---

## 🚀 What Is Airflow 3.x?

Airflow 3.x is the latest evolution of the platform, expanding beyond traditional batch-oriented data pipelines to handle **modern AI and machine learning workloads**.

| Feature | What It Adds |
|---------|---------------|
| AI & LLM Orchestration | A growing set of providers for orchestrating AI and agentic tools alongside standard pipelines |
| Modern Workloads | Support for LLM-based workloads, model training, and event-triggered batch pipelines |
| Public Interface (3.0+) | A refined interface letting you extend/adapt nearly every part of the system — including execution logic and UI plugins |
| Task SDK (`airflow.sdk`) | A standalone SDK for improved developer experience when authoring tasks — used throughout this guide to define DAGs (`from airflow.sdk import DAG`) |

Despite these advancements, Airflow 3.x maintains the **"workflows as code"** philosophy: version control, testing, and dynamic pipeline generation.

---

## 🔧 What Changed From Airflow 2.x (Practical Import Guide)

> ⚠️ **Version note:** Some tutorials online still use Airflow 2.x imports — the concepts are similar, but public APIs and provider imports have changed. When in doubt, follow the docs matching your installed version.

| Concept | Airflow 2.x style | Airflow 3.x style |
|---------|--------------------|---------------------|
| DAG object | `from airflow import DAG` | `from airflow.sdk import DAG` |
| PythonOperator | `from airflow.operators.python import PythonOperator` | `from airflow.providers.standard.operators.python import PythonOperator` |
| BashOperator | `from airflow.operators.bash import BashOperator` | `from airflow.providers.standard.operators.bash import BashOperator` |
| Scheduling param | `schedule_interval="@daily"` | `schedule="@daily"` |
| `start_date` | Sometimes left as a placeholder in tutorials | Must be a real, timezone-aware `pendulum.datetime(...)` |

---

## 🤖 How Are AI Tools Integrated?

- **Support for modern workloads:** develop, schedule, and monitor LLM-based and agentic workloads, plus ML/model-training tasks.
- **Extensible framework:** because Airflow is an extensible Python framework, you can connect workflows to virtually any AI technology or external service.
- **Public Interface for 3.0+:** adapts nearly every part of the system — including execution logic and UI plugins — to fit AI-specific needs.

---

## 📝 "Workflows as Code" Advantages

Defining pipelines in Python (rather than a "drag-and-drop" platform) enables:

- ✅ Version control
- ✅ Unit testing
- ✅ Easier team collaboration

---

## 🔔 Other Advanced & Operational Notes

| Topic | Detail |
|-------|--------|
| Callbacks | A DAG feature — specific actions (like notifications) that trigger when a workflow completes |
| Clean Environment Management | `NamedTemporaryFile` ensures files are auto-deleted after upload to S3, keeping your server uncluttered |
| Volume Cleanup | `docker-compose down -v` removes not just containers, but also the associated **data volumes** |

```bash
# Tears down containers AND deletes their data volumes
docker-compose down -v
```

> ⚠️ **Gotcha:** `docker-compose down -v` deletes your data volumes too — don't run this if you want to keep your local database contents.

---

## 🎁 Course Bonus

The original tutorial's creator offered two bonus videos tied to engagement milestones:

| Milestone | Bonus Content |
|-----------|----------------|
| 1,000 Likes | A video explaining how to debug Airflow DAGs |
| 5,000 Likes | A video specifically about the Airflow Docker operator |

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| Airflow 3.x | Expands Airflow into AI/LLM/agentic workload orchestration |
| `airflow.sdk` | The 3.x public SDK for defining DAGs |
| `airflow.providers.standard...` | Where standard operators (Python, Bash, etc.) now live |
| Task SDK | Standalone SDK for authoring tasks (Airflow 3.x) |
| Callbacks | Trigger actions (e.g. notifications) on workflow completion |
| `docker-compose down -v` | Removes containers **and** their data volumes |

---

⬅️ [Previous: Connections, Variables & Sensors](06_connections_hooks.md) | [🏠 Roadmap](00_README.md) | ➡️ [Next: MLOps Production Patterns](08_mlops_production_patterns.md)
