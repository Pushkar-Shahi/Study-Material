<div align="center">

# <span style="color:#E07B00">🟠 Section 4 — Functions</span>

![Section](https://img.shields.io/badge/Section-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Reusable_Code-E07B00)

</div>

---

## 🧩 What Is a Function?

A **reusable block of code** designed to perform a specific task — define it once, "call" it whenever needed.

---

## 🔤 1. Parameters vs. Arguments

| Term | Meaning |
|---|---|
| **Parameter** | Placeholder variable defined in the function |
| **Argument** | The actual value passed in when calling the function |

### 🛡️ Default Parameters

```js
function greetingMsg(userName = "Guest", greetings = "Hii") {
    console.log(`${greetings}, ${userName}`);
}

greetingMsg("Priyanshu");   // → Hii, Priyanshu
greetingMsg();               // → Hii, Guest (falls back to defaults)
```

---

## 📤 2. Returning Values

Use `return` to send a value back out of the function.

```js
function totalMarks(mathMarks, scienceMarks) {
    return mathMarks + scienceMarks;
}

let score = totalMarks(46, 56);   // score = 102
```

> [!WARNING]
> If a function has **no** `return` statement, it automatically returns `undefined`.

---

## 3️⃣ Three Ways to Write Functions

### A. Function Declaration

```js
function fun1() {
    console.log("function declaration");
}
```

> [!TIP]
> **Hoisting:** You can call this **before** it's written in your file — JS automatically hoists it to the top.

### B. Function Expression

```js
let add = function (num1, num2) {
    return num1 + num2;
};
```

> [!WARNING]
> Cannot be called before it's initialized — doing so throws an error (no hoisting benefit).

### C. Arrow Functions

```js
const add = (num1, num2) => num1 + num2;
```

| Feature | Detail |
|---|---|
| No parentheses | Optional if there's exactly **one** parameter |
| Implicit return | Single-line functions skip `return` and `{ }` entirely |
| Explicit return | Multi-line functions **must** use `{ }` and `return` |

```js
const square = x => x * x;              // implicit return, single param

const complex = (a, b) => {                // explicit return, multi-line
    let sum = a + b;
    return sum * 2;
};
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Parameters vs. Arguments | Placeholders vs. actual passed-in values |
| Default parameters | Fallback values when no argument is given |
| `return` | Sends a value back to the caller |
| Function Declaration | Traditional syntax — supports hoisting |
| Function Expression | Function stored in a variable — no hoisting |
| Arrow Function | Shorter modern syntax, supports implicit return |

---

### 🛠️ MLOps Perspective: Functions as Pipeline Steps
> [!IMPORTANT]
> Functions are the atom of clean MLOps code:
> - Every well-structured ML pipeline is a series of functions: `load_data()`, `preprocess()`, `train_model()`, `evaluate()`, `push_to_registry()`.
> - **Arrow functions** in JS are like Python's **lambda functions** — used for quick, single-purpose transformations (e.g., mapping a list of filenames, filtering records).
> - **Default parameters** map directly to `argparse` defaults or `Hydra` config defaults in Python ML projects — defining sensible fallbacks so your training script works even without explicit arguments.

---

<div align="center">

⬅️ [Previous: Section 3 — Control Flow](./03_control_flow.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 5 — Data Structures](./05_data_structures.md)

</div>
