<div align="center">

# <span style="color:#F1C40F">🟨 Level 3: Execution Context & Hoisting</span>

![Level](https://img.shields.io/badge/Level-3-F1C40F?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-How%20JS%20Runs-F1C40F?style=flat-square)

</div>

---

## ⚙️ How Does JS Execute Internally?

Every piece of running JS code lives inside an **Execution Context** — the environment where JS actually executes.

Each execution context runs in **two phases**:

| Phase | What Happens |
|-------|---------------|
| 🏗️ Creation | Memory is allocated; `var` → `undefined`, `let`/`const` → TDZ |
| ▶️ Execution | Code runs line by line; variables get their real values |

---

## 🌍 The Global Execution Context

```javascript
var a = 5;
let b = 10;
console.log(a + b);
```

| Phase | `a` | `b` | Output |
|-------|-----|-----|--------|
| Creation | `undefined` | *(TDZ)* | — |
| Execution | `5` | `10` | `console.log(15)` |

---

## 🧱 Function Execution Contexts

**Every function call creates its own, brand-new execution context** (with its own creation + execution phases).

```javascript
function fun1() {
    let num1 = 10;
    let num2 = 20;
    return num1 + num2;
}

const result = fun1();
console.log(result); // 30
```

| Phase (inside `fun1`) | `num1` | `num2` | Result |
|------------------------|--------|--------|--------|
| Creation | `10` *(assigned during creation in this walkthrough)* | `20` | — |
| Execution | `10` | `20` | `return 30` |

### Nested Function Calls

```javascript
function outer() {
    let num1 = 10;
    let num2 = 20;

    function inner() {
        let num1 = 50;
        let num2 = 60;
        return num1 + num2;
    }

    const result = inner() + num1 + num2;
    return result;
}

const result = outer();
console.log(result); // 140
```

> 💡 Calling `outer()` creates the **global** context first, then a **new context for `outer`**, then another **new context for `inner`** — each nested inside the last.

---

## 📚 The Call Stack

The call stack tracks *which execution context is currently running*, using **LIFO** (Last In, First Out) — like a stack of books.

| Operation | Meaning |
|-----------|---------|
| **Push** | A new function call is added to the top of the stack |
| **Pop** | A finished function call is removed from the top |

```
push →  [ inner ]
        [ outer ]
        [ global ]
```

The last function pushed is the first one popped off once it finishes.

---

## 🪜 Hoisting

JS "hoists" declarations to the top of their scope during the **creation phase** — but *how much* gets hoisted differs.

```javascript
fun2(); // ❌ TypeError: fun2 is not a function

var fun2 = function () {
    console.log("hello");
};
```

> ⚠️ **Gotcha:** `var fun2` is hoisted, but only the **declaration** — its value is `undefined` at that point. Calling `undefined()` throws **`TypeError: fun2 is not a function`**.

| Declared As | Hoisting Behavior |
|-------------|---------------------|
| `function fun2(){}` (declaration) | Fully hoisted — callable before its line |
| `var fun2 = function(){}` (expression) | Only the `var` name hoisted (as `undefined`), not the value |
| `let` / `const` | Hoisted into the TDZ — inaccessible until declared |

---

## 🔁 Recursion & Stack Overflow

```javascript
function recurse() {
    recurse();
}

recurse();
```

```
Uncaught RangeError: Maximum call stack size exceeded
  at recurse (index.js:58:5)
  at recurse (index.js:58:5)
  at recurse (index.js:58:5)
  ...
```

> ⚠️ **Gotcha:** A recursive function with **no base case / exit condition** keeps pushing new execution contexts onto the call stack until it overflows.

---

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| Execution Context | Environment where JS code runs |
| Creation Phase | Memory allocated for variables/functions |
| Execution Phase | Code actually runs, values assigned |
| Call Stack (LIFO) | Tracks active execution contexts via push/pop |
| Hoisting | Declarations moved to top of scope during creation |
| Function declaration vs expression | Declarations fully hoisted; expressions are not |
| Stack overflow | Result of uncontrolled recursion filling the call stack |

---

[⬅️ Previous: Scope & Closures](02_scope_closures.md) | [🏠 Roadmap](00_README.md) | [➡️ Next: `this` & Coercion](04_this_coercion.md)
