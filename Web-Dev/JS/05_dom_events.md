<div align="center">

# <span style="color:#E74C3C">🟥 Level 5: DOM Events</span>

![Level](https://img.shields.io/badge/Level-5-E74C3C?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Interactivity-E74C3C?style=flat-square)

</div>

---

## ⚡ What Is an Event?

An **event** is an **action** (like a click) that **triggers** something to happen.

```
action (e.g. click) → event → triggers a response
```

---

## 👂 Listening for Events

```javascript
btn.addEventListener(eventType, callback);
```

| Common Event Types |
|----------------------|
| `click` |
| `mouseover` |
| `mousedown` |

```javascript
let btn = document.querySelector("#reveal-gift");
let h1 = document.querySelector("#gift");

function revealGift() {
    h1.classList.toggle("hidden");
}

btn.addEventListener("click", revealGift); // pass the function REFERENCE, not a call
```

> ⚠️ **Gotcha:** Pass `revealGift`, **not** `revealGift()` — the latter calls it immediately instead of registering it as a callback.

---

## 🎯 The Event Object

The callback automatically receives an **event object** with useful properties:

```javascript
console.log(event.target);        // the exact element the event happened ON
console.log(event.currentTarget); // the element the LISTENER is attached to
```

| Property | Meaning |
|----------|---------|
| `event.target` | The specific element that was actually clicked |
| `event.currentTarget` | The element the `addEventListener` was applied to |

Also available: `removeEventListener(...)` to detach a listener when no longer needed.

---

## 🫧 Bubbling vs Capturing

How events travel through the DOM:

```
document → ... → outer → target → inner (bubbling phase back up)
```

| Phase | Direction |
|-------|-----------|
| **Capturing** | Top (document) → down to the target |
| **Bubbling** | Target → back up to the top (document) — this is the *default* |

```javascript
outer.addEventListener("click", (e) => {
    console.log("Outer");
}, { capture: true }); // listens during the CAPTURING phase
```

> 💡 By default, listeners fire during the **bubbling** phase. Passing `{ capture: true }` makes the listener fire during the **capturing** phase instead.

---

## ✋ Controlling Event Flow

| Method | Effect |
|--------|--------|
| `e.stopPropagation()` | Stops the event from **bubbling** further up the DOM |
| `e.preventDefault()` | Stops the browser's **default behavior** (e.g., link navigation, form submit) |

```javascript
btn2.addEventListener("click", (e) => {
    e.stopPropagation();
    console.log("Btn2");
});
```

---

## 🎪 Event Delegation

Instead of attaching a listener to **every** child element (inefficient for large lists — e.g., 1000 items), attach **one** listener to the **parent** and use `e.target` to figure out what was actually clicked.

```javascript
productList.addEventListener("click", (e) => {
    e.stopPropagation();
    console.log(e.target.parentElement);
    console.log(e.target.tagName);
    console.log(e.target.textContent);

    if (e.target.textContent === "Remove product") {
        e.target.parentElement.remove();
    }
});
```

| Property | Purpose |
|----------|---------|
| `e.target` | The exact element clicked inside the list |
| `e.target.parentElement` | The direct parent of whatever was clicked |
| `e.target.closest(selector)` | Finds the **nearest ancestor** matching a CSS selector |

> 💡 **Why it matters:** With 1,000 product cards, attaching 1,000 individual `addEventListener` calls is wasteful. **One** listener on the parent (`productList`) + `e.target` checks handles all of them.

---

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `addEventListener(type, callback)` | Registers a response to a user action |
| Event object (`e`) | Carries info about the event |
| `e.target` | Element that triggered the event |
| `e.currentTarget` | Element the listener is attached to |
| Bubbling | Event travels from target **up** to document (default) |
| Capturing | Event travels from document **down** to target (`capture: true`) |
| `stopPropagation()` | Stops bubbling/capturing from continuing |
| `preventDefault()` | Cancels default browser behavior |
| Event delegation | One parent listener handles all children via `e.target` |

---

[⬅️ Previous: `this` & Coercion](04_this_coercion.md) | [🏠 Roadmap](00_README.md) | [➡️ Next: Form Handling](06_form_handling.md)
