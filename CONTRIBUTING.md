# 🤝 Contributing to MPL

**Welcome, Initiate.**

Thank you for your interest in contributing to the **Magick Programming Language (MPL)**. We are not just building a programming language; we are digitizing centuries of esoteric wisdom into executable logic.

Whether you are a **Python Developer (Artificer)**, an **Occult Researcher (Scribe)**, or a **Systems Architect**, your contributions are valuable to the Order.

---

## 📜 The Philosophy

Before contributing, please understand that MPL treats code as a ritual.
1.  **Intent Matters:** Code should be readable, precise, and purposeful.
2.  **As Above, So Below:** High-level abstractions must cleanly map to low-level machine logic.
3.  **Respect the Lineage:** When adding historical figures or traditions to the ontology, accuracy and cultural respect are paramount.

---

## 🛠️ How to Contribute

There are three main ways you can contribute to the repository:

### 1. The Core Engine (Python Devs)
Work on the Interpreter, Lexer, Parser, or the Magic Runtime Environment (MRE).
* **Focus:** Performance, AST generation, memory management.
* **Language:** Python 3.8+ (eventually Rust for core modules).

### 2. The Ontology (Researchers)
Expand the database of historical magicians, deities, and correspondences.
* **Task:** Update `data/magi_225.json` or `ONTOLOGY.md`.
* **Requirement:** Provide historical sources (e.g., *Agrippa, The Golden Bough, The Kybalion*) in your PR description.

### 3. The Grimoire (Documentation)
Help us write tutorials, fix typos, or clarify complex concepts.
* **Task:** Update `README.md`, `docs/`, or create new examples in `examples/`.

---

## ⚡ Development Setup

1.  **Fork** the repository to your GitHub account.
2.  **Clone** the project to your local machine (your Temple):
    ```bash
    git clone [https://github.com/YOUR_USERNAME/MPL.git](https://github.com/YOUR_USERNAME/MPL.git)
    cd MPL
    ```
3.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🔄 Pull Request (PR) Process

1.  **Create a Branch:** Never work directly on `main`. Create a feature branch:
    * `feature/tesla-protocol`
    * `fix/lexer-typo`
    * `data/add-paracelsus`
2.  **Commit Your Rites:** Write clear, concise commit messages.
    * *Bad:* "Fixed stuff"
    * *Good:* "Implemented the 3-6-9 looping logic in the Parser"
3.  **Submit a Pull Request:**
    * Go to the original MPL repository.
    * Click "New Pull Request."
    * Describe your changes. If you are adding a new Magician to the database, cite your source.
4.  **Review:** The Maintainers (The Circle) will review your code. Be open to feedback.

---

## 📐 Style Guide

### Python Code (The Logic)
* Follow **PEP 8** standards.
* Use **Type Hinting** everywhere. We want strict typing to prevent "magical mishaps."
    ```python
    # Good
    def invoke_spirit(name: str, frequency: int) -> bool:
    ```

### MPL Script (The Magic)
* When writing example `.ms` files, use descriptive variable names.
* **Naming Convention:** Snake_case for variables (`mana_pool`), PascalCase for Constructs (`HermeticCircle`).

---

## 🛡️ Code of Conduct

* **No Malificium:** Do not submit malicious code or logic intended to harm systems.
* **Respect:** This project touches on sensitive cultural and religious topics. Treat all traditions (Western, Eastern, Shamanic, etc.) with dignity.
* **Patience:** We are all students of the Great Work. Be kind in code reviews.

---

*"Any sufficiently advanced technology is indistinguishable from magic."* — Arthur C. Clarke
