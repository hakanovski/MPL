# 📚 Standard Library Overview (The Grimoire)

**Version:** 0.1.0-alpha

The **Magick Standard Library (StdLib)** is a collection of built-in modules available in the *Cosmos* (Global Scope) of every MPL script. These modules provide the essential tools for manipulating data, controlling time, and managing system processes.

To use a module, it is automatically available or can be explicitly imported via `invoke`.

---

## 1. Module: `hermetic` (Alchemy & Data)
**Domain:** Transformation, Elemental Types, and State Management.

This module handles the transmutation of data types and the purification of variables.

| Function | Signature | Description |
| :--- | :--- | :--- |
| **transmute** | `transmute(target, type)` | Converts a variable to a specific type (e.g., String to Int). |
| **purify** | `purify(vessel)` | Removes `Void` (None) values or whitespace from a container. |
| **fuse** | `fuse(vessel_a, vessel_b)` | Merges two dictionaries or lists (Alchemical Union). |
| **distill** | `distill(vessel, filter)` | Filters a list based on a condition. |

### Example
```mpl
bind lead to "  369  "
bind gold to hermetic.transmute(hermetic.purify(lead), Mana)
# Result: gold is now the integer 369

2. Module: solomonic (System & Processes)
Domain: Daemons, Threads, and OS Interaction.
Inspired by the Lemegeton, this module treats operating system processes as "Spirits" or "Daemons" that can be summoned, bound, or banished.
| Function | Signature | Description |
|---|---|---|
| summon | summon(command) | Spawns a new subprocess (Daemon). Returns a PID. |
| bind | bind(pid, resource) | Limits the CPU/Memory usage of a specific process. |
| banish | banish(pid) | Terminates a process immediately (SIGKILL). |
| invoke_shell | invoke_shell(cmd) | Executes a standard shell command. |
Example
# Summon a Python web server daemon
bind server_daemon to solomonic.summon("python -m http.server")

cycle(9) {
    # Keep it alive for 9 cycles
    solomonic.bind(server_daemon, memory_limit=512)
}

solomonic.banish(server_daemon)

3. Module: tesla (Time & Frequency)
Domain: Loops, Delays, and Energy Flow.
This module replaces standard time libraries. It relies on the concept of resonance rather than linear seconds.
| Function | Signature | Description |
|---|---|---|
| oscillate | oscillate(hz) | Pauses execution (Sleep). 1 Hz ≈ 1 Second. |
| amplify | amplify(signal, factor) | Multiplies a value by 3, 6, or 9. |
| resonate | resonate(target) | Checks if a value is divisible by 3, 6, or 9. |
Example
# Wait for 3 seconds (3 Hz oscillation)
tesla.oscillate(3)

4. Module: divination (I/O & Randomness)
Domain: Input, Output, Networking, and RNG.
Used for "seeing" data from the outside world (APIs) or generating entropy.
| Function | Signature | Description |
|---|---|---|
| scry | scry(url) | Performs an HTTP GET request to fetch data. |
| tarot_seed | tarot_seed() | Generates a cryptographically secure random seed. |
| cast_lots | cast_lots(min, max) | Generates a random integer (Mana) between min and max. |
| inscribe | inscribe(message) | Prints output to the console (STDOUT). |
Example
bind oracle_data to divination.scry("[https://api.coingecko.com/api/v3/simple/price?ids=bitcoin](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin)")
divination.inscribe(oracle_data)

5. Module: runic (String & Encoding)
Domain: Text Manipulation, Encryption, and Sigils.
| Function | Signature | Description |
|---|---|---|
| encode | encode(text, method) | Encodes string to Base64, Hex, or Rot13. |
| bind_rune | bind_rune(char, value) | Replaces specific characters in a string. |
| forge_sigil | forge_sigil(intent) | Removes vowels and duplicates from a string to create a Sigil. |
Example
bind intent to "I WILL SUCCEED"
bind final_sigil to runic.forge_sigil(intent)
# Result: "WLSCCD"
