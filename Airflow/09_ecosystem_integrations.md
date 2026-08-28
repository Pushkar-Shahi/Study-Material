<div align="center">

# <span style="color:#EC407A">🩷 Level 9 — Ecosystem Integrations</span>

![Level](https://img.shields.io/badge/Level--9-EC407A?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-MLflow%2C%20Docker%2C%20K8s%2C%20Cloud%2C%20CI%2FCD-EC407A?style=flat-square)

</div>

---

## 🧪 Airflow + MLflow

One of the most important combinations for an MLOps engineer.

| Tool | Responsibility |
|------|-----------------|
| Airflow | Orchestrates the workflow |
| MLflow | Tracks experiments / models / artifacts |

```
Airflow DAG → Training task → MLflow experiment → accuracy = 0.91
   → Register model → Production
```

MLflow tracks **Params, Metrics, and the Model** → feeding into the **Model Registry**.

> ⭐ **Don't confuse their responsibilities:** Airflow decides *when/how* a workflow runs. MLflow tracks *what happened* during the experiment.

---

## 🐳 Airflow + Docker

```
Git → Docker Image → Airflow → Run container → ML pipeline
```

Your training code can be packaged:

```dockerfile
FROM python:3.11
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ /app/src/
CMD ["python", "/app/src/train.py"]
```

Airflow then orchestrates execution of the container.

---

## ☸️ Airflow + Kubernetes

Particularly important if you want to work as an MLOps engineer.

```
Airflow — Kubernetes Operator
   ├── Data Pod
   ├── Training Pod (→ GPU)
   └── Eval Pod
```

Flow: `Airflow → KubernetesPodOperator → training container → GPU node → train model → save artifact to S3`

This allows you to cleanly **separate orchestration from compute**.

---

## ☁️ Airflow + Cloud

You should eventually learn **one cloud deeply**.

| Cloud | Flow |
|-------|------|
| AWS | Airflow → S3 → SageMaker → MLflow/Registry → EKS/SageMaker Endpoint |
| GCP | Airflow / Cloud Composer → GCS → Vertex AI → Model Registry → Endpoint |
| Azure | Airflow → Azure Blob → Azure ML → Model Registry → Endpoint |

---

## 🔄 CI/CD + Airflow

```
Developer → Git Push → CI → Tests → Docker Build
   → Container Registry → Deploy DAG → Airflow
```

CI might test: **Python tests, DAG import, Linting, Data validation code, Docker build, Security scanning**.

---

## 🧭 Summary Table

| Keyword | Purpose |
|---------|---------|
| Airflow + MLflow | Airflow orchestrates; MLflow tracks experiments & manages the Model Registry |
| Airflow + Docker | Package training code into an image; Airflow orchestrates container execution |
| Airflow + Kubernetes | `KubernetesPodOperator` cleanly separates orchestration from compute (incl. GPU) |
| Airflow + Cloud | AWS (S3/SageMaker), GCP (GCS/Vertex AI), Azure (Blob/Azure ML) |
| CI/CD + Airflow | Tests, builds, and deploys DAGs through a standard CI/CD pipeline |

---

⬅️ [Previous: MLOps Production Patterns](08_mlops_production_patterns.md) | [🏠 Roadmap](00_README.md) | ➡️ [Next: Comparisons, Roadmap & Reference](10_comparisons_reference.md)
