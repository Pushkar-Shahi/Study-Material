<div align="center">

# <span style="color:#C0392B">🔴 Level 5 — OOP & Error Handling</span>

![Level](https://img.shields.io/badge/Level-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Structure_%26_Resilience-C0392B)

</div>

---

## 🏗️ Object-Oriented Programming (OOP)

OOP organizes software design around **objects** (data) rather than just functions and logic.

### 🧩 Classes & Objects
| Term | Meaning | Example |
|---|---|---|
| Class | Blueprint/template | `Car` class defines `brand`, `color` |
| Object | Specific instance of a class | `"BMW"`, `"Volvo"` |

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

my_car = Car("BMW", "Black")
```

### 🔨 The Constructor `__init__`
Automatically runs when a new object is created — used to initialize attributes.

### 🪞 The `self` Parameter
Represents the **current instance** of the class — lets you access its variables and methods.

### 👨‍👩‍👧 Inheritance
A **child class** inherits attributes and methods from a **parent class**.
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):   # inherits from Person
    pass
```

### 🔀 Polymorphism
Different types handled through the **same interface**.
```python
len("hello")       # string
len([1, 2, 3])      # list
len({"a": 1})        # dictionary
# all use the same len() interface
```

---

## 🛡️ Error Handling

### ⚠️ Common Errors
| Error | Cause |
|---|---|
| `ZeroDivisionError` | Dividing by zero |
| `ValueError` | Right type, wrong value (e.g., `int("Twenty")`) |
| `IndexError` | Accessing a list index that doesn't exist |
| `KeyError` | Accessing a dictionary key that isn't there |

### 🔁 `try` / `except` Block
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### 🔀 `else` and `finally`
| Block | Runs When |
|---|---|
| `else` | Only if **no exception** occurred in `try` |
| `finally` | **Always** runs — great for cleanup (e.g., closing a file) |

```python
try:
    x = int("5")
except ValueError:
    print("Invalid input")
else:
    print("Conversion succeeded")
finally:
    print("Done processing")
```

### 🚨 Raising Errors
```python
if marks > 100:
    raise ValueError("Marks Invalid")
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Class / Object | Blueprint vs. real instance |
| `__init__` / `self` | Initialize and reference object data |
| Inheritance | Share behavior between classes |
| Polymorphism | Same interface, different implementations |
| `try/except/else/finally` | Handle runtime errors gracefully |
| `raise` | Manually trigger an error |

---

### 🛠️ MLOps Perspective: OOP & Resilience in Production
> [!IMPORTANT]
> OOP and Error Handling are critical for writing **production-grade** ML code:
> - **OOP:** ML Frameworks like `scikit-learn` are built entirely on OOP. Every model is a class with `.fit()` and `.predict()` methods. When you build custom transformers or preprocessing steps, you subclass `BaseEstimator`
> - **`try/except`:** Production pipelines **must not crash**. Wrap data-loading steps in `try/except` to catch bad file reads or network failures and trigger fallback logic or alerts
> - **`finally`:** Always use `finally` to release database connections or close file handles — essential for preventing resource leaks in long-running pipeline containers
> - **`raise`:** Validate model inputs explicitly. If a model receives data with the wrong number of features, `raise ValueError` immediately rather than letting it produce silent garbage predictions

---

<div align="center">

⬅️ [Previous: Level 4 — Functions & Advanced Tools](./04_functions_advanced.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 6 — File Handling](./06_file_handling.md)

</div>
