# 🕯️ MPL Style Guide (The Book of Law)

> *"Order is the first law of Heaven."* — Ancient Maxim

To maintain the potency and readability of the **Magick Programming Language (MPL)**, all Initiates and Adepts are expected to follow these coding conventions.

Whether you are writing **MagickScript (`.ms`)** rituals or contributing to the **Python Engine (`.py`)**, adherence to this guide ensures that the logic flows without resistance.

---

## 1. MagickScript (`.ms`) Conventions

When writing rituals in MPL, treat the code as a stanza of poetry. It should be readable, rhythmic, and clear.

### A. Naming Conventions (The True Names)

| Component | Convention | Style | Example |
| :--- | :--- | :--- | :--- |
| **Variables (Vessels)** | `snake_case` | Lowercase with underscores | `mana_pool`, `target_entity` |
| **Functions (Rites)** | `snake_case` | Lowercase with underscores | `cast_protection()`, `invoke_hermes()` |
| **Classes (Egregors)** | `PascalCase` | Capitalize first letters | `ProtectionCircle`, `PhilosopherStone` |
| **Constants (Truths)** | `UPPER_CASE` | All caps with underscores | `MAX_ENTROPY`, `PLANCK_CONSTANT` |

### B. Indentation (Sacred Geometry)
* **Standard:** Use **4 Spaces**. Do NOT use tabs.
* **Visual Hierarchy:** Indentation represents the depth of the ritual circle. Code inside a `cycle` or `if` block must be indented to show it is "contained" within that energy field.

```mpl
# Bad
cycle(3) {
invoke.hermes()
}

# Good
cycle(3) {
    invoke.hermes()
}

C. Comments (Marginalia)
Comments are not just notes; they are the Intent behind the code.
 * Use # for comments.
 * Rule: Do not explain what the code is doing (the syntax shows that). Explain why you are doing it.
<!-- end list -->
# Bad
# Bind x to 10
bind x to 10

# Good
# Setting the threshold for the entropy sensor
bind entropy_threshold to 10

D. File Extensions
 * All MPL scripts must end with .ms.
 * Example: ritual_of_clarity.ms
2. Python Engine (.py) Conventions
For those contributing to the MRE (Magic Runtime Engine) source code:
A. PEP 8 Compliance
 * We strictly follow PEP 8 standards.
 * Use black and flake8 (configured in our .pre-commit-config.yaml) to automatically format your code before committing.
B. Type Hinting
 * Strict Typing: All function signatures must use Python Type Hints. We are dealing with abstract logic; we cannot afford ambiguity.
<!-- end list -->
# Correct
def transmute_energy(source: str, amount: int) -> float:
    pass

# Incorrect
def transmute_energy(source, amount):
    pass

C. Docstrings
 * Use triple quotes """ for docstrings.
 * Follow the Google Style docstring format.
3. Best Practices (The Wisdom)
A. The Law of Closure
Always close what you open.
 * If you summon a process, you must eventually banish it.
 * If you open a cycle, ensure it has an exit condition.
B. The Law of Containment (Scope)
 * Do not rely on Global Variables (The Cosmos) unless absolutely necessary.
 * Keep variables local to their cycle (The Circle) to prevent "Dissipation Errors" (Memory Leaks).
C. The Tesla Protocol
 * When defining loops, prefer the sacred numbers 3, 6, and 9.
 * 3: For creation and initialization.
 * 6: For maintenance and oscillation.
 * 9: For destruction and completion.
"A messy ritual invites messy spirits. Keep your code clean."
