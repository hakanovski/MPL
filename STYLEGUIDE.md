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
