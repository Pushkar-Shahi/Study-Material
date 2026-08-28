<div align="center">

# <span style="color:#34495E">⬛ Level 10 — Comparisons, Roadmap & Reference</span>

![Level](https://img.shields.io/badge/Level--10-34495E?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Study%20Guide%20%26%20Interview%20Prep-34495E?style=flat-square)

</div>

---

## 🆚 Airflow vs Jenkins

| Jenkins | Airflow |
|---------|---------|
| Primarily: CI/CD | Primarily: Workflow orchestration |

```
Git → Jenkins/GitHub Actions → Deploy Airflow DAG → Airflow → Run ML pipeline
```

> ⚠️ **Common misconception:** Don't think of Airflow as simply "Jenkins for data." They solve different problems and often work together.

---

## 🆚 Airflow vs Kubeflow

| Airflow | Kubeflow |
|---------|----------|
| General workflow orchestration (Data → Train → Evaluate → Deploy) | Focused on ML workflows / platform capabilities on Kubernetes |

> ⭐ **Not competitors:** A company can use both — Airflow can trigger and coordinate a Kubeflow pipeline as one step in a larger workflow.

---

## 🆚 Airflow vs MLflow

- **Airflow** → *"When/how should this workflow run?"*
- **MLflow** → *"What happened during the ML experiment / model lifecycle?"*

---

## 🆚 Airflow vs Prefect/Dagster

Airflow, Prefect, and Dagster can all be used for workflow orchestration.

> ℹ️ **Where Airflow stands out:** Airflow has particularly strong adoption in data engineering and a mature ecosystem of integrations. For interviews, focus deeply on Airflow rather than trying to master every orchestrator.

---

## 🏗️ The MLOps Stack You Should Understand

```
Git → CI/CD → AIRFLOW
                 ├── Data (S3)
                 ├── Train (K8s / GPU)
                 └── Evaluate (MLflow)
        → Model Registry → Deployment → Monitoring → Drift
        → Airflow (Retraining) → ...loop
```

> ⭐ **Why this matters:** If you understand this architecture, you're learning Airflow **as an MLOps engineer**, rather than just as a scheduler.

---

## 📚 Important Airflow Terminology

Learn these terms properly — you don't need to memorize definitions mechanically, but you should understand how they work together:

`DAG` · `Task` · `Task Instance` · `DAG Run` · `Operator` · `Sensor` · `Scheduler` · `Executor` · `Worker` · `Metadata Database` · `XCom` · `Variable` · `Connection` · `Pool` · `Trigger Rule` · `TaskFlow API` · `Backfill` · `Catchup` · `Retries` · `SLA / deadlines` · `Dataset` · `Deferrable Operator`

---

## 🗓️ Your Practical Learning Roadmap

**By concept level:**

| Level | Topics | Practice |
|-------|--------|----------|
| 1 — Fundamentals | DAG, Task, Operator, Scheduler, Executor, Worker, Metadata DB, Airflow UI | Build: `task1 → task2 → task3` |
| 2 — Workflow Concepts | Dependencies, Retries, Catchup, Backfill, XCom, Variables, Connections, Sensors, Branching, Trigger rules | — |
| 3 — Production Airflow | Docker, PostgreSQL, Celery, Kubernetes, Secrets, Logging, Monitoring, Pools, Concurrency, DAG deployment | — |
| 4 — MLOps Integration | Airflow + MLflow, + Docker, + Kubernetes, + S3/GCS, + model registry, + data validation, + monitoring | — |
| 5 — Build a Real Project | Full loop: New Data → Data Check → Features → Training → Evaluation → Monitoring → Drift? → Retrain | See below |

**By week:**

| Week | Focus |
|------|-------|
| Week 1 | Airflow architecture, DAGs, Tasks, Operators, Scheduling, Airflow UI |
| Week 2 | XCom, Variables, Connections, Sensors, Branching, Retries, Backfill/Catchup |
| Week 3 | Docker + Airflow, PostgreSQL, Executors, Logging, Pools, Concurrency, Production deployment |
| Week 4 | Airflow + MLflow, Airflow + S3, Airflow + Kubernetes, Training pipeline, Model evaluation, Model deployment |
| Week 5+ | Monitoring, Data drift, Automated retraining, CI/CD, Complete MLOps project |

> ✅ **Pro tip:** Building one real, end-to-end project (Level 5 above) will teach you far more than doing 20 basic Airflow tutorials.

---

## 🧪 Runnable Beginner MLOps DAG (Practice)

Use this after installing Airflow. It intentionally keeps the ML work simple so you can first understand the orchestration mechanics.

```python
import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

def validate_data():
    print("Data validation passed")

def train_model():
    print("Training model...")
    # Replace this with a call to your real training job.

def evaluate_model():
    accuracy = 0.92
    print(f"Validation accuracy: {accuracy}")

with DAG(
    dag_id="beginner_mlops_pipeline",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags=["mlops", "learning"],
) as dag:

    validate = PythonOperator(task_id="validate_data", python_callable=validate_data, retries=2)
    train = PythonOperator(task_id="train_model", python_callable=train_model, retries=2)
    evaluate = PythonOperator(task_id="evaluate_model", python_callable=evaluate_model)

    validate >> train >> evaluate
```

**What this teaches:**
- ✓ A DAG defines the workflow
- ✓ Each `PythonOperator` creates a task
- ✓ `>>` defines dependencies
- ✓ `retries=2` handles transient failures
- ✓ `catchup=False` prevents historical scheduled runs from being created automatically
- ✓ `pendulum` gives Airflow a timezone-aware `start_date`

> ⚠️ **Important:** This is a learning DAG. In a production MLOps system, replace the training task with an external/containerized training job when the workload is large or GPU-intensive.

---

## ❓ Interview Questions You Should Be Able to Answer

**Fundamentals**
1. What is Airflow? 2. What is a DAG? 3. What is a task? 4. What is an operator? 5. What does the scheduler do? 6. What is an executor? 7. What is XCom? 8. What are Airflow Variables? 9. What are Connections? 10. What is a Sensor?

**Production**
1. How do you handle task failures? 2. How do retries work? 3. What is idempotency? 4. What is backfill? 5. What is catchup? 6. How do you handle secrets? 7. How do you scale Airflow? 8. How do you control task concurrency? 9. How do you monitor Airflow? 10. How do you deploy DAGs?

**MLOps**
1. How would you design an ML training DAG? 2. How would Airflow interact with MLflow? 3. How would you run GPU training from Airflow? 4. Why use Kubernetes with Airflow? 5. How would you implement model quality gates? 6. How would you implement automated retraining? 7. How would you handle data validation? 8. How would you prevent duplicate training/data processing? 9. How would you design a production ML pipeline? 10. Airflow vs Kubeflow vs MLflow — what's the difference?

---

## 🛠️ Error Checklist Before You Run an Airflow DAG

If a DAG is not appearing in the Airflow UI, check these first:

| # | Issue | Fix |
|---|-------|-----|
| 1 | Import errors | Run `airflow dags list-import-errors` — a single Python import/syntax error can prevent the DAG from being parsed |
| 2 | Wrong Airflow version imports | For Airflow 3.x, use the public SDK and provider packages (see [Level 7](07_airflow_3x_modern.md)) — don't blindly copy 2.x-only imports |
| 3 | Invalid `start_date` | ✗ `start_date=...` → ✓ `start_date=pendulum.datetime(2026, 1, 1, tz="UTC")` — always use a real, timezone-aware date |
| 4 | Large XCom values | Don't return a huge DataFrame or model from a task just to pass it through XCom — store the artifact externally and pass a reference |
| 5 | Heavy training inside Airflow | Don't turn an Airflow worker into a five-hour GPU training machine — trigger an external job instead |
| 6 | Branching errors | A branch callable must return the `task_id` of the downstream task(s) that should continue |
| 7 | Duplicate work after retries | Make tasks idempotent — a retry should not blindly append duplicate records or create conflicting state |
| 8 | Scheduling confusion | A DAG's logical date/data interval is not simply "the exact time the Python code started" — learn how data intervals work |

---

## 🎓 Final MLOps Mental Model

```
GIT → CI/CD → AIRFLOW (Orchestration)
                 ├── DATA (S3/DB)
                 ├── TRAIN (K8s/GPU)
                 └── EVALUATE (MLflow)
        → MODEL REGISTRY → DEPLOYMENT → MONITORING
        → DRIFT/QUALITY → RETRAINING → back to AIRFLOW
```

| Component | Role |
|-----------|------|
| Airflow | Orchestration |
| MLflow | Experiment / model lifecycle tracking |
| Docker | Packaging |
| Kubernetes / cloud ML services | Compute and execution |
| S3 / GCS / Azure Blob | Data and artifacts |
| DVC | Versioning datasets/model artifacts when appropriate |
| FastAPI / KServe / SageMaker / Vertex AI | Model serving |

> ✅ **The MLOps engineer's job:** Connect these components into a reliable, observable, reproducible, retryable, and maintainable system.
>
> **Airflow is the conductor. It doesn't need to be every instrument in the orchestra.**

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| Airflow vs Jenkins/Kubeflow/MLflow/Prefect | Know the boundaries — orchestration vs CI/CD vs ML platform vs experiment tracking |
| MLOps Stack | Git → CI/CD → Airflow (Data/Train/Evaluate) → Registry → Deploy → Monitor → Retrain |
| Terminology list | The vocabulary every Airflow/MLOps engineer should know cold |
| Learning Roadmap | Fundamentals → Workflow Concepts → Production → MLOps Integration → Real Project |
| Error Checklist | The 8 things to check before debugging further when a DAG won't run |

---

⬅️ [Previous: Ecosystem Integrations](09_ecosystem_integrations.md) | [🏠 Roadmap](00_README.md) | ➡️ *(End of roadmap)*
