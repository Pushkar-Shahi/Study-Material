<div align="center">

# <span style="color:#1E6FEB">🔵 Phase 2 — Conditionals</span>

![Phase](https://img.shields.io/badge/Phase-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_Decision_Making-1E6FEB)

</div>

---

## 🔀 The `if-else` Statement

Runs one block of code if a condition is true, otherwise runs the `else` block.

```cpp
int n;
cin >> n;
if (n % 2 == 0) cout << "Even";
else cout << "Odd";
```

### 🔍 Relational Operators
| Operator | Meaning |
|:---:|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` `<` | Greater / Less than |
| `>=` `<=` | Greater/Less than or equal to |

---

## 🧠 Logical Operators — Combining Conditions

| Operator | Name | Behavior | Example |
|:---:|---|---|---|
| `&&` | AND | **Both** conditions must be true | 4-digit number: `n >= 1000 && n <= 9999` |
| `\|\|` | OR | **At least one** condition true | Divisible by 5 or 3: `n % 5 == 0 \|\| n % 3 == 0` |

---

## ⚡ The Ternary Operator

A concise, single-line version of `if-else`:

```cpp
condition ? expression_if_true : expression_if_false;
```

```cpp
int max = (a > b) ? a : b;
```

---

## 🔄 Switch Case

Better than long `if-else` chains when checking **one variable** against many specific values (e.g., day of the week).

```cpp
switch (day) {
    case 1: cout << "Monday"; break;
    case 2: cout << "Tuesday"; break;
    default: cout << "Invalid day";
}
```

---

## 🔗 Nested If-Else

An `if` statement placed inside another `if` — useful for multi-step logic like finding the **greatest of three numbers**.

```cpp
if (a > b) {
    if (a > c) cout << a << " is greatest";
    else cout << c << " is greatest";
} else {
    if (b > c) cout << b << " is greatest";
    else cout << c << " is greatest";
}
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `if / else` | Branch code based on a condition |
| `&&` / `\|\|` | Combine multiple conditions |
| Ternary `?:` | One-line if-else |
| `switch` | Efficient multi-value checks on one variable |
| Nested if | Handle multi-level decision logic |

---

### 🛠️ MLOps Perspective: Conditionals in Production Systems
> [!NOTE]
> Conditional logic is at the heart of every MLOps decision system:
> - **Model routing:** `if (confidence > 0.9) use_model_A; else use_model_B;` — this is A/B testing at its core
> - **Data validation:** Before feeding data to a model, validate ranges (`if (age < 0 || age > 120) reject_record()`)
> - **Health checks:** Pipeline health checks use conditionals to decide whether to trigger alerts or rollbacks
> - The **ternary operator** is heavily used in Python too (`value = a if condition else b`) — same concept, different syntax

---

<div align="center">

⬅️ [Previous: Phase 1 — Building Blocks](./01_building_blocks.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Phase 3 — Loops](./03_loops.md)

</div>
