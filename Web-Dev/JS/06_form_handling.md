<div align="center">

# <span style="color:#9B59B6">🟪 Level 6: Form Handling & Validation</span>

![Level](https://img.shields.io/badge/Level-6-9B59B6?style=flat-square) ![Theme](https://img.shields.io/badge/Theme-Forms%20%26%20Validation-9B59B6?style=flat-square)

</div>

---

## 📝 Form Handling & Form Events

Two related ideas:

| Concept | What It Covers |
|---------|------------------|
| **Form Handling** | Reading/collecting values a user enters |
| **Form Events** | Reacting to what the user does inside the form |

---

## 🚀 The `submit` Event

```javascript
form.addEventListener("submit", (e) => {
    e.preventDefault(); // stop the default browser page reload/navigation
});
```

> 💡 `preventDefault()` here stops the browser's default behavior of reloading the page on form submission — letting your JS handle it instead.

### Reading Field Values

```javascript
const password = document.querySelector("#password").value;
const email = document.querySelector("#email").value;

console.log({ name, password, email }); // shorthand object property syntax
```

---

## ⌨️ Other Form Events

| Event | Fires When |
|-------|-------------|
| `input` | **Every keystroke** — fires on every change to the value |
| `change` | Value changes **and** the field loses focus |
| `focus` | Element gains focus |
| `blur` | Element loses focus |

---

## ✅ Frontend vs Backend Validation

| Type | Where It Happens | Purpose |
|------|-------------------|---------|
| **Frontend validation** | In the browser (JS) | Collect form data and check it **before** sending to backend |
| HTML built-in | `<input required>` | Quick, declarative checks |
| **Backend validation** | On the server | Final, authoritative check (never trust the frontend alone) |

---

## 🧪 Custom Validation Function

```javascript
function validUsername(username) {
    if (username.value.trim().length === 0) {
        errorMessage.textContent = "Enter your name";
        return false;
    }
    return true;
}

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const isUsernameValid = validUsername(username);

    if (isUsernameValid) {
        console.log("Form is valid");
        // → send data to backend
    } else {
        console.log("Form invalid");
        // → show error
    }
});
```

> ⚠️ **Gotcha:** Always call `.trim()` before checking `.length` — otherwise whitespace-only input (`"   "`) would pass an empty check.

### Reusable Error Helpers

```javascript
function showError(input, errorMessage) {
    input.parentElement.querySelector(".error-message").textContent = errorMessage;
}

function clearError(input) {
    input.parentElement.querySelector(".error-message").textContent = "";
}
```

### Full Validation with Multiple Checks

```javascript
function validUsername(username) {
    if (username.value.trim().length === 0) {
        showError(username, "Please Enter you name");
        return false;
    }

    if (username.value.trim().length < 3) {
        showError(username, "username must be at least 3 character");
        return false;
    }

    clearError(username);
    return true;
}

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const isUsernameValid = validUsername(username);

    if (isUsernameValid) {
        console.log("Form is valid");
    } else {
        console.log("Form invalid");
    }
});
```

> 💡 Pattern: each validation function **returns `true`/`false`**, calls `showError()` on failure, and calls `clearError()` once the field becomes valid — keeping the submit handler clean.

---

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `submit` event | Fires when a form is submitted |
| `preventDefault()` | Stops default page reload/navigation |
| `input` event | Fires on every keystroke |
| `change` event | Fires on value change + blur |
| `focus` / `blur` | Element gains/loses focus |
| Frontend validation | Client-side check before sending data |
| `required` attribute | Built-in HTML-level validation |
| `showError()` / `clearError()` | Reusable helpers to display/remove field errors |
| Validation function pattern | Returns `true`/`false`, drives what `submit` handler does next |

---

## ⏭️ Coming Next

> *The following topics were referenced but not covered in this source material — not yet documented:*
> - <span style="color:gray">Async JS — Event Loop, `setTimeout`, `setInterval`</span>
> - <span style="color:gray">Full DOM manipulation (creating/modifying elements) beyond event handling</span>

---

[⬅️ Previous: DOM Events](05_dom_events.md) | [🏠 Roadmap](00_README.md) | ➡️ Next
