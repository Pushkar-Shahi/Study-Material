<div align="center">

# <span style="color:#D4A017">🟡 Section 3 — Control Flow</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Decisions_%26_Repetition-D4A017)

</div>

---

## 🔀 1. Conditionals (Making Decisions)

### `if / else if / else`

```js
let day = "fri";

if (day === "mon") {
    console.log("1st day of the week");
} else if (day === "tue") {
    console.log("2nd day of the week");
} else if (day === "fri") {
    console.log("5th day of the week"); // ✅ This runs
} else {
    console.log("Wrong day");
}
```

> [!TIP]
> JavaScript checks each condition top-to-bottom and runs only the **first** one that's true.

### 🔗 Nested if...else

An `if` inside another `if` — e.g., checking if a user is logged in, then checking if they're subscribed.

> [!WARNING]
> Too many nested levels quickly hurts readability.

### 🔄 The `switch` Statement

Better than long `else if` chains when comparing **one variable** against many values.

```js
switch (day) {
    case "mon":
        console.log("1st day of the week");
        break;
    case "tue":
        console.log("2nd day of the week");
        break;
    default:
        console.log("Wrong day");
}
```

| Keyword | Role |
|---|---|
| `case` | Defines a value to match |
| `break` | Stops execution and exits the switch — **critical!** |
| `default` | Runs if no case matches (like a final `else`) |

> [!WARNING]
> Forgetting `break` causes **"fall-through"** — JS keeps executing the next cases even if they don't match.

---

## 🔁 2. Loops (Repeating Tasks)

### `for` Loop — Known Iteration Count

```
for (initialization; condition; update) { ... }
```

```js
for (let i = 1; i < 10; i++) {
    console.log("hello");   // prints "hello" 9 times
}
```

| Part | Runs When |
|---|---|
| Initialization | Once, at the very start |
| Condition | Before **every** iteration |
| Update | At the end of **every** iteration |

### `while` Loop — Unknown Iteration Count

```js
let i = 1;              // Initialization
while (i <= 5) {          // Condition
    console.log(i);
    i++;                    // Update — must be inside the loop
}
```

> [!WARNING]
> You must initialize the counter **outside** and update it **inside** — otherwise, infinite loop.

### `do...while` Loop — Runs At Least Once

```js
let i = 1;
do {
    console.log(i);   // Runs once, prints 1
    i++;
} while (false);        // Condition checked AFTER the block runs
```

| Loop | Condition Checked | Runs At Least Once? |
|---|:---:|:---:|
| `for` / `while` | Before | ❌ |
| `do...while` | After | ✅ |

---

## 🎮 3. Loop Control: `break` and `continue`

| Keyword | Effect |
|---|---|
| `break` | Instantly terminates the entire loop |
| `continue` | Skips the rest of the current iteration, jumps to the update step |

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `if / else if / else` | Branch code based on conditions |
| `switch` | Efficient multi-value checks on one variable |
| `for` | Repeat a known number of times |
| `while` | Repeat while a condition holds (checked first) |
| `do...while` | Same as while, but guarantees at least one run |
| `break` / `continue` | Control loop flow from the inside |

---

### 🛠️ MLOps Perspective: Control Flow in Pipelines
> [!NOTE]
> Control flow structures directly mirror the logic in ML pipeline orchestrators (like Apache Airflow or Prefect):
> - **`if / else`** is how you write **branching DAGs** — if the model's validation accuracy exceeds a threshold, deploy; else, retrain.
> - **`for` loops** are how you process every file in a dataset directory, every record in a batch, or every experiment in a hyperparameter sweep.
> - **`break`** maps directly to **early stopping** in model training — stop iterating over epochs when the validation loss stops improving.

---

<div align="center">

⬅️ [Previous: Section 2 — Data Types & Operators](./02_data_types_operators.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 4 — Functions](./04_functions.md)

</div>
