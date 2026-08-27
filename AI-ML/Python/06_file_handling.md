<div align="center">

# <span style="color:#8E44AD">🟣 Level 6 — File Handling</span>

![Level](https://img.shields.io/badge/Level-6-8E44AD) ![Theme](https://img.shields.io/badge/Theme-Purple_%E2%80%94_Persisting_Data-8E44AD)

</div>

---

## 📂 Opening Files & Modes

```python
file = open("data.txt", "r")
```

| Mode | Name | Behavior |
|:---:|---|---|
| `'r'` | Read | Opens a file for reading |
| `'w'` | Write | Creates new / **overwrites** existing file |
| `'a'` | Append | Adds data to the end, keeps existing content |
| `'x'` | Create | Creates a new file, **fails** if it already exists |

---

## 📖 Reading Files

| Method | Returns |
|---|---|
| `read()` | Entire file as one string |
| `readline()` | One line at a time |
| `readlines()` | List of all lines |

```python
with open("data.txt", "r") as file:
    for line in file:        # iterate directly
        print(line)
```

---

## ✏️ Writing Files

```python
with open("data.txt", "w") as file:
    file.write("Hello, world!\n")
```

> [!TIP]
> **Best Practice:** Always use `with open(...) as file:` — it automatically closes the file for you, even if an error occurs.

---

## 📊 Working with CSV Files

Structured data uses the `csv` module — common in **AI/ML** workflows.

### ✏️ `csv.writer`
```python
import csv
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])       # header
    writer.writerow(["Aditya", 21])         # row
```

### 📖 `csv.reader`
```python
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:                      # each row = a list
        print(row)
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `open(filename, mode)` | Access a file in a specific mode |
| `read()/readline()/readlines()` | Different ways to read content |
| `write()` | Add string data to a file |
| `with` statement | Auto-closes files safely |
| `csv.writer` / `csv.reader` | Work with structured tabular data |

---

### 🛠️ MLOps Perspective: File Handling in Data Pipelines
> [!IMPORTANT]
> File handling is the foundation of data ingestion pipelines. In MLOps:
> - **CSV reading** is how you load raw training data before converting to a Pandas DataFrame with `pd.read_csv()` — which is itself built on Python's file I/O
> - **`'a'` (append) mode** is used to write logs during model training — append new metrics to a log file each epoch without overwriting previous runs
> - **`with` statement** is non-negotiable in production code — resource leaks (unclosed files) can crash long-running pipeline containers
> - Beyond CSV, you'll work with **JSON** (`json` module), **Parquet** (via PyArrow), and **YAML** (for config files) — all use the same underlying file I/O concepts you learned here

---

<div align="center">

⬅️ [Previous: Level 5 — OOP & Error Handling](./05_oop_error_handling.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full Python Roadmap!

</div>
