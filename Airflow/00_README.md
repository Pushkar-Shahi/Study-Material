<div align="center">

# 🌬️ Apache Airflow — Complete Learning Roadmap (incl. MLOps Edition)

### *From "what is a DAG?" to running production ML pipelines with quality gates, monitoring, and retraining loops*

![Progress](https://img.shields.io/badge/Progress-10%2F10%20Levels-2ECC71?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Airflow%203.x%20%7C%20Python%20%7C%20Docker%20%7C%20K8s-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## ⚠️ Version Note

These docs blend a general Airflow 2.0 tutorial with an **Airflow 3.x, error-fixed MLOps reference**. Where the two sources disagreed (imports, `start_date`, DAG parameter names), the **3.x-aligned version wins** and is called out in a callout box. Key corrections baked in throughout:

- ✅ Real, timezone-aware `pendulum` dates instead of placeholder `start_date=...`
- ✅ Airflow 3.x public SDK imports (`airflow.sdk`) and provider-package imports (`airflow.providers.standard...`) instead of old `airflow.operators.*` paths
- ✅ Complete branching example (`BranchPythonOperator` + both downstream tasks)
- ✅ XCom clarified as small-values-only, never large datasets or model artifacts
- ✅ Airflow clarified as an **orchestrator**, not a training engine or real-time serving system
- ✅ Catchup / logical dates / data intervals clarified to avoid a common misconception

---

## 🗺️ Progress Map

| # | Level | Focus | File | Status |
|---|-------|-------|------|--------|
| 1 | 🟩 Introduction & Core Concepts | History, DAGs, Tasks, Operators, why MLOps needs Airflow | [01_introduction_core_concepts.md](01_introduction_core_concepts.md) | ✅ |
| 2 | 🟦 Installation & Setup | Python env, Docker, package installs, permissions, executors | [02_installation_setup.md](02_installation_setup.md) | ✅ |
| 3 | 🟨 Architecture & Task Lifecycle | Components, task states, the MLOps architecture mental model | [03_architecture_task_lifecycle.md](03_architecture_task_lifecycle.md) | ✅ |
| 4 | 🟧 Building DAGs | BashOperator, PythonOperator, KubernetesPodOperator, TaskFlow, branching | [04_building_dags.md](04_building_dags.md) | ✅ |
| 5 | 🟥 Data Sharing & Scheduling | XComs, Cron, Catchup & Backfill, Dataset scheduling | [05_data_sharing_scheduling.md](05_data_sharing_scheduling.md) | ✅ |
| 6 | 🟪 Connections, Variables & Sensors | Postgres/S3 connections, hooks, Variables, Sensors, an ETL pipeline | [06_connections_hooks.md](06_connections_hooks.md) | ✅ |
| 7 | 🟫 Airflow 3.x & Modern Capabilities | AI/LLM orchestration, Task SDK, public interface, callbacks | [07_airflow_3x_modern.md](07_airflow_3x_modern.md) | ✅ |
| 8 | 🟦 MLOps Production Patterns | Idempotency, Pools, Deferrable Operators, validation, monitoring, alerts | [08_mlops_production_patterns.md](08_mlops_production_patterns.md) | ✅ |
| 9 | 🩷 Ecosystem Integrations | Airflow + MLflow, Docker, Kubernetes, Cloud, CI/CD | [09_ecosystem_integrations.md](09_ecosystem_integrations.md) | ✅ |
| 10 | ⬛ Comparisons, Roadmap & Reference | vs Jenkins/Kubeflow/Prefect, terminology, interview prep, error checklist | [10_comparisons_reference.md](10_comparisons_reference.md) | ✅ |

---

## 🎨 Quick-Reference Cheat Sheet

| Color | Level | Key Terms / Keywords |
|-------|-------|-----------------------|
| 🟩 Green | Introduction & Core Concepts | DAG, Task, Operator, DAG Run, Task Instance, "orchestrate, not execute" |
| 🟦 Blue | Installation & Setup | `venv`, `AIRFLOW_HOME`, `docker-compose up -d`, `AIRFLOW_UID`/`AIRFLOW_GID`, CeleryExecutor, LocalExecutor |
| 🟨 Yellow | Architecture & Task Lifecycle | Scheduler, Webserver, Metadata DB, Executor, Worker, "not a real-time system" |
| 🟧 Orange | Building DAGs | `BashOperator`, `PythonOperator`, `KubernetesPodOperator`, `@dag`, `@task`, `BranchPythonOperator` |
| 🟥 Red | Data Sharing & Scheduling | XCom, `xcom_push`/`xcom_pull`, 48 KB limit, `schedule`, `catchup`, `backfill`, Datasets |
| 🟪 Purple | Connections, Variables & Sensors | `postgres_conn_id`, `PostgresHook`, `S3Hook`, Variables, Sensors, Secrets Backend |
| 🟫 Brown | Airflow 3.x & Modern | `airflow.sdk`, provider packages, Task SDK, AI/agentic orchestration |
| 🟦 Teal | MLOps Production Patterns | Idempotency, retries, Pools, Deferrable Operators, data/model validation, drift |
| 🩷 Pink | Ecosystem Integrations | MLflow, Docker, KubernetesPodOperator, AWS/GCP/Azure, CI/CD |
| ⬛ Slate | Comparisons, Roadmap & Reference | Jenkins, Kubeflow, Prefect/Dagster, terminology, interview questions |

---

> 💡 **How to use this roadmap:** Levels 1–7 are the general Airflow foundation; Levels 8–10 are the MLOps-specific deep dive. If you already know Airflow basics, jump straight to [08_mlops_production_patterns.md](08_mlops_production_patterns.md).
