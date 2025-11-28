# 📐 MPL Language Specification

**Version:** 0.1.0-alpha
**Status:** Draft

---

## 1. Introduction

The **Magick Programming Language (MPL)** is an interpreted, domain-specific language (DSL) designed to map high-level esoteric intent to low-level computational logic. Unlike traditional languages that prioritize speed or efficiency, MPL prioritizes **structure, resonance, and ontological mapping**.

The runtime treats every script execution as a "Ritual" and every variable assignment as a "Binding."

---

## 2. Type System (The Elemental Types)

MPL employs a strong, dynamic typing system. Data types are named after alchemical and elemental concepts to reflect their mutable nature.

| MPL Type | Python Equivalent | Symbol | Description |
| :--- | :--- | :--- | :--- |
| **Sigil** | `str` | `"` | Textual data, intent strings, or ASCII art. Immutable. |
| **Mana** | `int` | `#` | Discrete numerical values. Used for counters and resource allocation. |
| **Flux** | `float` | `~` | Continuous values. Used for probability, frequency, and time. |
| **Polarity** | `bool` | `±` | Binary state. `True` (Active/Yang) or `False` (Passive/Yin). |
| **Vessel** | `dict/object` | `{}` | A container that holds other types or attributes. |
| **Void** | `None` | `ø` | Absence of value, or a cleared memory block. |

### Type Conversion (Transmutation)
Explicit conversion is handled via the `transmute` keyword.
```mpl
bind intent to "369"        # Type: Sigil
transmute intent -> Mana    # Type: Mana (369)

3. Scoping Rules (The Circles)
MPL manages memory visibility through the concept of Circles.
3.1 The Cosmos (Global Scope)
Variables bound at the top level of a script are visible everywhere. They represent universal constants.
3.2 The Circle (Local Scope)
Code blocks defined within cycle loops, if statements, or function definitions form a "Circle."
 * Containment: Variables bound inside a Circle cannot be accessed outside of it.
 * Leakage (DissipationError): Attempting to access a local variable from the Cosmos results in a DissipationError.
<!-- end list -->
bind universal_law to 42    # Cosmos

cycle(3) {
    bind secret to 7        # Circle (Local)
}

# Accessing 'secret' here causes DissipationError.

4. The Tesla Protocol (Execution Logic)
MPL does not use a standard binary execution loop. It utilizes the Tesla Protocol, a priority-based event loop governed by the numbers 3, 6, and 9.
4.1 Resonance Keys
 * Key 3 (Creation): High priority. Used for initialization, allocation, and summoning.
 * Key 6 (Sustenance): Medium priority. Used for maintaining state, monitoring, and standard operations.
 * Key 9 (Completion): Absolute priority. Used for garbage collection, closing connections, and banishing.
4.2 The cycle(n) Construct
Loops in MPL must be declared with a frequency (n).
cycle(3) { ... }  # Runs 3 times (Creation Phase)
cycle(6) { ... }  # Runs 6 times (Oscillation Phase)
cycle(9) { ... }  # Runs 9 times (Release Phase)

5. Ontology Resolution
MPL is "Ontology-Aware." It does not view functions as mere code blocks, but as entities with attributes.
When the interpreter encounters invoke.entity_id():
 * Lookup: It searches data/magi_225.json for the entity_id.
 * Context Injection: It loads the entity's attributes (Element, Planet, Frequency) into the current scope.
 * Role Check: It verifies if the entity's system_role (e.g., Firewall, Predictor) matches the attempted operation.
Example: Invoking a "Healer" entity (like Paracelsus) automatically enables error-correction modules for that block.
6. Error Handling (Backfire Protocols)
MPL categorizes errors based on their metaphysical impact on the system.
| Error Name | Cause | Handling Strategy |
|---|---|---|
| Fizzle | Syntax Error | The script refuses to run. The intent was unclear. |
| Backfire | Runtime Logic Error | The script halts to prevent system damage. |
| Corruption | Memory/Resource Overflow | The runtime executes an emergency banish() on all processes. |
| Dissipation | Scoping Error | A variable was lost to the Void. |
7. Comments
Comments are marked with the # symbol.
 * Single line: # This is a comment
 * They are treated as "Silent Intent" and are ignored by the Lexer but preserved in the AST for documentation.
<!-- end list -->

