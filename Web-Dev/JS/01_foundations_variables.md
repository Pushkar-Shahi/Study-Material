<div align="center">

# <span style="color:#2E8B57">🟢 Section 1 — Foundations & Variables</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Storing_Data-2E8B57)

</div>

---

## 📦 What Is a Variable?

A variable is like a **container or "box"** used to store data values.

| Step | Meaning | Example |
|---|---|---|
| **Declaration** | Creating the variable box | `let age;` |
| **Initialization** | Putting a value inside the box | `age = 24;` |
| **Both at once** | Declare + initialize together | `let age = 24;` |

---

## 🔑 The Three Keywords: `var`, `let`, `const`

| Keyword | Re-declare? | Re-assign (update)? | Notes |
|:---:|:---:|:---:|---|
| `var` | ✅ | ✅ | Old-style, avoid in modern JS |
| `let` | ❌ | ✅ | Standard for values that change |
| `const` | ❌ | ❌ | "Locked" — use for values that never change |

```js
var x = 1;   // can redeclare and reassign
let y = 2;   // can reassign, cannot redeclare
const z = 3;  // cannot redeclare or reassign
```

---

## 📝 Variable Naming Rules & Conventions

| Rule | Detail |
|---|---|
| ✅ Start characters | Letter, underscore (`_`), or dollar sign (`$`) — **never** a number |
| ❌ Reserved words | Can't use `let`, `var`, `const`, etc. as names |
| ⚠️ Case sensitivity | `name`, `Name`, and `NAME` are **three different** variables |
| 🐪 camelCase | Standard convention for multi-word names (e.g., `collegeName`) |

```js
let mobileNumber = "9876543210";   // ✅ camelCase
let _privateVar = "secret";         // ✅ starts with underscore
let $price = 99;                     // ✅ starts with $
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Declaration vs. Initialization | Creating a variable vs. giving it a value |
| `var` / `let` / `const` | Three ways to declare, each with different rules |
| Naming rules | Valid characters and reserved word restrictions |
| camelCase | Standard multi-word naming convention |

---

### 🛠️ MLOps Perspective: Variables in Data Pipelines
> [!NOTE]
> The `const` vs `let` discipline is a best practice in **any** language:
> - In Python ML code, using constants (`MODEL_VERSION = "v2.1"`) instead of magic numbers scattered through your pipeline prevents subtle bugs when deploying to production.
> - `const` in JS is identical in spirit to Python's convention of UPPERCASE constants — immutable config values like API keys, model thresholds, and endpoint URLs should never be reassigned mid-run.

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 2 — Data Types & Operators](./02_data_types_operators.md)

</div>
