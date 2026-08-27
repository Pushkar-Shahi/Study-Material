<div align="center">

# <span style="color:#C0392B">🔴 Section 5 — Data Structures</span>

![Section](https://img.shields.io/badge/Section-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Grouping_Data-C0392B)

</div>

---

## 📋 1. Arrays (Ordered Lists)

An **ordered collection** written with square brackets `[]`.

```js
let products = ["tshirt", "lower", "cap"];
```

### 🔢 Indexing & Length

| Concept | Detail |
|---|---|
| Zero-indexed | First item is at index `0` |
| Access an item | `products[0]` → `"tshirt"` |
| `.length` | Number of items in the array |
| Last index | Always `length - 1` |

### 🔧 Modifying Arrays — The 4 Core Methods

| Method | Effect |
|---|---|
| `push(item)` | Adds an item to the **end** |
| `pop()` | Removes the **last** item |
| `unshift(item)` | Adds an item to the **start** |
| `shift()` | Removes the **first** item |

### 🔗 Nested Arrays

```js
let products = [["tshirt", 566], ["lower", 543]];
console.log(products[0][0]);   // → "tshirt"
```

### 🔁 Looping Through Arrays

| Method | Syntax |
|---|---|
| **Traditional `for`** | `for(let i = 0; i < products.length; i++) { ... }` |
| **`for...of`** | `for (let value of products) { ... }` |
| **`.forEach()`** | `products.forEach(function(value, index) { ... })` |

```js
// for...of — grabs values directly, no index needed
for (let value of products) {
    console.log(value);
}
```

---

## 🗂️ 2. Objects (Key-Value Collections)

An **unordered collection** of properties, written with curly braces `{}`.

```js
let product2 = {
    name: "iphone",
    price: 57633,
    avgRating: 4.5
};
```

> [!NOTE]
> Keys are always strings (or auto-converted). Values can be **anything** — numbers, strings, booleans, arrays, other objects, even functions.

### 🔑 Accessing Properties

| Notation | Syntax | Best For |
|---|---|---|
| **Dot notation** | `product2.name` | Most common, readable |
| **Bracket notation** | `product2["name"]` | When the key is stored in a variable |

```js
let keyName = "price";
console.log(product2[keyName]);   // → 57633
```

### 🛠️ Object Helper Methods

| Method | Returns |
|---|---|
| `Object.keys(obj)` | Array of all keys |
| `Object.values(obj)` | Array of all values |
| `for...in` loop | Iterates over all keys |

---

## 🎁 3. Destructuring & Rest/Spread (`...`)

### 📦 Destructuring — Unpack Into Variables

```js
const [name, price] = ["iphone", 56835];
// name = "iphone", price = 56835
```

### 🌊 Spread Operator — Unpack/Expand Elements

Used to spread out elements, e.g., combining arrays.

### 📦 Rest Operator — Pack Remaining Elements

```js
const [n, p, ...hello] = ["iphone", 56835, 4.5, 75, 10];
// hello = [4.5, 75, 10]
```

| Operator | Symbol | Direction |
|---|:---:|---|
| Spread | `...` | Expands a collection into individual elements |
| Rest | `...` | Collects remaining elements into an array |

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Array `[]` | Ordered, indexed list of values |
| `push/pop/shift/unshift` | Add/remove items from either end |
| `for`, `for...of`, `.forEach()` | Three ways to loop through an array |
| Object `{}` | Key-value pairs for real-world entities |
| Dot vs. Bracket notation | Two ways to access object properties |
| `Object.keys()` / `Object.values()` | Extract keys or values as arrays |
| Destructuring | Unpack array/object values into variables |
| Spread / Rest (`...`) | Expand or collect elements |

---

### 🛠️ MLOps Perspective: The Foundation of JSON & APIs
> [!IMPORTANT]
> JS Arrays and Objects are the direct equivalent of Python **lists** and **dictionaries** — and they are the backbone of every ML API:
> - **JSON is just JS Objects:** When your FastAPI ML model returns a prediction, it returns JSON — which is literally a JS object. `{ "label": "cat", "confidence": 0.97 }`.
> - **Array of predictions:** Batch inference returns an array: `[{"label": "cat"}, {"label": "dog"}]` — looping through this with `.forEach()` or `for...of` is how your frontend renders each result.
> - **Destructuring in API responses:** `const { label, confidence } = apiResponse;` is an extremely common pattern for cleanly extracting prediction fields from your model's JSON response without accessing `apiResponse.label` and `apiResponse.confidence` separately every time.
> - **Spread operator:** Used to merge model metadata objects — `const fullResult = { ...modelInfo, ...prediction }` — combining the model version info with the actual prediction into one clean object to log.

---

<div align="center">

⬅️ [Previous: Section 4 — Functions](./04_functions.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full JavaScript Roadmap!

</div>
