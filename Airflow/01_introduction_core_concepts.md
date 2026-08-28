<div align="center">

# <span style="color:#2ECC71">🟩 Level 1 — Introduction & Core Concepts</span>

![Level](https://img.shields.io/badge/Level--1-2ECC71?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Foundations-2ECC71?style=flat-square)

</div>

---

## 📖 What Is Apache Airflow?

Apache Airflow is a **popular open-source workflow management platform written in Python**, used for **authoring, scheduling, and monitoring workflows**.

- 🍼 It began in **2014** as an internal tool at **Airbnb** to manage increasingly complex workflows.
- 🏛️ It became a **Top-Level Apache Software Foundation project in 2019**.

> ⭐ **The key idea:** Airflow orchestrates **when** and in **what order** your ML/data tasks run. It does **not** primarily perform the ML work itself.

---

## 🧩 The Core Building Blocks

| Concept | Emoji | Definition |
|---------|-------|------------|
| DAG (Directed Acyclic Graph) | 🕸️ | A collection of all the tasks you want to run, organized to show their relationships and dependencies. "Acyclic" means the workflow **cannot circle back** to a previous task |
| Task | 🧱 | Defines a specific unit of work within a DAG (e.g., fetching data) |
| Operator | ⚙️ | Determines **what actually gets done** — e.g., running a Bash command or a Python function |
| DAG Run | ▶️ | An **instantiation** of a workflow for a specific point in time (the execution date) |
| Task Instance | 🔹 | The run of a **specific task** within a given DAG Run |

---

## 🤖 Why MLOps Engineers Need Airflow

A typical ML project eventually becomes more than a single line:

```python
model.fit(X, y)
```

You need **automation**. For example, a daily retraining job:

```
Every day at 2 AM (trigger)
   ↓ Download new data
   ↓ Validate data
   ↓ Generate features
   ↓ Train model
   ↓ Evaluate model
   ↓ If accuracy > threshold (quality gate)
   ↓ Register model
   ↓ Deploy
```

Airflow can orchestrate this entire workflow, giving you: **scheduling, task dependencies, retries, logging, monitoring, failure handling, backfilling, parameterization, workflow visualization, cloud integrations, and ML platform integrations.**

### 🔁 The Typical ML Lifecycle Airflow Coordinates

```
Raw Data → Data Validation → Feature Engineering → Model Training
   → Model Evaluation → Model Registration → Deployment
   → Monitoring → Retraining
```

---

## 🔀 XComs & TaskFlow API (Preview)

Two concepts you'll use constantly, introduced here and covered in depth later:

- **XComs** ("cross-communications") — allow tasks to share small amounts of data → *full details in [Level 5](05_data_sharing_scheduling.md)*
- **TaskFlow API** — uses Python decorators to simplify DAG creation → *full details in [Level 4](04_building_dags.md)*

> 💡 **Tip:** Keep DAG vs. Task vs. Operator straight — a **DAG** is the whole workflow map, a **Task** is one node on that map, and an **Operator** is the template that defines what that node actually executes.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| Airflow | Open-source, Python-based platform for authoring, scheduling & monitoring workflows |
| DAG | The workflow — tasks + their dependencies, never circles back |
| Task | A single unit of work |
| Operator | Defines what a task actually does (Bash, Python, Kubernetes, etc.) |
| DAG Run / Task Instance | One execution instance of a DAG / of a task within it |
| "Orchestrate, not execute" | Airflow decides *when/order*; specialized systems do the heavy lifting |

---

⬅️ Previous | [🏠 Roadmap](00_README.md) | ➡️ [Next: Installation & Setup](02_installation_setup.md)
