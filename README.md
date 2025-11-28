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

---

## 📜 The Grimoire (Sample Rituals)

To understand the syntax of MPL, observe these sample incantations. You can find the full source files in the `examples/` directory.

### 1. The Awakening (Hello World)
**File:** [`examples/01_hello_world.ms`](examples/01_hello_world.ms)
Basic input/output binding.
```mpl
bind message to "Hello, Cosmos."
divination.inscribe(message)

2. The Cycle (Tesla Protocol)
File: examples/03_protection_ward.ms
Using the 3-6-9 resonance keys for flow control instead of linear loops.
# A creation cycle (Key 3)
cycle(3) {
    bind energy to energy + 33
    tesla.oscillate(1)
}

3. The Invocation (Ontology)
File: examples/04_invoke_hermes.ms
Summoning historical entities from the data/magi_225.json database.
invoke.hermes(intent="swift_communication")

if hermes.element == "Air" {
    cast transmit_message
}

---


1. The Awakening (Hello World)
Dosya: examples/01_hello_world.ms
Seviye: Başlangıç
Amaç: Ekrana yazı yazdırmak ve bir değişken tanımlamak.
# 01_hello_world.ms
# The First Breath: Declaring intent and manifesting it via the console.

# Bind the intent string (Sigil) to a vessel named 'message'
bind message to "Hello, Cosmos. The connection is established."

# Use the Divination module to output the result (Standard Output)
divination.inscribe(message)

2. The Transmutation (Variables & Math)
Dosya: examples/02_energy_flow.ms
Seviye: Kolay
Amaç: Matematiksel işlem yapmak, Tesla modülünü kullanmak ve tip dönüşümü (Transmutation).
# 02_energy_flow.ms
# A simple ritual to amplify Mana using Tesla mathematics.

# Initialize base energy (Mana)
bind base_energy to 100

# Use the Tesla module to amplify the energy by the sacred factor of 3
bind amplified_energy to tesla.amplify(base_energy, 3)

# Transmute the integer (Mana) into a string (Sigil) for display
transmute amplified_energy -> Sigil

# Log the result
divination.inscribe("Energy Manifestation Level: " + amplified_energy)

3. The Cycle (Loops & Resonance)
Dosya: examples/03_protection_ward.ms
Seviye: Orta
Amaç: cycle döngüsünü kullanmak. Standart for döngüsü yerine Tesla 3-6-9 mantığını göstermek.
# 03_protection_ward.ms
# A ritual to build a 3-layered protection circle.

bind ward_strength to 0
bind layer_name to "Aether"

# The Creation Cycle (Key 3)
# Loops exactly 3 times to initialize the structure
cycle(3) {
    # Increase the strength of the ward
    bind ward_strength to ward_strength + 33
    
    # Cast a visual confirmation
    divination.inscribe("Layer sealed. Current strength: " + ward_strength)
    
    # Pause for 1Hz (1 second) to let the energy settle
    tesla.oscillate(1)
}

divination.inscribe("Ritual Complete. Ward is active.")

4. The Invocation (Ontology & Objects)
Dosya: examples/04_invoke_hermes.ms
Seviye: İleri
Amaç: data/magi_225.json veritabanından bir varlık (Hermes) çağırmak ve onun özelliklerini (hermes.element) mantıksal karar (if) için kullanmak.
# 04_invoke_hermes.ms
# Invoking a historical intelligence to optimize communication.

# 1. Summon the entity from the Ontology Database
# This loads 'speed', 'element', and 'planet' into the local scope
invoke.hermes(intent="swift_communication")

# 2. Check the Elemental Alignment
# 'hermes.element' comes directly from the JSON data
if hermes.element == "Air" {
    
    divination.inscribe("Element Air detected. Channel is clear.")
    
    # Execute the specific spell for this entity
    cast transmit_message with {
        target = "Network_Node_1",
        speed = hermes.attribute_speed
    }

} else {
    # If the alignment is wrong, abort to prevent backfire
    divination.inscribe("Elemental mismatch. Banishing...")
    cast banish
}

5. The Grand Ritual (System & Daemons)
File: examples/05_server_daemon.ms
Level: Expert (Technomancy)
Purpose: To launch a background process (Daemon), monitor it, and terminate it when necessary. Uses the solomonic library.

# 05_server_daemon.ms
# A Technomancy ritual to manage a background web server (Daemon).

# Import the Solomonic library for process control
import solomonic

## 📝 More Syntax Examples:

# 1. Summon the Daemon (Start a local Python server)
bind server_pid to solomonic.summon("python -m http.server 8000")
divination.inscribe("Server Spirit summoned with PID: " + server_pid)

# 2. The Maintenance Cycle (Key 6)
# Monitor the process for stability
cycle(6) {
    
    bind status to solomonic.check_vitality(server_pid)
    
    if status == "Unstable" {
        divination.inscribe("Spirit is restless. Stabilizing...")
        solomonic.bind(server_pid, resource_limit="512MB")
    }
    
    tesla.oscillate(1)
}

# 3. The Release Cycle (Key 9)
# Properly close the connection and banish the process
divination.inscribe("Ritual concluded. Banishing spirit.")
solomonic.banish(server_pid)

---

🤝 Contributing
MPL is currently in Alpha Prototype stage. We welcome developers to help build the core interpreter.
 * Fork the repo.
 * Create your feature branch (git checkout -b feature/new-parser).
 * Commit your changes.
 * Push to the branch.
 * Open a Pull Request.

Copyright © 2025 MPL Project. Released under the MIT License. 🧙🏻‍♂️ Hakan Yorganci

