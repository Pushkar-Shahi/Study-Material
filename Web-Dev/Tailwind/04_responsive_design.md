<div align="center">

# <span style="color:#E07B00">🟠 Section 4 — Responsive Design</span>

![Section](https://img.shields.io/badge/Section-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Mobile_First-E07B00)

</div>

---

## 📱 Mobile-First Philosophy

Tailwind styles for the **smallest screens by default**, then uses breakpoint prefixes to apply different styles as the screen gets larger.

---

## 📏 Core Breakpoints

| Breakpoint | Minimum Width | CSS Media Query |
|:---:|:---:|---|
| `sm` | 640px (40rem) | `@media (width >= 40rem)` |
| `md` | 768px (48rem) | `@media (width >= 48rem)` |
| `lg` | 1024px (64rem) | `@media (width >= 64rem)` |
| `xl` | 1280px (80rem) | `@media (width >= 80rem)` |
| `2xl` | 1536px (96rem) | `@media (width >= 96rem)` |

> [!NOTE]
> A style prefixed with `md:` only triggers once the screen reaches **768px or wider**.

---

## 🛠️ How to Use Them

Prefix **any** utility class to make it responsive.

### 🔠 Typography
```html
<p class="text-sm md:text-lg">
    Small on mobile, large on tablets and up
</p>
```

### 📐 Layout
```html
<div class="hidden lg:block">
    Hidden on mobile, shown on desktop
</div>
```

### 📏 Spacing
```html
<div class="p-4 md:p-8">
    More padding as the screen grows
</div>
```

---

## 🌊 Minimum-Width Cascading

Since breakpoints are based on **minimum width**, a style applied at `md:` will **also apply** at `lg:` and `xl:` — unless you explicitly override it at those larger breakpoints.

```html
<div class="text-sm md:text-lg lg:text-xl">
    <!-- sm screens: text-sm -->
    <!-- md and up: text-lg -->
    <!-- lg and up: text-xl (overrides md:) -->
</div>
```

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Mobile-first | Base styles target the smallest screens |
| `sm:` `md:` `lg:` `xl:` `2xl:` | Breakpoint prefixes for responsive utilities |
| Prefixing any class | Makes typography, layout, and spacing responsive |
| Min-width cascading | Styles apply upward unless overridden at a larger breakpoint |

---

### 🛠️ MLOps Perspective: Multi-Device Observability
> [!NOTE]
> In production ML, an alert can trigger at 2 AM on a Sunday. 
> - You'll be checking model latency or a sudden spike in data drift on your smartphone.
> - By using simple prefixes (`<div class="hidden md:block">`), you ensure that complex, wide DataFrames are hidden on mobile, and simpler metric summaries are shown instead.
> - This guarantees your ML tools are usable across all devices without writing separate mobile stylesheets.

---

<div align="center">

⬅️ [Previous: Section 3 — Styling Basics](./03_styling_basics.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full Tailwind CSS Roadmap!

</div>
