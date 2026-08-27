<div align="center">

# <span style="color:#C0392B">🔴 Step 5 — User Interaction (Forms)</span>

![Step](https://img.shields.io/badge/Step-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Collecting_Data-C0392B)

</div>

---

## 📦 The Container — `<form>`

Everything a user fills out is wrapped in the `<form>` tag.

```html
<form action="/submit-data">
  <!-- inputs go here -->
</form>
```

| Attribute | Purpose |
|---|---|
| `action` | Where the browser sends the data (usually a backend endpoint) |

---

## 🎛️ Versatile Inputs — `<input>`

The `type` attribute transforms `<input>` into different kinds of fields.

| `type` value | Renders As |
|---|---|
| `text` | Standard text box |
| `email` | Email field (with format validation) |
| `password` | Hidden password field |
| `radio` | Multiple-choice option |
| `file` | File upload button |
| `submit` | Submit button |

```html
<input type="text" name="username">
<input type="email" name="email">
<input type="password" name="password">
<input type="radio" name="gender" value="male"> Male
```

---

## 🏷️ Labels & Placeholders

| Element/Attribute | Purpose |
|---|---|
| `<label for="...">` | Links descriptive text to an input for accessibility |
| `placeholder="..."` | Short hint shown inside the input box |

```html
<label for="email">Email:</label>
<input type="email" id="email" placeholder="you@example.com">
```

---

## 🎚️ Advanced Controls

| Tag | Purpose |
|:---:|---|
| `<textarea>` | Multi-line text input (e.g., a bio) |
| `<select>` + `<option>` | Dropdown menu |
| `<fieldset>` | Visually groups related fields together |

```html
<textarea rows="4" cols="30"></textarea>

<select name="country">
  <option value="in">India</option>
  <option value="us">USA</option>
</select>

<fieldset>
  <legend>Contact Info</legend>
  <!-- grouped inputs -->
</fieldset>
```

---

## 📤 Submission

Data is sent to the server when the user clicks:
- A `<button>`, **or**
- An `<input type="submit">`

```html
<button type="submit">Send</button>
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `<form action="...">` | Container that defines where data is sent |
| `<input type="...">` | Flexible field for different data types |
| `<label for="...">` | Accessible text tied to an input |
| `<textarea>` / `<select>` | Multi-line text / dropdown selection |
| `<fieldset>` | Groups related form fields |
| `<button>` / `type="submit"` | Triggers form submission |

---

### 🛠️ MLOps Perspective: Model Inference Triggers
> [!IMPORTANT]
> Forms are how users trigger your machine learning models!
> - The `action="/predict"` attribute is exactly how you route a user's input to your FastAPI model inference endpoint.
> - `input type="file"` is how a user uploads a CSV for batch predictions, or an image for your CNN to classify.
> - When the user clicks `<button type="submit">`, the browser sends a POST request to your ML API containing their data.

---

<div align="center">

⬅️ [Previous: Step 4 — Multimedia & Semantic Layout](./04_multimedia_semantic.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full Web Development Roadmap!

</div>
