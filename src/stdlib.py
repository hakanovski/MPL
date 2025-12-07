"""
src/stdlib.py
====================================
The Standard Library (The Grimoire).
Implements the core modules defined in stdlib_overview.md.
"""

import time
import sys
import subprocess
import shlex
import urllib.request
import json
import random
import base64
import re

# ==========================================
# 1. HERMETIC (Alchemy & Data)
# ==========================================
class Hermetic:
    """Domain: Transformation, Elemental Types, State Management."""
    
    @staticmethod
    def transmute(target, target_type):
        """Converts a variable to a specific type."""
        # MPL Types mapping
        if str(target_type) in ["Mana", "int"]:
            try: return int(target)
            except: return 0
        elif str(target_type) in ["Sigil", "str"]:
            return str(target)
        elif str(target_type) in ["Flux", "float"]:
            try: return float(target)
            except: return 0.0
        return target

    @staticmethod
    def purify(vessel):
        """Removes Void values or whitespace."""
        if isinstance(vessel, str):
            return vessel.strip()
        if isinstance(vessel, list):
            return [x for x in vessel if x is not None]
        return vessel

    @staticmethod
    def fuse(vessel_a, vessel_b):
        """Merges two collections (Alchemical Union)."""
        if isinstance(vessel_a, dict) and isinstance(vessel_b, dict):
            return {**vessel_a, **vessel_b}
        if isinstance(vessel_a, list) and isinstance(vessel_b, list):
            return vessel_a + vessel_b
        return str(vessel_a) + str(vessel_b)

# ==========================================
# 2. SOLOMONIC (System & Processes)
# ==========================================
class Solomonic:
    """Domain: Daemons, Threads, OS Interaction."""
    
    # Keep track of summoned spirits (processes)
    active_daemons = {}

    @staticmethod
    def summon(command):
        """Spawns a new subprocess (Daemon). Returns PID."""
        print(f"👹 [SOLOMONIC] Summoning daemon: '{command}'")
        try:
            args = shlex.split(command)
            # Starting process independently
            proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            pid = proc.pid
            Solomonic.active_daemons[pid] = proc
            return pid
        except Exception as e:
            print(f"⚠️ Summoning failed: {e}")
            return -1

    @staticmethod
    def bind(pid, resource_limit=None):
        """Limits a process (Mock implementation for v0.1)."""
        if pid in Solomonic.active_daemons:
            print(f"⛓️ [SOLOMONIC] Binding Spirit #{pid} (Limit: {resource_limit})...")
            # Real resource limiting requires 'resource' module (Unix only) or psutil.
            # For prototype, we just acknowledge the binding.
            return True
        return False

    @staticmethod
    def banish(pid):
        """Terminates a process immediately."""
        if pid in Solomonic.active_daemons:
            print(f"⚔️ [SOLOMONIC] Banishing Spirit #{pid}...")
            proc = Solomonic.active_daemons[pid]
            proc.terminate()
            del Solomonic.active_daemons[pid]
            return True
        return False

# ==========================================
# 3. TESLA (Time & Frequency)
# ==========================================
class Tesla:
    """Domain: Loops, Delays, Energy Flow."""

    @staticmethod
    def oscillate(hz):
        """Pauses execution. 1 Hz = 1 Second."""
        print(f"⚡ [TESLA] Oscillating system at {hz}Hz...")
        time.sleep(hz)

    @staticmethod
    def amplify(signal, factor):
        """Multiplies value. Warns if not harmonic (3, 6, 9)."""
        if factor not in [3, 6, 9]:
            print("⚠️ [TESLA] Warning: Non-harmonic amplification detects dissonance.")
        return signal * factor

# ==========================================
# 4. DIVINATION (I/O & Randomness)
# ==========================================
class Divination:
    """Domain: Input, Output, Networking, RNG."""

    @staticmethod
    def scry(url):
        """Performs HTTP GET request."""
        print(f"👁️ [DIVINATION] Scrying into the Aether: {url}")
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read().decode('utf-8')
                # Try to parse JSON if possible
                try: return json.loads(data)
                except: return data
        except Exception as e:
            return f"Void (Error: {e})"

    @staticmethod
    def tarot_seed():
        """Generates a random seed."""
        seed = random.randrange(100000, 999999)
        random.seed(seed)
        return seed

    @staticmethod
    def inscribe(message):
        """Prints output to console (STDOUT)."""
        print(f"📝 {message}")

# ==========================================
# 5. RUNIC (String & Encoding)
# ==========================================
class Runic:
    """Domain: Text Manipulation, Encryption."""

    @staticmethod
    def encode(text, method="base64"):
        if method == "base64":
            encoded = base64.b64encode(text.encode()).decode()
            return encoded
        return text

    @staticmethod
    def forge_sigil(intent):
        """Removes vowels and duplicates (Chaos Magick style)."""
        text = intent.upper()
        # Remove vowels
        text = re.sub(r'[AEIOU\s]', '', text)
        # Remove duplicates while keeping order
        sigil = "".join(dict.fromkeys(text))
        return sigil

# ==========================================
# THE GATEWAY (Standard Library Registry)
# ==========================================
class StdLib:
    """
    The main registry that connects string names to Python Classes.
    Used by the Interpreter to dispatch calls.
    """
    modules = {
        "hermetic": Hermetic,
        "solomonic": Solomonic,
        "tesla": Tesla,
        "divination": Divination,
        "runic": Runic
    }

    @staticmethod
    def call(module_name, func_name, args):
        if module_name in StdLib.modules:
            module = StdLib.modules[module_name]
            if hasattr(module, func_name):
                method = getattr(module, func_name)
                # Call the method with unpacked arguments
                return method(*args)
        
        print(f"⚠️ [FIZZLE] Unknown ritual: {module_name}.{func_name}")
        return None
