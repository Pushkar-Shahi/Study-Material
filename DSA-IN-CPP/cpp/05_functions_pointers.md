<div align="center">

# <span style="color:#C0392B">🔴 Phase 5 — Functions & Pointers</span>

![Phase](https://img.shields.io/badge/Phase-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Modular_Code_%26_Memory-C0392B)

</div>

---

## 🧩 Functions — Modular Code

Functions let you reuse pieces of code instead of rewriting them.

### 📝 Syntax
```cpp
int add(int a, int b) {   // return type, name, parameters
    return a + b;
}
```

| Component | Role |
|---|---|
| Return type | `int`, `float`, `void`, etc. |
| Name | Identifier for the function |
| Parameters | Optional inputs |

### 🔄 Return Type
| Type | Meaning |
|---|---|
| `void` | Function doesn't return a value |
| `int` (or other) | Function returns a value of that type |

---

## 🌍 Scope

| Scope Type | Where It's Accessible |
|---|---|
| **Local** | Only inside the function/block `{ }` it's declared in |
| **Global** | Accessible **everywhere** in the program |

---

## 🔀 Function Overloading (Preview)

Multiple functions can share the **same name** if they take different types/numbers of arguments.
> Full breakdown in [Phase 6 — Advanced Topics](./06_advanced_topics.md).

---

## 🧠 Pointers — Memory Management

A pointer stores the **memory address** of another variable.

### 🔑 Key Operators
| Operator | Name | Purpose |
|:---:|---|---|
| `&` | Address-of | Gets the memory address of a variable |
| `*` | Dereference | Accesses/changes the value at that address |

```cpp
int x = 21;
int* ptr = &x;    // ptr stores the address of x
cout << *ptr;      // dereference → prints 21
*ptr = 50;          // changes x to 50 directly
```

---

## 🔗 Pass by Reference

Passing a variable's **address** (via pointers) to a function lets you modify the **original variable**, not just a copy.

```cpp
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    swap(&x, &y);   // pass addresses
    cout << x << " " << y;   // → 10 5
}
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Functions | Reusable, modular blocks of code |
| Return type | Defines what a function sends back |
| Local vs. Global scope | Controls variable accessibility |
| `&` / `*` | Get address / access value at address |
| Pass by reference | Modify the original variable via its address |

---

### 🛠️ MLOps Perspective: Pointers, Memory & Model Serving
> [!IMPORTANT]
> Pointers and memory management are directly relevant to MLOps performance engineering:
> - **Python's reference system** is conceptually identical to C++ pointers — when you pass a NumPy array to a function, you're passing a reference (not a copy), so modifications affect the original
> - **Zero-copy inference:** High-performance model servers (like NVIDIA Triton) use shared memory pointers to pass data between processes without copying — understanding pointers explains how this works
> - **Memory leaks in long-running servers:** A model serving API that runs for days can accumulate memory leaks. Understanding pointer ownership (who is responsible for freeing memory) is how you debug these
> - **C++ extensions (pybind11):** When writing custom CUDA kernels or high-performance Python extensions, you work directly with raw pointers

---

<div align="center">

⬅️ [Previous: Phase 4 — Pattern Printing](./04_pattern_printing.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Phase 6 — Advanced Topics](./06_advanced_topics.md)

</div>
