# 🔮 MPL (Magick Programming Language)

![Version](https://img.shields.io/badge/version-0.9.6--beta-purple) ![Engine](https://img.shields.io/badge/engine-Python_3.8+-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Focus](https://img.shields.io/badge/focus-Technomancy-red)

> **"Any sufficiently advanced technology is indistinguishable from magic."** — Arthur C. Clarke
>
> **"Code is the modern spellbook."** — MPL Manifesto

---

## 📋 Overview

**MPL (Magick Programming Language)** is an interpreted, domain-specific language (DSL) designed to bridge the gap between **Esoteric Intent** (Ritual) and **Executable Logic** (Code).

While traditional programming languages process data for calculation, MPL processes **Symbols and Archetypes** to simulate or manifest operations. It creates a syntax where:
* **Loops** become **Tesla Resonance Cycles (3-6-9)**.
* **Variables** become **Bindings**.
* **Functions** become **Invocations**.
* **Outputs** become **Manifestations** (e.g., Generating Financial Algorithms).

Currently, the engine runs on a **Python Host** (`src/main.py`), acting as a translator between the Magickal Script (`.ms`) and the machine.

---

## ⚡ Key Features

* **📐 The Tesla Protocol:** Flow control is not linear; it is harmonic. Loops are restricted to resonant frequencies (3, 6, 9) to optimize logic execution.
* **🕯️ Solomonic Ontology:** A built-in JSON database (`data/72_solomon.json`) allows the user to `invoke` historical archetypes (e.g., Vassago, Bael) and use their specific attributes in code.
* **📈 Financial Technomancy:** The engine can transmute esoteric intent into **Pine Script (TradingView)** code. (See *Proof of Concept* below).
* **⚖️ Hybrid Engine:** Supports both "Sealed" (Static) and "Living Spirit" (Adaptive/Volatile) logic modes via the Standard Library.

---

## 🌌 The Grand Vision: Digitizing the 225 Magi

MPL is currently in **Phase 1 (Solomonic/Financial)**. However, the core architecture is designed to support a vast array of "Technomantic" applications by digitizing the logic of **225 historical archetypes** listed in the Manifesto.

We are building a **Transpiler Engine** where different modules target different outputs:

| Archetype | Domain | Target Output | Status |
| :--- | :--- | :--- | :--- |
| **King Solomon (Vassago)** | Prediction & Strategy | Pine Script (TradingView) | ✅ **Active** |
| **John Dee (Enochian)** | Cryptography & Security | Python / Rust (Encryption) | 🚧 *Concept* |
| **Paracelsus (Alchemy)** | Data Transformation (ETL) | Pandas / SQL | 📅 *Planned* |
| **Shamanic Roots** | IoT & Hardware Control | C++ / Arduino | 📅 *Planned* |
| **Chaos Magick** | Entropy & Randomness | System Testing / Fuzzing | 📅 *Planned* |

*MPL is not just a trading tool; it is a universal interface for Programmable Reality.*

---

## 📦 Installation

### Prerequisites
* **Python 3.8** or higher.

### Setup

```bash
# 1. Clone the Grimoire
git clone [https://github.com/hakanovski/MPL.git](https://github.com/hakanovski/MPL.git)

# 2. Enter the Sanctum
cd MPL

# 3. Create a Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 4. Install the System (The Binding)
pip install -e .

🚀 Usage
To cast a spell (run a script), simply use the mpl command followed by your ritual file:
mpl run examples/hybrid_oracle.ms

Example Console Output:
🌙 MPL - Magick Programming Language v0.9.6
📚 Magi Loaded.
⚡ Beginning Ritual Execution...
👁️‍🗨️ [ECHO]: --- ⚖️ INITIATING HYBRID PROTOCOL ⚖️ ---
⚡ [TESLA PROTOCOL] Resonant Frequency 3 detected. Optimizing ritual...
📈 [MARKET] Vassago is forging the Hybrid Strategy...
✨ Ritual Concluded Successfully.

📜 Syntax & The Grimoire (Examples)
MPL uses a declarative, command-based syntax. Below are the core constructs.
1. Binding (Variables)
Assigns a value or energy to a symbol.
# Bind a number (Mana)
bind mana_pool to 33

# Bind a String (Sigil)
bind intent to "Protection"

2. The Tesla Cycle (Loops)
Replaces for/while loops with harmonic resonance.
# Loops exactly 3 times (Creation Frequency)
cycle(3) {
    bind mana_pool to mana_pool * 2
    tesla.oscillate(1) # Frequency pause
}

3. Invocation (Functions & Ontology)
Summons a module or an entity to perform a task.
# Invoke the Hermetic module to transmute types
bind result to hermetic.transmute(mana_pool, "Sigil")

# Invoke a Solomonic Entity (Vassago) for Divination
invoke.vassago(title="Oracle_V1", fast=50, slow=197, rsi=45)

🏆 Proof of Concept: Financial Technomancy
MPL is not just theoretical; it creates real-world value.
The engine successfully generated a Hybrid Pine Script Indicator for TradingView, optimizing parameters using the Tesla 3-6-9 Protocol and Solomonic Divination.
 * Input Ritual: examples/hybrid_oracle.ms
 * Output Manifestation: Vassago & Tesla Ex-Machina 197-45-21
 * Status: Live on TradingView.
⚙️ System Architecture
The MRE (Magic Runtime Engine) follows a 4-stage pipeline:
 * Lexer (src/lexer.py): Tokenizes source code into Sealed Verbs (BIND, INVOKE, CYCLE).
 * Parser (src/parser.py): Constructs the AST (Abstract Syntax Tree) and validates ritual structure.
 * Resolver (src/resolver.py): Connects the AST to the data/ ontology (JSON Database).
 * Interpreter (src/interpreter.py): Executes logic and calls the src/stdlib.py (Standard Library).
🗺️ Roadmap
 * v0.5.0: Standard Library & Tesla Protocol ✅
 * v0.9.5: Financial Oracle & Hybrid Logic ✅
 * v1.0.0: CLI Tool (mpl run) & PyPI Package ✅
 * v2.0.0: The Transmutation (Expansion Packs & Rust Rewrite) 📅
See ROADMAP.md for details.
🤝 Contributing
The Grimoire is open to fellow Technomancers.
 * Fork the repo.
 * Create your branch (git checkout -b feature/new-spell).
 * Commit your changes.
 * Open a Pull Request.
License: MIT
Copyright © 2025 Hakan Yorganci

---


```markdown
# 🔮 MPL (Magick Programming Language) Roadmap

This document outlines the development trajectory, future milestones, and overarching vision of the **Magick Programming Language (MPL)**. The project aims to synthesize esoteric ritual logic (Hermetic, Qabbalistic, Shamanic) with modern computer science principles (Interpreter, AST, Bytecode).

> **Motto:** "Code is the modern spellbook."

---

## 🗺️ Overview

| Version | Code Name | Status | Primary Focus |
| :--- | :--- | :--- | :--- |
| **v0.5.0** | *The Ritual* | ✅ Completed | Standard Library (StdLib) and Tesla Protocol |
| **v0.9.0** | *The Grimoire* | ✅ Completed | JSON Integration, Shell, and Daemonic Resolvers |
| **v0.9.5** | *The Oracle* | ✅ Completed | **Financial Technomancy**, Pine Script Generation, Hybrid Logic |
| **v1.0.0** | *The Manifestation* | ✅ Ready | Packaging (PyPI), CLI Polish, and Documentation |
| **v2.0.0** | *The Transmutation* | 📅 Future Goal | **Multi-Target Transpilation** (Rust, C++, IoT), Expansion Packs |

---