<div align="center">

# <span style="color:#2ECC71">🟩 Level 1: Arrays & Objects</span>

![Level](https://img.shields.io/badge/Level-1-2ECC71?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Structured%20Data-2ECC71?style=flat-square)

</div>

---

## 📦 Arrays: Ordered Collections

An **array** is a *built-in* ordered collection / sequence of data.

```javascript
let arr = ["1", "2", "3"];
arr[0];       // index-based access → "1"
arr.length;   // 3
```

> 💡 Arrays are accessed by **index** (position), starting at `0`.

### Array of Arrays

```javascript
let products = [["tshirt", 566], ["lower", 543], ["cap", 53], ["shoes", 673]];

console.log(products[0][0]); // "tshirt" — order dependent!
```

> ⚠️ **Gotcha:** Nested-array access is **order dependent** — readability suffers as nesting grows. This is exactly why **objects** exist.

---

## 🗂️ Objects: Key/Value Collections

An **object** is a collection of **key : value** pairs — related properties and methods grouped together (mirrors real-world entities like a "product" or "student").

```javascript
let product2 = {
    price: 57633,
    avgRating: 4.5,
    totalRevies: 75,
    discount: 10,
    name: "iphone",
};
```

| Term | Meaning |
|------|---------|
| **Key** (property) | Always a `string` |
| **Value** | Can be `Number`, `String`, `Object`, `Array`, `Boolean`, `Function`, or `null` |

---

## 🔑 Dot vs Bracket Notation

| Notation | Syntax | When to Use |
|----------|--------|-------------|
| Dot | `product.name` | Key is a fixed, known identifier |
| Bracket | `product["name"]` | Key is dynamic / stored in a variable |

```javascript
let key = "name";
product[key];     // ✅ works — dynamic lookup
product.key;      // ❌ looks for a literal property called "key"
```

> 💡 If the key comes from a **string in a variable**, dot notation won't work — you *must* use bracket notation.

### Useful Object Methods

| Method | Returns |
|--------|---------|
| `Object.keys(obj)` | Array of the object's keys |
| `Object.values(obj)` | Array of the object's values |

---

## 🔁 Looping: Arrays vs Objects

| Loop | Iterates Over | Best For |
|------|----------------|----------|
| `for...of` | **Direct values** | Arrays |
| `for...in` | **Keys / indexes** | Objects (also works on array indexes) |
| `.forEach()` | Values (+ index) via callback | Arrays — shortcut for `for...of` |

```javascript
// for...of → direct value
for (value of product1) {
    console.log(value);
}

// Classic index loop
for (let i = 0; i < product1.length; i++) {
    console.log(product1[i]);
}

// .forEach() — callback function shortcut
product1.forEach(function (value, index) {
    console.log(value, index);
});
```

> 💡 **Callback function**: a function passed *as an argument* into another function (like `forEach`), which then calls it internally.

---

## 🧩 Destructuring

Pulls values out of arrays/objects into named variables in one line.

```javascript
const [name, price, c, d] = ["iphone", 56835, 4.5, 75, 10];
console.log(price); // 56835
```

---

## 🌊 Spread & Rest Operators

Both use `...` — direction of use decides the meaning.

| Operator | Direction | Meaning |
|----------|-----------|---------|
| **Spread** | Unpacks | "Unboxes" an array/object into individual elements |
| **Rest** | Packs | Collects remaining items **back into an array** |

```javascript
let arr = [53, 15, 626, 7, 43, 57, 23, 54, 752, 43];

// Spread → unpack into individual values
console.log(...arr);

// Rest → gather leftover items into a new array
const [n, p, ...hello] = ["iphone", 56835, 4.5, 75, 10];
console.log(hello); // [4.5, 75, 10]
```

---

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| Array | Ordered, indexed sequence of data |
| Object | Key/value pairs modeling real-world entities |
| Dot notation | Access known/static keys |
| Bracket notation | Access dynamic keys (via variable) |
| `Object.keys()` / `Object.values()` | Extract keys/values as arrays |
| `for...of` | Loop over array **values** |
| `for...in` | Loop over object **keys** |
| `.forEach()` | Callback-based array iteration |
| Destructuring | Unpack array/object into variables |
| Spread `...` | Unpack a collection |
| Rest `...` | Pack remaining items into an array |

---

⬅️ Previous | [🏠 Roadmap](00_README.md) | [➡️ Next: Scope & Closures](02_scope_closures.md)
