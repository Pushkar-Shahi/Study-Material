<div align="center">

# <span style="color:#F1C40F">🟨 Level 3 — Architecture & Task Lifecycle</span>

![Level](https://img.shields.io/badge/Level--3-F1C40F?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-How%20It%20All%20Runs-F1C40F?style=flat-square)

</div>

---

## 🏗️ Airflow's Core Architecture

| Component | Emoji | Role |
|-----------|-------|------|
| Web Server | 🖥️ | Provides the UI to monitor, trigger, and manage your DAGs — DAGs, tasks, logs, failures, execution history, dependencies, duration |
| Scheduler | ⏱️ | Determines **which task needs to run**; monitors all DAGs and schedules task instances |
| Executor | 🧮 | Determines **how** tasks are executed. Key options: **Local**, **Celery**, **Kubernetes** |
| Worker | 🛠️ | Actually executes tasks in distributed deployments |
| Metadata Database | 🗄️ | Stores Airflow's state — DAG status, task status, run history, connections, variables (commonly PostgreSQL or a MySQL-compatible system) |
| Data Engineer | 🧑‍💻 | Responsible for configuring the setup (database, executor) and authoring DAGs as Python files |

```
Airflow UI
   ↓
Scheduler
   ↓
Executor
   ↓
Worker(s)
   ↓
Metadata DB
```

---

## 🧠 Airflow's Most Important MLOps Architecture

A very useful mental model for ML work:

```
                AIRFLOW — Orchestration Layer
        ┌───────────────┼───────────────┐
   Data Pipeline    Training Pipeline   Deployment Pipeline
   S3 / GCS         MLflow              Kubernetes
   Spark            PyTorch             SageMaker
   dbt              XGBoost             Vertex AI
```

> ℹ️ **Interview-critical distinction:** Airflow is the **orchestrator**, not necessarily the execution engine.

---

## 🚫 Airflow Should NOT Do Everything

| ✗ Bad Architecture | ✓ Better Architecture |
|---------------------|--------------------------|
| Airflow Worker → Train 100 GB dataset → Train GPU model for 5 hours (inside the worker) | Airflow → Trigger training job → Kubernetes / SageMaker / Vertex AI → Training → Store model → Airflow continues |

> ✅ **Rule of thumb:** Airflow coordinates the process. Specialized systems perform the heavy work.

---

## ⏱️ Important: Airflow Is Not a Real-Time System

| ✗ Not Ideal — Real-Time Serving | ✓ Good Use — Nightly Batch |
|-----------------------------------|-------------------------------|
| User request → Airflow → Prediction → Response | Collect data → Train model → Evaluate model → Deploy |

Airflow is generally designed for **batch workflow orchestration**. For real-time inference, use an inference service such as **FastAPI, KServe, Seldon, SageMaker Endpoint, or Vertex AI Endpoint**.

> 💡 **Tip:** Airflow can orchestrate the *deployment* of those real-time services — it just shouldn't sit in the live request path itself.

---

## 🎨 Task Lifecycle Stages

Tasks are visually represented by **colors** in the Airflow UI as they move through these stages:

| Stage | Meaning |
|-------|---------|
| No Status | The scheduler has created an empty task instance |
| Scheduled | The scheduler determines the task is ready to run |
| Queued | The executor places the task into a queue for an available worker |
| Running | A worker picks up the task and begins execution |
| Success / Failed / Shutdown | Final outcomes — finished correctly, crashed, or manually stopped |

### 🔁 Non-Standard States

| State | When It Happens |
|-------|------------------|
| Up for Retry | Task failed but has retries remaining — waits to be rescheduled |
| Upstream Failed | Task can't run because a task it depends on failed |
| Up for Reschedule | Used mainly for **sensors** waiting for a condition (like a file appearing) |

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| Scheduler / Webserver / Executor / Worker / Metadata DB | The five core architecture components |
| Orchestration layer | Airflow's role — coordinating Data/Training/Deployment pipelines, not running them |
| "Airflow should not do everything" | Offload heavy compute (GPU training) to Kubernetes/SageMaker/Vertex AI |
| Not a real-time system | Airflow = batch orchestration; use FastAPI/KServe/etc. for live inference |
| Queued → Running → Success/Failed | The standard task lifecycle path |

---

⬅️ [Previous: Installation & Setup](02_installation_setup.md) | [🏠 Roadmap](00_README.md) | ➡️ [Next: Building DAGs](04_building_dags.md)
