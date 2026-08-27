<div align="center">

# <span style="color:#E07B00">🟠 Level 4 — Functions & Advanced Tools</span>

![Level](https://img.shields.io/badge/Level-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Reusable_%26_Concise_Code-E07B00)

</div>

---

## 🧩 Function Basics

```python
def greet(name="Raj"):     # default argument
    return f"Hello, {name}!"

greet("Aditya")             # positional argument
greet(name="Aditya")        # keyword argument
```

| Concept | Description |
|---|---|
| `def` | Keyword to define a function |
| Positional args | Passed in order |
| Keyword args | Passed by name, e.g. `name="Raj"` |
| Default args | Used when no value is provided |
| `return` | Sends a value back to the caller |

---

## ⚡ Lambda Functions

Anonymous, single-line functions — no `def`, no name.

```python
square = lambda x: x * x
square(5)   # → 25
```

**Syntax:** `lambda parameters: expression`

---

## 🔧 Advanced Functional Tools

### 🗺️ `map()` — Apply to Every Item
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
# → [1, 4, 9, 16]
```

### 🔬 `filter()` — Keep Only Matching Items
```python
evens = list(filter(lambda x: x % 2 == 0, numbers))
# → [2, 4]
```

### ➕ `reduce()` — Rolling Computation
```python
from functools import reduce
total = reduce(lambda a, b: a + b, numbers)
# → 10
```

---

## 📝 Summary Table

| Tool | Purpose |
|---|---|
| `def` function | Reusable named block of code |
| `lambda` | Quick, throwaway single-expression function |
| `map()` | Transform every item in an iterable |
| `filter()` | Keep only items matching a condition |
| `reduce()` | Combine all items into a single value |

---

### 🛠️ MLOps Perspective: Functional Tools in ML
> [!IMPORTANT]
> Functions are the building blocks of every ML pipeline step. In MLOps:
> - **Each pipeline step is a function:** Data ingestion, preprocessing, training, evaluation — each is wrapped in a Python function with defined inputs and outputs
> - **`lambda` + `map()`** are extremely common for fast, vectorized data transformations on lists of records before converting to a Pandas DataFrame or NumPy array
> - **`filter()`** is used to remove invalid or out-of-range records from a dataset in one line
> - MLOps frameworks like **Kubeflow and ZenML** define entire pipelines as decorated Python functions — mastering `def` is non-negotiable!

---

<div align="center">

⬅️ [Previous: Level 3 — Data Structures](./03_data_structures.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 5 — OOP & Error Handling](./05_oop_error_handling.md)

</div>
