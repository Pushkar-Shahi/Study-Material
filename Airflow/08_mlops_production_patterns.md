<div align="center">

# <span style="color:#1ABC9C">🟦 Level 8 — MLOps Production Patterns</span>

![Level](https://img.shields.io/badge/Level--8-1ABC9C?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Making%20It%20Production--Ready-1ABC9C?style=flat-square)

</div>

---

## ♻️ Idempotency

> ⚠️ **Very important for MLOps interviews:** A task should ideally produce the **same correct result** when executed again with the same inputs.

| ✗ Bad | ✓ Better |
|--------|----------|
| `append_data_to_database()` — if Airflow retries, you might duplicate records | `write_partition(date="2026-08-11")` — or use upsert/overwrite semantics |

> 🧠 **Always ask this question:** *"If Airflow runs my task twice, will it corrupt my data?"*

---

## 🔁 Retries

ML/data pipelines fail — API timeouts, S3 unavailability, database connection failures, Kubernetes pod failures. Configure retries so a transient failure doesn't kill your pipeline:

```python
retries = 3
retry_delay = timedelta(minutes=5)
```

> ⭐ **Production feature:** Configuring retries and retry delay is one of the most important production-readiness settings in any DAG.

---

## 🏊 Pools

Suppose you have **100 training tasks but only 4 GPUs** — you don't want all 100 jobs running simultaneously.

```
100 tasks → GPU Pool = 4 slots → only 4 run at once
```

> ⭐ **Production concept:** Airflow **pools** let you control concurrency against a limited resource, like GPUs or an external API rate limit.

---

## ⏸️ Deferrable Operators

Some tasks spend most of their time **waiting**:

```
Start training job → Wait 2 hours → Training finished
```

A traditional worker stays occupied the whole time it waits. **Deferrable operators** let Airflow handle long waits far more efficiently, freeing worker slots during the wait.

> ℹ️ **Not day-one material:** You don't need to master this immediately, but you should know why it exists.

---

## ✅ Data Validation in Airflow

Integrate tools such as **Great Expectations, Soda, or Pandera**:

```
Raw Data → Data Validation → FAIL → Stop + Alert
                            → PASS → Training
```

Example checks: null percentage, schema, data types, range, distribution, duplicate rows, categorical values.

---

## 🎯 Model Validation

```
Model → Evaluate → Compare against baseline → Quality gate
```

Metrics could include: **Accuracy, Precision, Recall, F1, ROC-AUC, RMSE, MAE, MAPE**.

> ⭐ **Ask the right question:** Don't simply ask *"Did training succeed?"* Ask *"Is this model better than the currently deployed model?"*

| ✗ Don't Deploy | ✓ Deploy |
|------------------|-----------|
| Current F1 = 0.84, New F1 = 0.79 | Current F1 = 0.84, New F1 = 0.88 |

---

## 📡 Monitoring + Airflow (The Full MLOps Loop)

```
Daily → Collect production predictions → Calculate drift → Drift detected?
     → Trigger retraining → Production → Monitoring → Drift Detection
     → Airflow → Retraining Pipeline
```

This gives you a complete MLOps loop:

```
Data → Train → Evaluate → Deploy → Monitor → Drift?
   No  → (loop continues)
   Yes → Retrain
```

---

## 🔔 Airflow Alerts

```
Training failed → Airflow → Slack / Email / PagerDuty
```

You want alerts for: **task failure, DAG failure, deadline/timeliness issues, data quality failure, model quality failure**.

---

## 📋 Airflow Logging

Every task should have useful logs:

```
[INFO] Loading data
[INFO] Dataset rows: 1,245,000
[INFO] Features: 42
[INFO] Training model
[INFO] Validation F1: 0.89
[INFO] Model registered: fraud_model:v17
```

> ℹ️ **Why it matters:** When production fails, logs are often the first thing you'll inspect.

---

## 📁 Airflow Folder Structure

A clean project structure might look like:

```
mlops-project/
├── dags/
│   └── training_pipeline.py
├── src/
│   ├── data/
│   │   ├── ingest.py
│   │   └── validation.py
│   ├── features/
│   │   └── build_features.py
│   ├── training/
│   │   └── train.py
│   └── evaluation/
│       └── evaluate.py
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

> ⭐ **Principle:** The DAG should mainly describe **orchestration**, while business/ML logic lives elsewhere in `src/`.

---

## 🏆 Airflow Best Practices for MLOps

| # | Practice | Detail |
|---|----------|--------|
| 1 | Keep DAGs lightweight | ✗ 1000 lines of ML code inside the DAG file → ✓ `DAG` → `train.py` → training container |
| 2 | Don't store large data in XCom | Use S3 / GCS / Azure Blob / a database, and pass references instead |
| 3 | Make tasks idempotent | Retries shouldn't corrupt your pipeline |
| 4 | Version your code | Use Git |
| 5 | Version your models | Use the MLflow Model Registry |
| 6 | Version your data | DVC, LakeFS, Delta Lake, Iceberg |
| 7 | Containerize ML workloads | Docker, Kubernetes |
| 8 | Separate orchestration from computation | See table below |

| Layer | Responsibility |
|-------|-----------------|
| Airflow | Orchestration |
| Kubernetes / SageMaker / etc. | Compute |
| MLflow | Experiment / model management |
| S3 / GCS | Artifacts / data |

> ⭐ **Remember this:** This mental model is extremely important for MLOps interviews and real production design.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| Idempotency | Re-running a task shouldn't corrupt data |
| `retries` / `retry_delay` | Handles transient pipeline failures |
| Pools | Controls concurrency against limited resources (GPUs, rate limits) |
| Deferrable Operators | Free worker slots during long waits |
| Data Validation | Catches bad data before it reaches training (Great Expectations, Soda, Pandera) |
| Model Validation | Compares new model against the currently deployed baseline |
| Alerts / Logging | Task/DAG failure notifications + inspectable logs for debugging |
| Folder Structure | Keeps DAGs thin; business logic lives in `src/` |

---

⬅️ [Previous: Airflow 3.x & Modern Capabilities](07_airflow_3x_modern.md) | [🏠 Roadmap](00_README.md) | ➡️ [Next: Ecosystem Integrations](09_ecosystem_integrations.md)
