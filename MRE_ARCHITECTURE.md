# ⚙️ MRE (Magic Runtime Engine) Architecture

**Version:** 0.1.0-alpha

The **Magic Runtime Engine (MRE)** is the core execution environment of MPL. Written in Python, it serves as the bridge between the high-level intent defined in `.ms` scripts and the low-level machine operations.

Unlike a standard interpreter, the MRE includes an **Ontological Resolver** layer that injects historical and metaphysical data into the runtime context dynamically.

---

## 1. System Overview (The Pipeline)

The execution flow follows a modified interpreter pipeline, metaphorically structured as a ritual process: **Tokenization (Naming) → Parsing (Structuring) → Resolution (Summoning) → Execution (Manifestation).**

```mermaid
graph TD
    Source[Source Code .ms] -->|Raw Text| Lexer
    Lexer -->|Tokens| Parser
    Parser -->|AST| Interpreter
    
    subgraph "The Magic Runtime Engine (MRE)"
        Interpreter <-->|Query| Ontology[Ontology Resolver]
        Ontology <-->|Read| DB[(data/magi_225.json)]
        Interpreter <-->|Manage| Memory[Memory & State (The Ether)]
        Interpreter -->|Output| StdOut[System Effect / Console]
    end

2. Core Components
A. The Lexer (src/lexer.py)
 * Role: The Scribe.
 * Function: Reads the raw .ms file and breaks it down into discrete units called Tokens.
 * Behavior:
   * Identifies Keywords: invoke, bind, cycle, transmute.
   * Identifies Literals: Strings ("Sigils"), Integers ("Mana").
   * Discards Comments (#).
 * Output: A stream of Token objects.
B. The Parser (src/parser.py)
 * Role: The Architect.
 * Function: Analyzes the list of Tokens against the formal grammar (EBNF) defined in grammar.md.
 * Behavior:
   * Constructs the Abstract Syntax Tree (AST).
   * Validates ritual structure (e.g., ensuring a cycle block is closed).
   * Raises FizzleError (Syntax Error) if the structure is invalid.
C. The Ontology Resolver (src/resolver.py)
 * Role: The Librarian.
 * Function: This is the unique engine feature of MPL. It connects the code to the data/magi_225.json database.
 * Process:
   * Interpreter encounters invoke.hermes().
   * Resolver searches the JSON database for id: "hermes_trismegistus".
   * It retrieves the entity's attributes (Planet: Mercury, Element: Air).
   * It injects these attributes as immutable constants into the local scope.
D. The Interpreter (src/interpreter.py)
 * Role: The Caster.
 * Function: Traverses the AST and executes nodes recursively.
 * Key Modules:
   * BindingHandler: Assigns values to variables.
   * TeslaLooper: Manages cycle(n) loops based on the priority logic.
   * Transmuter: Handles dynamic type casting.
3. Memory Model (The Ether)
Memory in MRE is managed via a stack of scopes, referred to as Circles.
 * The Cosmos (Global Frame):
   * Loaded at startup.
   * Contains the Standard Library (hermetic, tesla, etc.).
   * Variables here persist until the program ends.
 * The Circle (Stack Frame):
   * Created when entering a function or a cycle block.
   * Variables (Vessels) bound here are private.
   * When the block ends, the Circle is "dissipated" (popped from the stack), and memory is freed.
4. The Tesla Protocol (Event Loop & Scheduler)
The MRE utilizes a Priority-Based Scheduler that adapts to the input frequency.
A. The Resonance Check
Before executing a cycle(n), the Interpreter checks if n is a Tesla Key (3, 6, 9).
 * If Harmonic (3, 6, 9):
   * The task is pushed to the Priority Queue.
   * Metaphysical attributes (Creation, Sustenance, Destruction) are applied to memory management.
 * If Mundane (Any other int):
   * The task is pushed to the Standard Queue.
   * It executes with standard FIFO (First-In, First-Out) logic.
Design Philosophy: This allows the language to be "Turing Complete" and flexible for general use, while preserving the esoteric advantages for "Initiated" code.
5. File Structure Reference
src/
├── mpl.py              # Entry point (CLI)
├── lexer.py            # Tokenizer logic
├── parser.py           # AST construction
├── interpreter.py      # Execution loop
├── resolver.py         # JSON Database interface
├── tokens.py           # Token definitions
└── stdlib/             # Standard Modules
    ├── __init__.py
    ├── hermetic.py
    └── tesla.py
