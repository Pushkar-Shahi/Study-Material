<div align="center">

# <span style="color:#3498DB">🟦 Level 2: Scope & Closures</span>

![Level](https://img.shields.io/badge/Level-2-3498DB?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Variable%20Access-3498DB?style=flat-square)

</div>

---

## 🔍 What Is Scope?

**Scope** = *where a variable can be accessed from.*

A variable declared inside one block/function may or may not be visible to another — this depends on **where** it was declared, not where it's called.

---

## 🔒 Function Scope Is Independent

Each function call creates its **own fresh local scope**.

```javascript
function counter() {
    let count = 0;
    count = count + 1;
    console.log(count);
}

counter(); // 1
counter(); // 1  (independent — resets every call, no shared memory)
```

> 💡 Because `count` is declared **inside** `counter()`, each call starts fresh — the calls don't affect each other.

### Global Scope Persists

```javascript
let count = 0; // global

function counter() {
    count = count + 1; // modifies the outer/global variable
    console.log(count);
}

counter(); // 1
counter(); // 2  (shared global state — persists across calls)
```

### Local Shadows Global

```javascript
let count = 2; // global

function counter() {
    let count = 0;      // local — shadows the global one
    count = count + 2;
    console.log(count); // 2 (uses the LOCAL count, not global)
}

counter();
counter();
```

> ⚠️ **Gotcha:** When a local variable has the **same name** as a global one, the local one takes priority *inside that scope*.

---

## ⏳ Temporal Dead Zone (TDZ)

**Temporal** = time-related. The TDZ is the gap between a variable's **creation** and its **execution** (assignment).

```javascript
// Creation phase:   b → (in TDZ, not yet usable)
// Execution phase:  b → 10 (now accessible)
let b = 10;
```

| Phase | State of `let`/`const` variable |
|-------|----------------------------------|
| Creation | Exists but is **uninitialized** — in the TDZ |
| Execution | Assigned its actual value — now usable |

> ⚠️ Accessing a `let`/`const` variable **before** its declaration line throws a `ReferenceError` — this window is the Temporal Dead Zone.

```javascript
function random() {
    console.log(x); // ❌ TDZ error if x is declared with let below
    let x = 3;
}
```

---

## 🌐 Lexical Scoping & Lexical Environment

**Lexical scoping**: a function's access to variables is determined by **where it was written (defined)**, not where it's called from.

```javascript
let city = "Delhi";

function printCity() {
    console.log(city);
}

function random(fn) {
    let city = "Varanasi";
    fn(); // fn = printCity, called here
}

random(printCity); // "Delhi" — NOT "Varanasi"!
```

> 💡 `printCity` remembers the `city` from **where it was defined** (global scope, `"Delhi"`) — not the `city` in the scope where it's *invoked*. This is the essence of lexical scoping, and `printCity` acts here as a **callback function**.

---

## 🔗 Closures

A **closure** = an inner function **+** the lexical environment (variables) of its parent — remembered even after the parent function has finished executing.

```javascript
function outer() {
    function inner() {
        return log; // uses a variable from outer's scope
    }
    return inner; // return the function definition itself (not inner())
}

console.log(outer()()); // outer() returns inner, then () calls it
```

| Term | Meaning |
|------|---------|
| Inner function | Function defined inside another function |
| Closure | Inner function + captured variables from parent's environment |
| `return inner` | Returns the function **definition** (copy), to be called later |
| `return inner()` | Calls it immediately — returns its result, not the function |

---

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| Scope | Determines where a variable is accessible |
| Function scope | Local variables reset on every call |
| Global scope | Shared state, persists across calls |
| Shadowing | Local variable overrides a global one with the same name |
| TDZ | Window where `let`/`const` exist but can't be accessed yet |
| Lexical scoping | Access is based on **where code is written**, not called |
| Closure | Function + remembered parent environment |

---

[⬅️ Previous: Arrays & Objects](01_arrays_objects.md) | [🏠 Roadmap](00_README.md) | [➡️ Next: Execution Context & Hoisting](03_execution_context_hoisting.md)
