<div align="center">

# 🟦 <span style="color:#2563EB">Level 02: Data Structures & Built-ins</span>

> *Core programming primitives in JavaScript: reusable function abstractions, Math and String utilities, array manipulations, higher-order methods, and key-value object dictionaries.*

[![Level 02](https://img.shields.io/badge/Level--02-2563EB?style=for-the-badge&logo=codeforces&logoColor=white)](02_data_structures_and_builtins.md)
[![Theme](https://img.shields.io/badge/Theme-Data%20Structures%20%26%20Built--ins-2563EB?style=for-the-badge)](02_data_structures_and_builtins.md)
[![Lectures](https://img.shields.io/badge/Source-Lec%2031%2C%2032%2C%2033%2C%2034-grey?style=for-the-badge)](02_data_structures_and_builtins.md)

---

</div>

## 📌 Table of Contents
- [1. Functions & Reusable Logic](#1-functions--reusable-logic)
- [2. The Built-in Math Object](#2-the-built-in-math-object)
- [3. String Manipulation & Parsing](#3-string-manipulation--parsing)
- [4. Arrays & Index-Based Operations](#4-arrays--index-based-operations)
- [5. Higher-Order Array Methods](#5-higher-order-array-methods)
- [6. Objects & Key-Value Dictionaries](#6-objects--key-value-dictionaries)
- [🎯 Practice Problems](#-practice-problems)
- [🧭 Summary Table](#-summary-table)

---

## 1. Functions & Reusable Logic

A **function** is a reusable, self-contained block of statements designed to perform a distinct calculation or action.

### Function Syntaxes Compared

| Syntax Style | Example | Hoisting Behavior | `this` Binding |
| :--- | :--- | :--- | :--- |
| **Declaration** | `function add(a, b) { return a + b; }` | Fully hoisted to top of scope | Dynamic (caller-based) |
| **Expression** | `const add = function(a, b) { return a + b; };` | Variable hoisted in TDZ | Dynamic (caller-based) |
| **Arrow Function** | `const add = (a, b) => a + b;` | Variable hoisted in TDZ | Lexical (inherits from outer scope) |

### Parameters, Arguments & Default Values

```javascript
// Function definition: 'price' and 'discountPercent' are Parameters
// discountPercent has a default fallback value of 10
function calculateDiscount(price, discountPercent = 10) {
  const discountAmount = (price * discountPercent) / 100;
  const finalPrice = price - discountAmount;
  return finalPrice; // Explicit return exits function and passes value back
}

// Function invocation: 2000 and 5 are Arguments
const finalBill = calculateDiscount(2000, 5); // Returns 1900
console.log(`Final Price: Rs ${finalBill}`);

// Using default parameter
const defaultBill = calculateDiscount(1000);  // Uses discountPercent = 10 -> 900
console.log(`Default Discount Bill: Rs ${defaultBill}`);
```

> [!NOTE]
> Functions without an explicit `return` statement return `undefined` by default.

---

## 2. The Built-in Math Object

JavaScript includes a built-in static `Math` object with mathematical constants and functions:

| Method | Description | Example | Result |
| :--- | :--- | :--- | :---: |
| `Math.abs(x)` | Absolute (positive) magnitude of `x` | `Math.abs(-5)` | `5` |
| `Math.round(x)` | Rounds to the nearest integer | `Math.round(4.6)` | `5` |
| `Math.floor(x)` | Rounds down towards negative infinity | `Math.floor(4.9)` | `4` |
| `Math.ceil(x)` | Rounds up towards positive infinity | `Math.ceil(4.1)` | `5` |
| `Math.min(...n)`| Returns the lowest numerical argument | `Math.min(10, 5, 20)` | `5` |
| `Math.max(...n)`| Returns the highest numerical argument | `Math.max(10, 5, 20)` | `20` |
| `Math.pow(b, e)`| Computes base `b` raised to exponent `e` | `Math.pow(2, 3)` | `8` |
| `Math.sqrt(x)` | Square root of `x` | `Math.sqrt(25)` | `5` |

### Random Generation Formula

`Math.random()` returns a floating-point number in the range `[0, 1)` (including `0`, but excluding `1`). To generate a random integer within an inclusive range `[min, max]`:

$$\text{Random Integer} = \lfloor \text{Math.random}() \times (\text{max} - \text{min} + 1) \rfloor + \text{min}$$

```javascript
// Random dice roll between 1 and 6
function rollDice() {
  const min = 1;
  const max = 6;
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Random token between 50 and 100
function getRandomToken(min = 50, max = 100) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(`Dice output: ${rollDice()}`);
```

---

## 3. String Manipulation & Parsing

Strings are zero-indexed sequences of UTF-16 character codes. Strings in JavaScript are **immutable**; all string methods return new strings rather than modifying the original.

### Common String Methods

| Method | Behavior | Example | Output |
| :--- | :--- | :--- | :--- |
| `.length` | Property returning character count | `"JavaScript".length` | `10` |
| `.toUpperCase()` | Returns all uppercase string | `"hello".toUpperCase()` | `"HELLO"` |
| `.toLowerCase()` | Returns all lowercase string | `"HELLO".toLowerCase()` | `"hello"` |
| `.trim()` | Strips leading and trailing whitespace | `"  user@mail.com  ".trim()` | `"user@mail.com"` |
| `.includes(sub)` | Tests substring presence (returns boolean) | `"avatar.png".includes(".png")` | `true` |
| `.indexOf(sub)` | First index of substring or `-1` | `"Hello".indexOf("l")` | `2` |
| `.slice(s, e)` | Extracts characters from `s` to index `e` (exclusive) | `"JavaScript".slice(0, 4)` | `"Java"` |
| `.replace(a, b)`| Replaces first match `a` with `b` | `"Rs 100".replace("100", "200")` | `"Rs 200"` |
| `.split(sep)` | Splits string into an array of strings | `"a,b,c".split(",")` | `["a", "b", "c"]` |

```javascript
// Real-world practical validation: File Extension Checker
function isValidProfileImage(filename) {
  const lower = filename.toLowerCase().trim();
  return lower.endsWith(".png") || lower.endsWith(".jpg") || lower.endsWith(".jpeg");
}

console.log(isValidProfileImage("profile_pic.PNG")); // true
console.log(isValidProfileImage("report.pdf"));        // false
```

---

## 4. Arrays & Index-Based Operations

An **array** is an ordered, zero-indexed list of values. Elements can be of any type, including numbers, strings, objects, or nested arrays.

```javascript
const fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]); // "Apple"
console.log(fruits.length); // 3
```

### Mutating Operations (Modifies In-Place)

```javascript
const list = ["Item 1", "Item 2"];

list.push("Item 3");    // Appends to end -> ["Item 1", "Item 2", "Item 3"]
const last = list.pop(); // Removes from end -> returns "Item 3"

list.unshift("Start");   // Inserts at beginning -> ["Start", "Item 1", "Item 2"]
const first = list.shift(); // Removes from beginning -> returns "Start"
```

### Mutating `splice()` vs Non-Mutating `slice()`

Understanding the distinction between `slice()` and `splice()` is critical for state immutability:

| Feature | `slice(start, end)` | `splice(start, deleteCount, ...items)` |
| :--- | :--- | :--- |
| **Modification** | **Non-mutating**: Returns a shallow copy slice | **Mutating**: Alters original array directly |
| **Second Argument** | Ending index (exclusive) | Number of items to delete from `start` |
| **Third+ Argument** | N/A | Elements to insert at `start` index |
| **Return Value** | Selected extracted slice | Array containing deleted elements |

```javascript
const original = ["A", "B", "C", "D", "E"];

// Non-mutating slice: extracts indices 1 to 3 (exclusive)
const sliced = original.slice(1, 3);
console.log("sliced:", sliced);     // ["B", "C"]
console.log("original:", original); // ["A", "B", "C", "D", "E"] (unchanged)

// Mutating splice: at index 2, remove 1 item and insert "Z"
const spliced = original.splice(2, 1, "Z");
console.log("spliced:", spliced);   // ["C"] (the removed item)
console.log("original:", original); // ["A", "B", "Z", "D", "E"] (mutated!)
```

---

## 5. Higher-Order Array Methods

A **Higher-Order Function (HOF)** is a function that either accepts another function as an argument (a **callback**) or returns a function.

### Functional Iterators Comparison

| Method | Callback Arguments | Returns | Purpose | Mutates Source? |
| :--- | :--- | :--- | :--- | :---: |
| `forEach()` | `(item, index, arr)` | `undefined` | Side-effects (logging, DOM rendering) | ❌ |
| `map()` | `(item, index, arr)` | New array (same size) | Transforming each item | ❌ |
| `filter()` | `(item, index, arr)` | New array (subset) | Filtering items matching a condition | ❌ |
| `reduce()` | `(acc, item, index)` | Single accumulated value | Aggregating numbers, objects, or lists | ❌ |

### Method Implementations

```javascript
const products = [
  { id: 1, name: "Keyboard", price: 1500, inStock: true },
  { id: 2, name: "Mouse", price: 800, inStock: false },
  { id: 3, name: "Monitor", price: 12000, inStock: true }
];

// 1. map(): Extract product names
const productNames = products.map(product => product.name);
console.log("Product Names:", productNames); // ["Keyboard", "Mouse", "Monitor"]

// 2. filter(): Only available products
const availableProducts = products.filter(product => product.inStock);
console.log("Available:", availableProducts); // Keyboard & Monitor

// 3. reduce(): Calculate total stock valuation
const totalValue = products.reduce((acc, product) => {
  return acc + product.price;
}, 0); // 0 is initial accumulator value
console.log(`Total Inventory Value: Rs ${totalValue}`); // Rs 14300
```

> [!TIP]
> Always supply the initial accumulator value in `reduce()`. Omitting it will default `acc` to the first item of the array, leading to runtime errors when operating on arrays of objects.

---

## 6. Objects & Key-Value Dictionaries

An **object** is an unordered collection of related data stored as key-value pairs (properties and methods), mapping directly to real-world domain models.

```javascript
const product = {
  id: 101,
  name: "Wireless Headphones",
  price: 2999,
  inStock: true,
  tags: ["audio", "bluetooth"]
};
```

### Property Access: Dot Notation vs. Bracket Notation

```javascript
// 1. Dot notation: property name must be a valid identifier
console.log(product.name);  // "Wireless Headphones"

// 2. Bracket notation: requires property name as a string
console.log(product["price"]); // 2999

// 3. Dynamic property resolution via variable:
const targetKey = "inStock";
console.log(product[targetKey]); // true (evaluates variable targetKey to "inStock")
```

> [!CAUTION]
> **Common Student Confusion**:
> - `product.targetKey` looks literally for a key named `"targetKey"` (returns `undefined`).
> - `product[targetKey]` evaluates the identifier `targetKey`, looking up `product["inStock"]`.
> - Always use bracket notation when key names contain spaces, hyphens (e.g. `product["shipping-cost"]`), or come from variables!

### Property Manipulation & Utility Methods

```javascript
const user = { username: "nishant_dev", role: "admin", active: true };

// Adding & modifying properties
user.email = "nishant@example.com";
user.active = false;

// Deleting properties
delete user.role;

// Object utility helpers
console.log(Object.keys(user));   // ["username", "active", "email"]
console.log(Object.values(user)); // ["nishant_dev", false, "nishant@example.com"]
console.log(Object.entries(user));// [["username", "nishant_dev"], ...]
```

### Iterating: `for...in` vs `for...of`

| Loop Type | Primary Target | Yields During Iteration |
| :--- | :--- | :--- |
| `for...in` | **Objects** (and Arrays) | Property **keys** (or array indices as strings) |
| `for...of` | **Iterables** (Arrays, Strings, Sets, Maps) | Direct **values** |

```javascript
const car = { make: "Tata", model: "Nexon", year: 2024 };

// for...in over object
for (const key in car) {
  console.log(`${key} -> ${car[key]}`);
}

const colors = ["Red", "Green", "Blue"];

// for...of over iterable array
for (const color of colors) {
  console.log(`Color: ${color}`);
}
```

---

## 🎯 Practice Problems

1. **Array Deduplication & Calculation**:
   Given an array of cart item prices `[120, 450, 120, 800, 450]`, write an expression using `filter()` that removes duplicate prices, then use `reduce()` to sum the unique prices.
   > *Hint: Inside `filter(item, index, arr)`, compare `arr.indexOf(item) === index` to keep only the first occurrence.*

2. **Dynamic Object Counter**:
   Given an array of strings `["apple", "banana", "apple", "orange", "banana", "apple"]`, compute the frequency of each fruit as an object `{ apple: 3, banana: 2, orange: 1 }`.
   > *Hint: Use `reduce((acc, fruit) => { ... }, {})` checking whether `acc[fruit]` exists or initializing it to 0.*

---

## 🧭 Summary Table

| Concept | Purpose | Syntax Pattern |
| :--- | :--- | :--- |
| **Arrow Function** | Compact function syntax with lexical `this` | `const fn = (a, b) => a * b;` |
| **`Math.random()` Formula** | Generate random integer between `min` and `max` | `Math.floor(Math.random() * (max - min + 1)) + min` |
| **`splice()` vs `slice()`** | Mutating in-place change vs non-mutating sub-array | `arr.splice(idx, 1)` vs `arr.slice(start, end)` |
| **`map()` / `filter()`** | Transform elements / select matching elements | `arr.map(x => x * 2); arr.filter(x => x > 0);` |
| **`reduce()`** | Aggregate collection down to a single outcome | `arr.reduce((acc, curr) => acc + curr, 0)` |
| **Bracket Notation** | Access properties dynamically with variables | `obj[variableKey]` |
| **`Object.keys()`** | Extract array of property names | `Object.keys(obj)` |

---

<div align="center">

⬅️ [Level 01: Foundations & Syntax](01_foundations_and_syntax.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Level 03: Engine Mechanics & Scoping](03_execution_context_scope_and_closures.md)

</div>
