# 🐠 **The Babel Fish Base Converter**
*Because numbers should speak every language in the galaxy!* 🌠  

---

## 💫 What Is This?

Ever wished you could whisper sweet binary nothings to a hexadecimal alien?  
Or maybe you want to turn your base-7 gibberish into base-19 poetry?  
Well, you’re in luck — this script is your **universal translator**! 🌎➡️🌍➡️🌌  

It converts numbers from *any base (2–36)* to *any other base*, using pure, **hand-forged** math —  
no `bin()`, no `hex()`, no `oct()`, no `int(x, base)`, and definitely no `format()` black magic. 🪄🚫  

---

## ⚙️ How It Works

This code runs in **two epic stages**:

### 🧩 Part 1 — `to_decimal(number_string, original_base)`
Transforms any number (like `"C7"` in base 16) into its decimal form.  
It does this by:  
1. Taking your number apart digit-by-digit 🔍  
2. Multiplying each piece by its base power 💥  
3. Summing everything into a single glorious decimal integer 🌞  

**Example:**  
`"C7"` in base 16 → (12 × 16¹) + (7 × 16⁰) = **199**

---

### 🔁 Part 2 — `from_decimal(decimal_number, target_base)`
Now that we’ve got a decimal number, it’s time for **The Great Escape**! 🏃‍♂️💨  
This function repeatedly divides your number by the target base, collecting the remainders —  
which become your *new digits* in reverse order.  

**Example:**  
`199` in base 10 → base 16 = **"C7"**

---

### 🧠 The Grand Translator: `main()`
Your interactive portal! 🌀  
It:
1. Greets the user (that’s you, space traveler 👩‍🚀)
2. Asks for:
   - The number to convert
   - Its original base
   - The target base
3. Prints your result like a proud math bard 🎤

---

## 💻 Example Run


✨ It’s alive! ✨  

---

## 🚀 Features

- 🧮 Converts between bases **2 through 36**
- 🔢 Handles both **numbers and letters (A–Z)**
- ⚔️ Uses **zero forbidden Python functions**
- 💬 Fully interactive, fun CLI
- 👀 Code so clean, your computer will wink at you

---

## 🧱 Requirements

- Python 3+
- A functioning brain 🧠  
- Coffee (optional, but highly recommended ☕)

---

## 🧭 Decision Tree

```text
                🌌 START 🌌
                     │
                     ▼
        ┌────────────────────────┐
        │ User enters:            │
        │ number_string, bases    │
        └────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  to_decimal()           │
        │  Convert from base N →  │
        │  base 10 (decimal)      │
        └────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  from_decimal()         │
        │  Convert from decimal → │
        │  target base            │
        └────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │ Print final translated  │
        │ number with style ✨     │
        └────────────────────────┘
                     │
                     ▼
                🐠 END 🐠
