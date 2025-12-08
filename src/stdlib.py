"""
src/stdlib.py
====================================
The Standard Library (The Grimoire).
Patched v0.9.1 to support 'summon_daemon.ms' and JSON Mapping.
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
import os

# ==========================================
# 1. HERMETIC (Alchemy & Data)
# ==========================================
class Hermetic:
    """Domain: Transformation, Elemental Types, State Management."""
    
    @staticmethod
    def transmute(target, target_type):
        """Converts a variable to a specific type."""
        # MPL Types mapping
        t_str = str(target_type)
        if t_str in ["Mana", "int", "Integer"]:
            try: return int(target)
            except: return 0
        elif t_str in ["Sigil", "str", "String"]:
            return str(target)
        elif t_str in ["Flux", "float"]:
            try: return float(target)
            except: return 0.0
        return target

    @staticmethod
    def purify(vessel):
        if isinstance(vessel, str): return vessel.strip()
        if isinstance(vessel, list): return [x for x in vessel if x is not None]
        return vessel

# ==========================================
# 2. SOLOMONIC (System, Processes & Daemons)
# ==========================================
class Solomonic:
    """Domain: Daemons, Threads, OS Interaction."""
    
    active_daemons = {}

    @staticmethod
    def summon(command):
        print(f"👹 [SOLOMONIC] Summoning daemon: '{command}'")
        try:
            args = shlex.split(command)
            proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            pid = proc.pid
            Solomonic.active_daemons[pid] = proc
            return pid
        except Exception as e:
            print(f"⚠️ Summoning failed: {e}")
            return -1

    @staticmethod
    def bind(pid, resource_limit=None):
        if pid in Solomonic.active_daemons:
            print(f"⛓️ [SOLOMONIC] Binding Spirit #{pid} (Limit: {resource_limit})...")
            return True
        return False

    @staticmethod
    def banish(pid):
        if pid in Solomonic.active_daemons:
            print(f"⚔️ [SOLOMONIC] Banishing Spirit #{pid}...")
            try:
                proc = Solomonic.active_daemons[pid]
                proc.terminate()
                del Solomonic.active_daemons[pid]
            except: pass
            return True
        return False

    # --- TECHNOMANCY MAPPINGS FOR GOETIA (JSON SUPPORT) ---
    # These methods map directly to 72_solomon_sigil_shapes.json functions
    
    @staticmethod
    def hide(pid=None):
        """Used by Bael (001). Simulates cloaking."""
        print("👻 [PROCESS] Casting veil of invisibility (Stealth Mode Activated)...")
        return True

    @staticmethod
    def root_access():
        """Used by Paimon (009). Simulates sudo/admin request."""
        user = os.getenv('USER', 'Initiate')
        print(f"👑 [SYSTEM] Elevating privileges for user '{user}'... Root Access Granted.")
        return True

# ==========================================
# 3. TESLA (Time & Frequency)
# ==========================================
class Tesla:
    @staticmethod
    def oscillate(hz):
        print(f"⚡ [TESLA] Oscillating system at {hz}Hz...")
        time.sleep(hz)

    @staticmethod
    def amplify(signal, factor):
        if factor not in [3, 6, 9]:
            print("⚠️ [TESLA] Dissonance detected.")
        return signal * factor

# ==========================================
# 4. DIVINATION (I/O & Randomness)
# ==========================================
class Divination:
    @staticmethod
    def inscribe(message):
        print(f"📝 {message}")
    
    @staticmethod
    def scry(url):
        # ... (mevcut kod aynı kalabilir)
        return "Data"

# ==========================================
# THE GATEWAY (Standard Library Registry)
# ==========================================
class StdLib:
    """
    The main registry. 
    UPDATED: Includes aliases for JSON compatibility.
    """
    modules = {
        # Core Modules
        "hermetic": Hermetic,
        "solomonic": Solomonic,
        "tesla": Tesla,
        "divination": Divination,
        # "runic": Runic, # (Eğer runic sınıfı varsa ekle)

        # --- JSON Mapping Aliases ---
        # 72_solomon.json calls "process.hide", so we map "process" -> Solomonic
        "process": Solomonic,
        "system": Solomonic,
        "network": Divination, # Orobas 'network.sniffer' kullanıyor
        "alchemy": Hermetic    # Zagan 'alchemy.master' kullanıyor
    }

    @staticmethod
    def call(module_name, func_name, args):
        if module_name in StdLib.modules:
            module = StdLib.modules[module_name]
            if hasattr(module, func_name):
                method = getattr(module, func_name)
                # Handle argument mismatch gracefully for prototype
                try:
                    return method(*args)
                except TypeError:
                    # If args don't match, call without args (mock behavior)
                    return method()
        
        print(f"⚠️ [FIZZLE] Unknown ritual: {module_name}.{func_name}")
        return None
