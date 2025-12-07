# 🔮 MPL (Magick Programming Language) Roadmap

This document outlines the development trajectory, future milestones, and overarching vision of the **Magick Programming Language (MPL)**. The project aims to synthesize esoteric ritual logic (Hermetic, Qabbalistic, Shamanic) with modern computer science principles (Interpreter, AST, Bytecode).

> **Motto:** "Code is the modern spellbook."

---

## 🗺️ Overview

| Version | Code Name | Status | Primary Focus |
| :--- | :--- | :--- | :--- |
| **v0.1.0** | *The Awakening* | ✅ Completed | Manifesto, Ontology, and Core Concepts |
| **v0.2.0** | *The Structure* | ✅ Completed | Data Structures, Grammar, and Lexer |
| **v0.3.0** | *The Engine* | ✅ Completed | Parser, AST, and Core Interpreter |
| **v0.5.0** | *The Ritual* | ✅ Completed | Standard Library (StdLib) and Tesla Protocol |
| **v0.9.0** | *The Grimoire* | 🚧 In Progress | Advanced Examples, Unit Tests, CLI Polish |
| **v1.0.0** | *The Manifestation* | 📅 Goal | First Stable Release, Packaging (PyPI), and Docs |

---

## 🛠️ Detailed Milestones

### 🌱 v0.1.0 - The Awakening (Completed)
Laying the philosophical and theoretical foundations of the project.
- [x] **Manifesto:** Publication of the philosophical vision (`MANIFESTO.md`).
- [x] **Ontology:** Compilation of the 225 Historical Magi list (`MAGI.md`).
- [x] **Repo Structure:** Establishment of the basic GitHub directory hierarchy.

### 🏗️ v0.2.0 - The Structure (Completed)
Structuring the data and defining the language rules.
- [x] **Data Transformation:** Converting the `MAGI.md` text into machine-readable `data/magi_225.json` format.
- [x] **Grammar Definition:** Writing the formal grammar of the language in EBNF format (`docs/grammar.md`).
- [x] **Lexer Prototype:** Developing a basic Lexer in Python to tokenize MPL syntax (`src/lexer.py`).

### ⚙️ v0.3.0 - The Engine (Completed)
Making the code executable.
- [x] **Parser:** Module to convert tokens into Abstract Syntax Trees (AST) (`src/parser.py`).
- [x] **Interpreter Core:** Python-side implementation of core commands like `invoke`, `bind`, and `cast` (`src/interpreter.py`).
- [x] **Error Handling:** Treating errors as "Corruption" or "Backfire" events (`RuntimeException`).

### ⚡ v0.5.0 - The Ritual (Completed)
The phase where the language develops its unique character.
- [x] **Tesla Protocol:** Implementation of the 3-6-9 cyclical logic loops inside the Interpreter.
- [x] **StdLib (Standard Library):** Implemented in `src/stdlib.py`.
    - `import hermetic` (Elemental manipulation)
    - `import solomonic` (Daemon/Process management)
    - `import divination` (Data prediction and Random Seed generation)
- [x] **Sigil Generator:** An algorithm that converts intent strings into sigils (`Runic.forge_sigil`).

### 📜 v0.9.0 - The Grimoire (Current Focus)
Polishing the experience before public release.
- [ ] **Interactive Shell:** Improving the `mpl_shell.py` REPL experience.
- [ ] **Unit Tests:** Writing `tests/` to ensure the magic doesn't backfire.
- [ ] **Advanced Examples:** Creating complex ritual scripts in `examples/`.
- [ ] **Refactoring:** Connecting `72_solomon_sigil_shapes.json` fully to the Resolver.

### 🚀 v1.0.0 - The Manifestation (Goal)
Opening up to the community and ensuring usability.
- [ ] **PIP Package:** Making the language installable via `pip install mpl-ms`.
- [ ] **CLI Tool:** Enabling execution via terminal commands like `mpl run ritual.ms`.
- [ ] **Full Documentation:** Detailed documentation for all functions and historical magi.

---

## 🔮 Future Vision (Long-Term / v2.0+)

**"Technomancy" Integrations:**
This phase aims to bridge the software with the physical world.

* **IoT Integration:** Controlling smart devices (e.g., Philips Hue lights changing color upon ritual completion).
* **Hardware RNG:** Harvesting true "Entropy" from hardware noise for spell casting.
* **Audio Synthesis:** Generating audio waves based on Tesla coil frequencies (Binaural beats).
* **Financial Oracle:** Fetching data from Stock/Crypto APIs to run "Divination" algorithms.

---

## 🤝 Contributing
This roadmap is dynamic and may evolve based on community feedback ("Issues"). Please feel free to share your ideas in the `Discussions` tab.
