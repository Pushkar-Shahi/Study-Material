<div align="center">

# <span style="color:#9B59B6">🟪 Level 6 — Connections, Variables & Sensors</span>

![Level](https://img.shields.io/badge/Level--6-9B59B6?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Postgres%2C%20S3%20%26%20Config-9B59B6?style=flat-square)

</div>

---

## 🔌 Airflow Connections

Connections store **credentials/configuration** for external systems (AWS, GCP, PostgreSQL, Slack, Kubernetes, etc.) so operators and hooks can use them. Create them via the UI: **Admin > Connections**.

| Field | Example / Notes |
|-------|------------------|
| Connection Id | Unique name, e.g. `postgres_localhost` |
| Connection Type | `postgres` |
| Host | `host.docker.internal` (Docker on Mac/Windows → local DB), otherwise the service name from `docker-compose.yaml` or `localhost` |
| Schema | The specific database name, e.g. `test` |
| Login / Password | Your DB credentials (often `airflow`/`airflow` locally) |
| Port | Typically `5432` |

> ⚠️ **Secrets:** For passwords/API keys, use a **Secrets Backend** or an appropriate secret manager — never hard-code credentials in DAG code.

---

## 🎛️ Variables

Airflow Variables store **configuration values** you can access from within any task:

```python
model_threshold = 0.85
environment = "production"
bucket_name = "ml-models"
```

> ⚠️ **Gotcha:** Don't use Variables as a replacement for proper secrets management — use a Secrets Backend for actual credentials.

---

## 🐘 PostgresOperator

```python
from airflow.providers.postgres.operators.postgres import PostgresOperator

create_table = PostgresOperator(
    task_id="create_table",
    postgres_conn_id="postgres_localhost",
    sql="""
        CREATE TABLE IF NOT EXISTS dag_runs (
            dt DATE,
            dag_id VARCHAR(250)
        );
    """
)

insert_row = PostgresOperator(
    task_id="insert_row",
    postgres_conn_id="postgres_localhost",
    sql="""
        INSERT INTO dag_runs (dt, dag_id)
        VALUES ('{{ ds }}', '{{ dag.dag_id }}');
    """
)
```

Supports **Jinja templates** — `{{ ds }}` (execution date), `{{ dag.dag_id }}` (current DAG's name). Often used to delete existing data before a new insert, to avoid primary key violations.

---

## 🪝 PostgresHook

```python
from airflow.providers.postgres.hooks.postgres import PostgresHook

def query_and_save():
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders;")
    results = cursor.fetchall()
    # process results, e.g. write to a local CSV via Python's csv module
```

---

## 👀 Sensors

Sensors **wait for something to happen** before letting the pipeline continue.

```
Wait for data → Data available? → YES → Continue pipeline
```

Common types: wait for a file, wait for another DAG, wait for an external job, wait for a cloud object.

For ML specifically: `Wait for new dataset → Validate → Train`

### S3KeySensor

```python
from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor

wait_for_file = S3KeySensor(
    task_id="wait_for_file",
    bucket_name="my-bucket",
    bucket_key="incoming/data.csv",
    aws_conn_id="aws_default",
    poke_interval=5,
    timeout=30
)
```

| Behavior | Detail |
|----------|--------|
| Poking mode | Default — checks for the file's existence at a set frequency |
| Poke Interval | e.g. every 5 seconds |
| Timeout | e.g. 30 seconds — task fails if the file never appears |

> 💡 **Tip:** For local testing, use **MinIO** — an open-source, S3-API-compatible tool — to simulate an S3 environment in Docker.

### S3Hook

```python
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

def upload_to_s3(local_path, bucket, key):
    hook = S3Hook(aws_conn_id="aws_default")
    hook.load_file(filename=local_path, key=key, bucket_name=bucket, replace=True)
```

---

## 🔗 Building a Postgres-to-S3 ETL Pipeline

1. **Query Data** — Use `PostgresHook` to pull records from a table (e.g. `orders`)
2. **Dynamic Filtering** — Use Airflow macros (like the execution date) to query only the relevant time interval
3. **Temporary Storage** — Use Python's `NamedTemporaryFile` to save queried data to a temporary location on disk
4. **Upload** — Use `S3Hook` to upload the temp file to your S3 bucket

> ⚠️ **Gotcha:** Because the file lives in a temporary directory, it's automatically deleted once the task finishes — keeping your local `dags` folder uncluttered.

---

## 🧭 Summary Table

| Feature | Purpose |
|---------|---------|
| Variables | Configuration values (e.g. thresholds, environment names) |
| Connections | External system credentials/config (e.g. AWS, Postgres) |
| XCom | Small task-to-task communication *(see [Level 5](05_data_sharing_scheduling.md))* |
| Metadata DB | Airflow's own internal state |
| Object storage (S3/GCS) | Large data / models / artifacts |
| Sensors | Wait for a condition (file, dataset, job) before continuing |

---

⬅️ [Previous: Data Sharing & Scheduling](05_data_sharing_scheduling.md) | [🏠 Roadmap](00_README.md) | ➡️ [Next: Airflow 3.x & Modern Capabilities](07_airflow_3x_modern.md)
