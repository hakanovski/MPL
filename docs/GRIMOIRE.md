# 📜 The Grand Grimoire: MPL Technical Documentation

> **Version:** v0.9.6 (The Robust Oracle)
> **Engine:** Python 3.8+
> **License:** MIT

---

## 👁️ Overview

This Grimoire serves as the official reference manual for the **Magick Programming Language (MPL)**. It details the syntax, the esoteric logic of the interpreter, and the full API of the Standard Library (The Grimoire).

MPL is a **Domain-Specific Language (DSL)** designed to transmute intent-based commands into executable Python logic, with a specific focus on **Financial Technomancy** and **System Rituals**.

---

## ⚡ Core Syntax (The Sealed Verbs)

MPL does not use standard programming keywords. Instead, it uses **Ritual Verbs** to manipulate the environment.

### 1. BIND (Variable Assignment)
Allocates memory and assigns value (Mana) to a symbol.
* **Syntax:** `bind <variable_name> to <value>`
* **Types:** Integer, Float, String.

```mpl
bind mana_pool to 100
bind intent to "Wealth"
bind ratio to 1.618

2. CYCLE (The Tesla Protocol)
Executes a block of code repeatedly. Unlike standard loops, MPL optimizes execution based on Resonant Frequencies (3, 6, 9).
 * Syntax: cycle(<frequency>) { ... }
<!-- end list -->
# Loops 3 times (Creation Frequency)
cycle(3) {
    bind mana_pool to mana_pool + 10
    echo "Gathering energy..."
}

3. INVOKE (Function Call)
Summons an entity or module from the Standard Library to perform a task.
 * Syntax: invoke.<entity>(param1=value, param2=value)
 * Fallback: If an entity is not found in the JSON Ontology, the interpreter searches the Standard Library directly.
<!-- end list -->
# Invoking the Financial Oracle
invoke.vassago(title="Bitcoin_Strategy", rsi=45)

4. ECHO (System Output)
Projects a message to the console (The Void).
 * Syntax: echo <message>
<!-- end list -->
echo "The ritual has begun."

📚 Standard Library (API Reference)
The Standard Library (src/stdlib.py) contains the core modules that power MPL. These modules are accessible via the invoke command.
📈 1. Market Module (Financial Technomancy)
Domain: TradingView, Pine Script, Financial Analysis.
Aliases: market, oracle, vassago.
divine(title, fast, slow, rsi, adx, offset)
Generates a valid Pine Script v6 strategy code based on Hybrid Logic (Sealed vs. Living Spirit).
| Parameter | Type | Default | Description |
|---|---|---|---|
| title | str | "Oracle" | The name of the indicator/strategy. |
| fast | int | 50 | Length of the Support SMA. |
| slow | int | 200 | Length of the Trend Line (Tesla Tuned). |
| rsi | int | 45 | RSI Threshold for Sniper Entries. |
| offset | int | 21 | Fibonacci Offset for Future Projection. |
Example:
invoke.vassago(title="Ex-Machina", slow=197, rsi=45)

⚡ 2. Tesla Module (Energy & Math)
Domain: Frequency, Vibration, Amplification.
Aliases: tesla.
amplify(signal, factor)
Multiplies a numeric value by a specified factor.
| Parameter | Type | Description |
|---|---|---|
| signal | int/float | The base value to amplify. |
| factor | int/float | The multiplier. |
Example:
bind energy to tesla.amplify(100, 3)

👑 3. Solomonic Module (System Control)
Domain: OS Processes, Root Access, Stealth.
Aliases: solomonic, process, system.
hide(pid)
Simulates hiding a process ID from the system monitor.
 * Returns: True (Visual simulation only).
root_access()
Grants simulated administrative privileges for the ritual context.
Example:
invoke.solomonic(func="hide", pid=101)

⚗️ 4. Hermetic Module (Alchemy)
Domain: Type Conversion, Transmutation.
Aliases: hermetic.
transmute(target, target_type)
Converts a value from one data type to another.
| Parameter | Type | Description |
|---|---|---|
| target | any | The variable to convert. |
| target_type | str | The desired type ("Mana" for int, "Sigil" for str). |
Example:
bind result to hermetic.transmute("108", "Mana")

💥 Error Codes (The Backfire)
When a ritual fails, the Interpreter raises specific error flags.
| Code | Meaning | Cause |
|---|---|---|
| [BACKFIRE] | Critical Failure | Python exception in the Standard Library (e.g., Division by zero). |
| [FIZZLE] | Soft Failure | The invoked module exists, but the function name is unknown. |
| [INVOKE] | Summoning Failed | The entity/module name could not be found in the Grimoire or Registry. |
| [VOID] | Null Pointer | Attempting to use a variable that has not been bound. |
> "The code provides the structure; the user provides the power."
> — Hakan Yorganci, Technomancer
> 

---
