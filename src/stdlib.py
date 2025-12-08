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
        print(f"👁️ [DIVINATION] Scrying into the Aether: {url}")
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read().decode('utf-8')
                try: return json.loads(data)
                except: return data
        except Exception as e:
            return f"Void (Error: {e})"
            
    @staticmethod
    def cast_lots(min_val, max_val):
        return random.randint(min_val, max_val)

# ==========================================
# 5. RUNIC (Text & Sigils)
# ==========================================
class Runic:
    @staticmethod
    def forge_sigil(intent):
        text = intent.upper()
        text = re.sub(r'[AEIOU\s]', '', text)
        sigil = "".join(dict.fromkeys(text))
        return sigil

# ==========================================
# THE GATEWAY (Standard Library Registry)
# ==========================================
class StdLib:
    """
    The main registry. 
    Includes aliases for JSON compatibility.
    """
    modules = {
        # Core Modules
        "hermetic": Hermetic,
        "solomonic": Solomonic,
        "tesla": Tesla,
        "divination": Divination,
        "runic": Runic,

        # --- JSON Mapping Aliases ---
        "process": Solomonic,  # Maps 'process.hide' to Solomonic.hide
        "system": Solomonic,   # Maps 'system.root_access' to Solomonic.root_access
        "network": Divination, # Maps 'network.sniffer'
        "alchemy": Hermetic    # Maps 'alchemy.master'
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

# ==========================================
# 6. MARKET (Financial Technomancy)
# ==========================================
class Market:
    """Domain: TradingView Integration & Pine Script Generation."""

    @staticmethod
    def forge_pinescript(title, fast_len, slow_len, rsi_buy, rsi_sell, adx_thresh):
        """
        Takes magical parameters and injects them into the Hakan Yorganci Protocol.
        """
        print(f"📈 [MARKET] Forging Strategy: {title}...")
        
        # Pine Script Template (Senin kodun)
        # Değişkenleri {suslu_parantez} icine alarak dinamiklestirdim.
        script = f"""
//@version=6
// Generated by MPL (Magick Programming Language) v0.9.1
// Strategy: {title}
// Infused with Solomonic Intent

strategy("{title}", overlay=true, initial_capital=1000, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

//=== OPTIMIZED MAGICK INPUTS ===//
smaLenShort  = {fast_len}   // Magically tuned Support
smaLenLong   = {slow_len}  // Magically tuned Trend
buyRsiDipLvl = {rsi_buy}  // Sniper Level
sellRsiPeakLvl = {rsi_sell}
adxThreshold = {adx_thresh}

//=== STANDARD LOGIC ===//
useTrendFilter = true
useAdx = true
rsiLen = 14
rsiMaLen = 9

// Calculations
sma50  = ta.sma(close, smaLenShort)
sma200 = ta.sma(close, smaLenLong)
rsiVal   = ta.rsi(close, rsiLen)
rsiMaVal = ta.sma(rsiVal, rsiMaLen)
[diplus, diminus, adxVal] = ta.dmi(14, 14)
adxCondition = useAdx ? (adxVal > adxThreshold) : true

// Entry Logic
rsiCrossUp = ta.crossover(rsiMaVal, buyRsiDipLvl)
trendCondition = useTrendFilter ? (close > sma200) : true
longEntryCond = trendCondition and adxCondition and rsiCrossUp and strategy.position_size == 0

// Exit Logic
takeProfitCond = rsiMaVal > sellRsiPeakLvl
stopLossCond = close < sma50
longExitCond = (takeProfitCond or stopLossCond) and strategy.position_size > 0

// Execution
if longEntryCond
    strategy.entry("Magick Sniper", strategy.long, comment="Entry")

if longExitCond
    exitReason = takeProfitCond ? "TP (Magick)" : "SL (Magick)"
    strategy.close("Magick Sniper", comment=exitReason)

// Plotting
plot(sma50, color=color.orange, linewidth=2)
plot(sma200, color=color.blue, linewidth=3)
        """
        return script

# ... (Mevcut kodlar) ...

# GÜNCELLEME: StdLib Registry
class StdLib:
    modules = {
        "hermetic": Hermetic,
        "solomonic": Solomonic,
        "tesla": Tesla,
        "divination": Divination,
        "runic": Runic,
        
        # YENİ MODÜL:
        "market": Market, 
        
        # Aliaslar
        "process": Solomonic,
        "system": Solomonic,
        "network": Divination,
        "alchemy": Hermetic
    }
    # ... (call metodu aynı kalıyor)
