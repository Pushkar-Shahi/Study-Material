<div align="center">

# <span style="color:#E74C3C">🟥 Level 5 — Data Sharing & Scheduling</span>

![Level](https://img.shields.io/badge/Level--5-E74C3C?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-XComs%2C%20Cron%20%26%20Backfills-E74C3C?style=flat-square)

</div>

---

## 🔀 XComs (Cross-Communications)

XComs allow tasks within a DAG to share **small amounts of data**.

| Mechanism | How It Works |
|-----------|---------------|
| Push & Pull | One task "pushes" information to XComs, another task "pulls" it |
| Automatic Sharing | Any value returned by a Python function in a `PythonOperator` is auto-pushed under the key `return_value` |
| Manual Control | `ti.xcom_push` sends specific data with a key; `ti.xcom_pull` retrieves it by `task_ids` + `key` |
| TaskFlow API | Automatically manages push/pull when you pass variables between decorated tasks |

```python
def push_data(ti):
    ti.xcom_push(key="model_version", value="v42")

def pull_data(ti):
    value = ti.xcom_pull(task_ids="push_data_task", key="model_version")
    print(value)
```

> ⚠️ **Important MLOps rule:** Do **not** put large datasets or models into XCom (strict **48 KB** limit).
>
> | ✗ Bad | ✓ Better |
> |--------|----------|
> | XCom → 2 GB model file | S3 → `model.pkl`, then XCom → `"s3://bucket/models/model.pkl"` (a *reference*, not the data) |

---

## ⏳ Catchup & Backfill

Two different ways to handle running a DAG for dates in the past.

| Feature | Catchup | Backfill |
|---------|---------|----------|
| Default behavior | `True` by default | N/A — manual action |
| What it does | Auto-triggers every missed run from `start_date` to now, once the DAG is turned on | Manually runs a DAG for a specific historical period, even if catchup is off |
| How to control | Set `catchup=False` to only run the most recent interval | Run via CLI |
| Where it runs | Automatic, on DAG activation | Inside the Airflow scheduler container |

```python
@dag(schedule="@daily", start_date=pendulum.datetime(2026, 1, 1, tz="UTC"), catchup=False)
def my_dag():
    ...
```

```bash
airflow dags backfill --start-date [START_DATE] --end-date [END_DATE] [DAG_ID]
```

> ⚠️ **Don't over-generalize:** Don't memorize "always use `catchup=False`." Understand *why* you're disabling historical runs before you disable them.

> ℹ️ **Key mental model:** Airflow's scheduling model is strongly based around **logical dates / data intervals** — not "the exact moment the DAG code started." A DAG run for `2026-08-01` represents the data interval for that date, regardless of when it actually executed. This is one of the most common beginner points of confusion.

---

## ⏰ Scheduling with Cron Expressions

The `schedule` parameter (called `schedule_interval` in older Airflow versions) determines when your workflow runs. It accepts **Cron expressions** — five whitespace-separated fields representing different time units.

```python
schedule="@daily"
# or
schedule="0 2 * * *"
```

| Expression | Meaning |
|------------|---------|
| `@daily` | Runs at midnight (same as `0 0 * * *`) |
| `@hourly` | Runs every hour |
| `0 2 * * *` | Every day at 2:00 AM |
| `0 3 * * 2` | Every Tuesday at 3:00 AM |
| `0 3 * * 2,5` | Every Tuesday **and** Friday at 3:00 AM |
| `0 3 * * 2-5` | Every day **Tuesday through Friday** at 3:00 AM |

> 💡 **Tip:** Use [crontab.guru](https://crontab.guru) to visually generate and verify your cron strings in plain English. Understand these well — they're used constantly in production scheduling.

---

## 📦 Airflow Dataset Scheduling

| ✗ Traditional: Time-Based | ✓ Modern: Data/Event-Aware |
|------------------------------|-------------------------------|
| Run every day at 2 AM, regardless of whether new data exists | New dataset available → trigger downstream workflow automatically |

This event/data-aware scheduling can be particularly useful for **data-driven ML pipelines**, where you want a DAG to fire only when a real upstream dependency (a new dataset) has actually landed.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| XCom | Small data-sharing mechanism between tasks (48 KB limit — references only, not artifacts) |
| `xcom_push` / `xcom_pull` | Manual XCom control |
| `catchup` | Controls whether missed past runs auto-trigger (default `True`) |
| `airflow dags backfill` | CLI command to manually run historical DAG intervals |
| Logical date / data interval | What a DAG run actually represents — not literally "when it started" |
| `schedule` (`schedule_interval` in 2.x) | Cron-based schedule for a DAG |
| Dataset scheduling | Event/data-aware triggering instead of pure time-based cron |

---

⬅️ [Previous: Building DAGs](04_building_dags.md) | [🏠 Roadmap](00_README.md) | ➡️ [Next: Connections, Variables & Sensors](06_connections_hooks.md)
