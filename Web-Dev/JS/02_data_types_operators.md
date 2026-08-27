<div align="center">

# <span style="color:#1E6FEB">🔵 Section 2 — Data Types & Operators</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Values_%26_Calculations-1E6FEB)

</div>

---

## 🧱 JavaScript Data Types

### 1️⃣ Primitive Data Types

| Type | Description | Example |
|---|---|---|
| **Number** | Integers, decimals, negatives | `45`, `9.5`, `-5` |
| **String** | Text (single, double quotes, or backticks) | `"Hello World"` |
| **Boolean** | Logical state | `true` / `false` |
| **Null** | Intentional, explicit absence of value | `null` |
| **Undefined** | Declared but not yet assigned | `undefined` |
| **BigInt** | Extremely large integers | `123n` |
| **Symbol** | Unique identifiers | `Symbol("id")` |

```js
let name = `Hello, ${userName}`;   // template literal — embeds variables
```

> [!TIP]
> Use `typeof` to check any value's data type: `typeof 45` → `"number"`

### 2️⃣ Non-Primitive (Complex) Data Types

| Type | Description |
|---|---|
| **Object** | Key-value pairs representing real-world entities |
| **Array** | Ordered, indexed list of values |
| **Function** | Reusable block of code |

---

## ⚙️ JavaScript Operators

### ➗ Arithmetic Operators

| Operator | Meaning |
|:---:|---|
| `+` `-` | Addition / Subtraction |
| `*` `/` | Multiplication / Division |
| `%` | Modulus (remainder) |
| `**` | Exponentiation (e.g., `2 ** 4` → `16`) |
| `++` `--` | Increment / Decrement |

> [!NOTE]
> **Pre vs. Post:** `++num` updates immediately; `num++` updates after the current line runs.

### 📝 Assignment Operators

```js
num += 5;   // shorthand for: num = num + 5
```

| Operator | Equivalent |
|:---:|---|
| `+=` | `num = num + x` |
| `-=` `*=` `/=` `%=` `**=` | Same pattern for other operations |

### 🔍 Comparison Operators

| Operator | Meaning | Returns |
|:---:|---|---|
| `>` `<` `>=` `<=` | Greater/Less than (or equal) | Boolean |
| `!=` | Not equal to | Boolean |
| `==` | **Loose** equality — converts type first | `"5" == 5` → `true` |
| `===` | **Strict** equality — checks value AND type | `"5" === 5` → `false` |

### 🧠 Logical Operators

| Operator | Name | Behavior |
|:---:|---|---|
| `&&` | AND | True only if **both** conditions are true |
| `\|\|` | OR | True if **at least one** condition is true |
| `!` | NOT | Inverts the boolean |

---

## ✅❌ Truthy & Falsy Values

Non-boolean values are treated as truthy or falsy inside conditions like `if`.

| Falsy Values | Everything Else |
|---|---|
| `0`, `""` (empty string), `null`, `undefined`, `NaN`, `false` | ✅ **Truthy** (e.g., `1`, non-empty strings, `true`) |

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Primitive types | Single-value building blocks (Number, String, Boolean, etc.) |
| Non-primitive types | Structures grouping values (Object, Array, Function) |
| `typeof` | Checks a value's data type |
| `==` vs `===` | Loose vs. strict equality comparison |
| Truthy/Falsy | How non-boolean values behave in conditions |

---

### 🛠️ MLOps Perspective: Type Safety & Data Validation
> [!IMPORTANT]
> The `==` vs `===` distinction is one of the most important lessons in data engineering:
> - In Python/pandas, comparing `df["label"] == 1` when `"label"` is accidentally a string column (`"1"`) silently produces wrong results — this is the Python equivalent of `==` (loose) comparison causing a bug.
> - Understanding **truthy/falsy** is key when writing model serving validation code: `if (!prediction)` catches `null`, `undefined`, `0`, and empty string all at once — a common pattern for catching failed inference results.
> - **`null` vs `undefined`:** In an ML API response, `null` means "the field exists but has no value" (model returned nothing), while `undefined` means "the field was never part of the response schema" — critical difference for debugging.

---

<div align="center">

⬅️ [Previous: Section 1 — Foundations & Variables](./01_foundations_variables.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 3 — Control Flow](./03_control_flow.md)

</div>
