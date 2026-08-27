<div align="center">

# <span style="color:#D4A017">🟡 Level 3 — Data Structures</span>

![Level](https://img.shields.io/badge/Level-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Organizing_Data-D4A017)

</div>

---

## 🗂️ The Five Core Structures

| Structure | Ordered? | Mutable? | Duplicates? | Syntax |
|---|:---:|:---:|:---:|---|
| 📋 **List** | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| 🔤 **String** | ✅ | ❌ | ✅ | `"hello"` |
| 🔒 **Tuple** | ✅ | ❌ | ✅ | `(1, 2, 3)` |
| 🪪 **Set** | ❌ | ✅ | ❌ | `{1, 2, 3}` |
| 🗝️ **Dictionary** | ✅ (3.7+) | ✅ | Keys: ❌ | `{"key": "value"}` |

---

## 📋 Lists
Ordered and **mutable** — you can change, add, or remove items. Duplicates allowed.
```python
fruits = ["apple", "banana", "apple"]
fruits.append("mango")
```

---

## 🔤 Strings
Ordered, **immutable** sequences of characters — once created, they can't be changed in place.
```python
name = "Aditya"
# name[0] = "P"  ❌ this would raise an error
```

---

## 🔒 Tuples
Like lists (ordered, allow duplicates) but **immutable** — locked after creation.
```python
coordinates = (10, 20)
```

---

## 🪪 Sets
Unordered collections of **unique** values — duplicates are automatically removed.
```python
unique_ids = {101, 102, 102, 103}   # → {101, 102, 103}
```

---

## 🗝️ Dictionaries
Key-value pairs. Keys must be **unique** and are used to retrieve values.
```python
student = {"name": "Raj", "age": 21}
print(student["name"])   # → "Raj"
```

---

## 📝 Summary Table

| Structure | Best For |
|---|---|
| List | General-purpose ordered, changeable collection |
| String | Text data |
| Tuple | Fixed, unchangeable ordered data |
| Set | Uniqueness / removing duplicates |
| Dictionary | Fast lookup by a unique key |

---

### 🛠️ MLOps Perspective: Data Structures in ML Workflows
> [!IMPORTANT]
> Data structures are the building blocks of every ML pipeline. Here's how they map to real MLOps use cases:
> - **List:** Batches of file paths, a list of feature column names, or a sequence of training epochs
> - **Dictionary:** Model metadata, config files (`{"learning_rate": 0.01, "batch_size": 32}`), and JSON API responses from model registries
> - **Set:** Checking for duplicate records in a dataset before training — `set(df['id'])` to find unique IDs
> - **Tuple:** Immutable model input shapes — `input_shape = (224, 224, 3)` — never change these accidentally!

---

<div align="center">

⬅️ [Previous: Level 2 — Loops & Logic](./02_loops_logic.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 4 — Functions & Advanced Tools](./04_functions_advanced.md)

</div>
