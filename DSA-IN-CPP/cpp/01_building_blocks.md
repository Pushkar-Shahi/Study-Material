<div align="center">

# <span style="color:#2E8B57">🟢 Phase 1 — The Building Blocks</span>

![Phase](https://img.shields.io/badge/Phase-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Core_Syntax-2E8B57)

</div>

---

## 📤 Output & Input

| Operator | Purpose |
|---|---|
| `cout <<` | Display output |
| `cin >>` | Take input from the user |

```cpp
int a, b;
cout << "Enter 1st number: ";
cin >> a;
cout << "Enter 2nd number: ";
cin >> b;
cout << "The sum is: " << a + b;
```

---

## 📦 Variables & Data Types

| Type | Stores | Example |
|---|---|---|
| `int` | Integers | `21` |
| `float` / `double` | Real (decimal) numbers | `3.14` |
| `char` | Single character | `'A'`, `'z'` |

> [!TIP]
> To calculate the area of a circle, declare `radius` and `area` as `float`, then use `cin >> radius` to get input.

### 📝 Variable Naming Rules
- ✅ Must start with a **letter** or **underscore (`_`)**
- ❌ No special characters (like `@`, `#`, `-`) except underscore
- ❌ No spaces or commas
- ❌ Cannot use keywords (like `int`, `float`) as names

---

## ➗ Integer Division vs. Modulus

```cpp
5 / 2   // → 2   (integer division truncates the decimal)
5 % 2   // → 1   (modulus gives the remainder)
```

> [!WARNING]
> Dividing two integers **always** returns an integer. Need decimal precision? Use `float` or `double`.

---

## 🔤 The `char` Type & ASCII

Characters are internally represented as integers called **ASCII values**.

| Character | ASCII Value |
|:---:|:---:|
| `'a'` | 97 |
| `'A'` | 65 |
| `'0'` | 48 |
| `'1'` | 49 |

```cpp
char c = 'a';
cout << (int)c;   // typecast → prints 97
```

> [!NOTE]
> Because characters map to numbers, you can do math with them — adding two `char` variables adds their ASCII values.

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `cout` / `cin` | Basic output and input |
| `int`, `float`, `double`, `char` | Core data types |
| Naming rules | Valid variable identifiers |
| `/` vs `%` | Integer division vs. remainder |
| ASCII | Numeric backbone of the `char` type |

---

### 🛠️ MLOps Perspective: C++ Data Types & ML
> [!NOTE]
> Data types in C++ map directly to types used in ML model inference:
> - `float` (32-bit) is the default precision for model weights — most deep learning models use `float32`
> - `double` (64-bit) is used for high-precision scientific computing
> - Understanding integer vs. float division prevents subtle bugs when computing metrics like accuracy (`correct / total` returns `0` if both are `int`!)
> - ASCII knowledge is foundational for NLP — text tokenizers often work at the character/byte level

---

<div align="center">

🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Phase 2 — Conditionals](./02_conditionals.md)

</div>
