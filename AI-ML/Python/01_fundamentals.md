<div align="center">

# <span style="color:#2E8B57">🟢 Level 1 — Python Fundamentals</span>

![Level](https://img.shields.io/badge/Level-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Building_Blocks-2E8B57)

</div>

---

## 📦 Variables & Data Types

Variables are containers used for storing data values. Python has **no type declaration** — you just assign with `=`.

| Type | Keyword | Example |
|---|---|---|
| Integer | `int` | `50`, `-6` |
| Float | `float` | `5.7`, `2.0` |
| String | `str` | `"Aditya"` |
| Boolean | `bool` | `True`, `False` |

---

## ⌨️ Input & Typecasting

```python
age = input("Enter your age: ")   # always returns a string!
age = int(age)                     # typecast to int for calculations
```

| Function | Converts To |
|---|---|
| `int()` | Integer |
| `float()` | Decimal |
| `str()` | Text |

> [!WARNING]
> `input()` **always** returns a string — even if the user types a number. Always typecast before doing arithmetic!

---

## ⚙️ Basic Operators

### ➕ Arithmetic
| Operator | Meaning | Example |
|:---:|---|---|
| `+` `-` `*` | Add / Subtract / Multiply | `5 + 3` |
| `/` | Division (always returns float) | `10 / 2 → 5.0` |
| `//` | Floored division (removes decimals) | `10 // 3 → 3` |
| `%` | Modulus (remainder) | `10 % 3 → 1` |
| `**` | Exponentiation (power) | `2 ** 3 → 8` |

### 📝 Assignment
```python
x += 5   # same as x = x + 5
```

### 🔍 Comparison (returns Boolean)
| Operator | Meaning |
|:---:|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` `<` | Greater / Less than |

### 🧠 Logical
| Operator | Behavior |
|---|---|
| `and` | True if **both** are true |
| `or` | True if **at least one** is true |
| `not` | Reverses the result |

---

## 🔀 Decision Making (if / elif / else)

| Keyword | Role |
|---|---|
| `if` | Runs only if condition is `True` |
| `elif` | Checks another condition if the previous was `False` |
| `else` | Catch-all if nothing else matched |

### ✅ Syntax Rules
- Always end `if`, `elif`, `else` with a **colon `:`**
- **Indentation** defines the body of the block

```python
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Fail")
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Variables & Types | Store and label data |
| Typecasting | Convert between data types |
| Operators | Manipulate and compare values |
| if/elif/else | Branch code based on conditions |

---

### 🛠️ MLOps Perspective: Python Fundamentals
> [!NOTE]
> These basics are the foundation of every ML script you will ever write. In an MLOps context:
> - **Boolean flags** control pipeline behavior (e.g., `IS_PROD = True`)
> - **Typecasting** is critical when parsing environment variables or config files — everything from `.env` files comes in as a string
> - **`if/elif/else`** is how you write routing logic in model serving APIs (e.g., route to Model A if confidence > 0.9, else fallback to Model B)

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Level 2 — Loops & Logic](./02_loops_logic.md)

</div>
