<div align="center">

# <span style="color:#E67E22">🟧 Level 4 — Building DAGs</span>

![Level](https://img.shields.io/badge/Level--4-E67E22?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Operators%2C%20Branching%20%26%20TaskFlow-E67E22?style=flat-square)

</div>

---

> ⚠️ **Version note:** Some tutorials online still use Airflow 2.x imports (e.g. `from airflow.operators.python import PythonOperator`). The examples below use the **current Airflow 3.x style** — `airflow.sdk` for the DAG object and `airflow.providers.standard...` for standard operators. Concepts are the same either way; when in doubt, follow the docs matching your installed version.

---

## 🕸️ The Most Important Concept: Defining a DAG

```python
import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="ml_training_pipeline",
    schedule="@daily",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )
    validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )
    train = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
    )

    extract >> validate >> train
```

The important part is the dependency operator: `extract >> validate >> train` — this defines execution order.

> ⚠️ **Gotcha:** Always use a real, timezone-aware `start_date` (via `pendulum.datetime(...)`). A placeholder like `start_date=...` will break DAG parsing.

---

## 🖥️ BashOperator

```python
from airflow.providers.standard.operators.bash import BashOperator

task1 = BashOperator(task_id="say_hello", bash_command="echo hello world")
task2 = BashOperator(task_id="run_training", bash_command="python train.py")

task1 >> task2
```

Common commands: `python train.py`, `pytest tests/`, `dvc pull`.

---

## 🐍 PythonOperator

```python
from airflow.providers.standard.operators.python import PythonOperator

def train_model():
    print("training...")

run_task = PythonOperator(
    task_id="run_my_function",
    python_callable=train_model,
    op_kwargs={"name": "Airflow"}   # pass args via op_kwargs
)
```

Good for: data preprocessing, validation, small ML operations, calling APIs, triggering ML jobs.

---

## ☸️ KubernetesPodOperator — Extremely Important for MLOps

Allows Airflow to run a task **inside a Kubernetes pod** — much better than running large model training directly inside the Airflow worker.

```
Airflow → Kubernetes → Training Pod → ML Training
```

Airflow can fan this out across multiple pods for a pipeline:

| Pod | Task |
|-----|------|
| Data Validation | Runs in its own pod |
| Feature Engineering | Runs in its own pod |
| GPU Training | Runs in its own pod |
| Evaluation | Runs in its own pod |

> 💡 **Tip:** This is how you keep heavy GPU training **off** the Airflow worker (see [Level 3](03_architecture_task_lifecycle.md) — "Airflow Should NOT Do Everything").

---

## 🚦 Branching / Conditional Deployment

A key MLOps pattern — the **quality gate**: only register/deploy a model if it clears a threshold.

```python
from airflow.providers.standard.operators.python import BranchPythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator

def check_model():
    accuracy = 0.92
    if accuracy >= 0.90:
        return "register_model"
    return "stop_pipeline"

check = BranchPythonOperator(
    task_id="check_model",
    python_callable=check_model,
)

register = EmptyOperator(task_id="register_model")
stop = EmptyOperator(task_id="stop_pipeline")

evaluate >> check >> [register, stop]
```

> ⚠️ **Rule:** The branch function must return the `task_id` of the downstream task to follow. This is how you implement model quality gates.

---

## ✨ TaskFlow API

Modern Airflow encourages the TaskFlow API for Python-heavy workflows — it uses decorators to reduce boilerplate.

| ✗ Traditional Operator Wiring | ✓ TaskFlow API |
|-------------------------------|------------------|
| `extract = PythonOperator(task_id="extract", python_callable=extract_data)`<br>`transform = PythonOperator(task_id="transform", python_callable=transform_data)`<br>`extract >> transform` | `@task`<br>`def extract(): return data`<br><br>`@task`<br>`def transform(data): return transformed_data`<br><br>`data = extract()`<br>`transformed = transform(data)` |

```python
from airflow.decorators import dag, task
import pendulum

@dag(schedule="@daily", start_date=pendulum.datetime(2026, 1, 1, tz="UTC"), catchup=False)
def my_taskflow_dag():

    @task
    def extract():
        return {"value": 42}

    @task(multiple_outputs=True)
    def transform(data):
        return {"doubled": data["value"] * 2}

    @task
    def load(result):
        print(f"Loaded: {result}")

    raw = extract()
    transformed = transform(raw)
    load(transformed["doubled"])

my_taskflow_dag()
```

> ✅ **Benefit:** No manual `>>` wiring needed — dependencies are inferred from function calls, and XCom push/pull is handled automatically. This can reduce boilerplate by **nearly a third** vs. the traditional PythonOperator.

---

## 🔁 Dynamic Task Mapping

Suppose you need to train models for several targets: `model_A`, `model_B`, `model_C`, `model_D`. Instead of manually creating four near-identical tasks, Airflow can **dynamically map a task over a list**.

```
train_model
   ├── model_A
   ├── model_B
   └── model_C
```

Very useful for: multiple models, multiple datasets, multiple regions, multiple customers, hyperparameter jobs.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| `airflow.sdk` / provider imports | Airflow 3.x-correct import paths for `DAG` and standard operators |
| `BashOperator` / `PythonOperator` | Run a shell command / Python function as a task |
| `KubernetesPodOperator` | Runs a task inside a K8s pod — key for offloading heavy ML compute |
| `BranchPythonOperator` | Implements conditional workflows / quality gates |
| `@dag` / `@task` | TaskFlow API decorators — less boilerplate, automatic dependencies & XCom |
| Dynamic Task Mapping | Fan a single task out across a list (models, datasets, regions...) |

---

⬅️ [Previous: Architecture & Task Lifecycle](03_architecture_task_lifecycle.md) | [🏠 Roadmap](00_README.md) | ➡️ [Next: Data Sharing & Scheduling](05_data_sharing_scheduling.md)
