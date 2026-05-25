# 👻 GhostPrint

<p align="center">
  <img src="https://img.shields.io/pypi/v/ghostprint?color=blue&label=PyPI" />
  <img src="https://img.shields.io/pypi/pyversions/ghostprint" />
  <img src="https://img.shields.io/github/license/MRThugh/ghostprint" />
  <img src="https://img.shields.io/badge/style-cinematic-black" />
</p>

<p align="center">
  <b>Cinematic terminal effects for Python</b><br/>
  Glitch • Animations • Hacker UI • Gradient text • Loading effects
</p>

---

## ⚡ Overview

GhostPrint is a lightweight Python library for creating cinematic and hacker-style terminal experiences.

It focuses on making CLI output more expressive, animated, and visually engaging without external dependencies.

---

## 📦 Installation

```bash
pip install ghostprint
```

---

## 🚀 Quick Start

```python
from ghostprint import *
from ghostprint.colors import gradient

banner("GhostPrint")

typewrite("Connecting to DarkLine Network...", 0.02)

loading("Authenticating", 2)

print()

print(gradient("ACCESS GRANTED"))

print()

glitch("WELCOME BACK, ALI")

print()

box("github.com/MRThugh")
```

---

## 🎬 Example Output

```
████████████████████
███  GhostPrint  ███
████████████████████

Connecting to DarkLine Network...
Authenticating ✓

ACCESS GRANTED

WELCOME BACK, ALI

┌────────────────────┐
│ github.com/MRThugh │
└────────────────────┘
```

---

## ✨ Features

- 👾 Glitch text effects
- ⌨️ Typewriter animation
- ⏳ Loading spinners
- 🌈 Gradient text output
- 📦 Terminal boxes & banners
- 🧠 Zero dependencies
- ⚡ Lightweight & fast

---

## 📚 API

### `glitch(text)`
Creates a glitch animation effect.

```python
glitch("ACCESS GRANTED")
```

---

### `typewrite(text, speed)`
Simulates typing effect.

```python
typewrite("Hello World", 0.03)
```

---

### `loading(text, duration)`
Displays animated loading spinner.

```python
loading("Loading", 3)
```

---

### `banner(text)`
Displays a cinematic banner.

```python
banner("GhostPrint")
```

---

### `box(text)`
Draws a terminal box.

```python
box("MRThugh")
```

---

### `gradient(text)`
Applies color gradient effect.

```python
print(gradient("GhostPrint"))
```

---

## 📦 Install from Source

```bash
git clone https://github.com/MRThugh/ghostprint.git
cd ghostprint
pip install .
```

---

## 🔗 Links

- 🐍 PyPI: https://pypi.org/project/ghostprint/
- 💻 GitHub: https://github.com/MRThugh

---

## 👨‍💻 Author

**Ali Kamrani**

- GitHub: https://github.com/MRThugh  
- Email: kamrani.exe@gmail.com  

---

## 📄 License

This project is licensed under the MIT License.
