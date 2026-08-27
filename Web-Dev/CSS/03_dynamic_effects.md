<div align="center">

# <span style="color:#D4A017">🟡 Section 3 — Dynamic Effects</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Motion_%26_Manipulation-D4A017)

</div>

---

## ⏳ 1. Transitions

Let property changes happen **smoothly over time** instead of instantly.

| Property | Purpose |
|---|---|
| `transition-duration` | Exact length of time the effect takes |
| `transition-property` | Which CSS properties get animated |
| `transition-timing-function` | Speed curve (e.g., `ease-in`, `ease-out`) |
| `transition-delay` | How long to wait before the effect begins |

```css
.button {
    transition-property: background-color;
    transition-duration: 0.3s;
    transition-timing-function: ease-in;
    transition-delay: 0.1s;
}
```

---

## 🔄 2. Transforms

Visually modify an element **without affecting the surrounding layout**.

| Function | Effect |
|---|---|
| `translate()` | Moves an element horizontally/vertically |
| `scale()` | Resizes an element on a 2D plane |
| `rotate()` | Turns an element around a fixed point |

```css
.card:hover {
    transform: scale(1.1) rotate(5deg);
}
```

---

## 🎬 3. Animations

More advanced than transitions — rely on a **storyboard** called `@keyframes` to define styles at specific checkpoints.

```css
@keyframes bounce {
    0%   { transform: translateY(0); }
    50%  { transform: translateY(-20px); }
    100% { transform: translateY(0); }
}

.ball {
    animation-name: bounce;
    animation-duration: 1s;
    animation-iteration-count: infinite;
}
```

| Property | Purpose |
|---|---|
| `animation-iteration-count` | How many times it plays (or `infinite`) |
| `animation-direction` | Forward, backward, or alternating |
| `animation-fill-mode` | Styles applied before start / after end |

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Transitions | Smooth, simple property changes over time |
| Transforms | Move, resize, or rotate without disrupting layout |
| `@keyframes` | Define multi-step animation storyboards |
| `animation-*` properties | Fine-tune how an animation plays |

---

### 🛠️ MLOps Perspective: UX & Loading States
> [!NOTE]
> Why does an ML Engineer care about animations? **Latency.**
> - Large ML models (especially Generative AI or heavy deep learning models) take time to run inference (sometimes several seconds).
> - If you don't provide visual feedback (like a spinning loading icon using CSS animations), users will assume the app is broken and leave.
> - A simple `@keyframes` animation for a loading spinner is one of the most important CSS tricks you can learn for ML web apps.

---

<div align="center">

⬅️ [Previous: Section 2 — Layout](./02_layout.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Section 4 — Responsiveness](./04_responsiveness.md)

</div>
