> **Current Version:** 0.1.0-alpha
> **Engine Core:** Python 3.8+
> **File Extension:** `*.ms` (MagickScript)
> **License:** MIT

---

## 📋 Overview

**MPL (Magick Programming Language)** is an interpreted, domain-specific language (DSL) designed to structure abstract esoteric intent into executable logic.

While traditional programming languages manipulate data to perform calculations, MPL manipulates **Symbols and Syntax** to simulate ritual operations. It treats "Magick" as a rigorous set of logical steps: defining dependencies (Invoke), assigning pointers (Bind), configuring parameters (Shape), and executing threads (Release).

This repository contains the prototype interpreter and the core Standard Library definitions.

> **Note:** For the philosophical vision, the list of 225 historical lineages, and the "Tesla Protocol" inspiration, please refer to [**MANIFESTO.md**](./MANIFESTO.md).

---

## ⚙️ System Architecture

MPL runs on a custom **Magic Runtime Engine (MRE)** built in Python. The architecture follows a standard compiler pipeline adapted for ritual logic:

1.  **Lexer (`src/lexer.py`):**
    * Tokenizes the input `.ms` source code.
    * Identifies unique keywords: `INVOKE`, `BIND`, `SHAPE`, `RELEASE`.
    * Parses literals: Strings, Numbers, and Frequency values (e.g., `432hz`).

2.  **Parser (`src/parser.py`):**
    * Analyzes the token stream.
    * Builds an **Abstract Syntax Tree (AST)** that represents the ritual flow.
    * Validates the "Tetragrammaton Cycle" (ensures the ritual steps are in the correct order).

3.  **Interpreter (`src/interpreter.py`):**
    * Traverses the AST.
    * Executes the logic defined in the `stdlib` (Standard Library).
    * Outputs the simulation result (Energy Delta, Probability Shift, or Console Output).

---

## 📦 Installation

### Prerequisites
* **Python 3.8** or higher.

### Setup
```bash
# 1. Clone the repository
git clone [https://github.com/your-username/mpl.git](https://github.com/your-username/mpl.git)

# 2. Navigate to the project directory
cd mpl

# 3. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

🚀 Usage
To run a MagicScript file, pass the file path to the main compiler script:
python src/main.py examples/protection_ward.ms

Example Output
[MRE] Initializing Runtime...
[INVOKE] Entity <Archangel.MICHAEL> loaded into memory.
[BIND] Connection established -> Target: LOCAL_SYSTEM.
[SHAPE] Modulating frequency to 417hz...
[RELEASE] Executing Spell...
>>> SUCCESS: Ward active. Entropy cost: 12 units.

⚡ Syntax Reference: The 4-Step Cycle
MPL enforces a strict object-oriented ritual structure known as the Invoke-Bind-Shape-Release cycle.
1. INVOKE (Initialization)
Imports an archetype, spirit, or energy source from the Standard Library.
// Syntax: var name = invoke(Library.Entity);
var guardian = invoke(Goetia.Duke.BUNE);

2. BIND (Assignment)
Connects the invoked entity to a specific target (Object, Person, Place, or Self).
// Syntax: bind(variable).to(Target);
bind(guardian).to(Target.SELF);

3. SHAPE (Configuration)
Defines the parameters of the operation using method chaining.
// Syntax: shape(variable).param(value)...;
shape(guardian)
    .frequency(110hz)       // Set vibrational rate
    .material("Copper")     // Material correspondence
    .duration("Moon_Cycle"); // Temporal duration

4. RELEASE (Execution)
Compiles the intent and executes the function.
// Syntax: release(variable);
release(guardian);

📂 Project Structure
mpl/
│
├── src/
│   ├── __init__.py
│   ├── lexer.py         # Tokenizer logic
│   ├── parser.py        # AST construction
│   ├── interpreter.py   # Runtime execution
│   └── main.py          # CLI Entry point
│
├── stdlib/
│   ├── core.ms          # Base functions
│   ├── goetia.ms        # Solomonic definitions
│   └── runes.ms         # Elder Futhark definitions
│
├── examples/
│   ├── hello_world.ms
│   └── protection_circle.ms
│
├── docs/
│   └── grammar.md       # EBNF Grammar specification
│
├── MANIFESTO.md         # Philosophy, History & The 225 List
└── README.md            # This technical documentation

🤝 Contributing
MPL is currently in Alpha Prototype stage. We welcome developers to help build the core interpreter.
 * Fork the repo.
 * Create your feature branch (git checkout -b feature/new-parser).
 * Commit your changes.
 * Push to the branch.
 * Open a Pull Request.
Copyright © 2025 MPL Project. Released under the MIT License.

