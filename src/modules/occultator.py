# FILE: src/modules/occultator.py
# PROJECT: MPL (Magic Programming Language)
# MODULE: OCCULTATOR ENGINE (Core Math Library)
# AUTHOR: Miela Labs LLC
# RESEARCH SOURCE: Deep Analysis of John Dee's Enochian System & Sigil Dei Aemeth

import math

# --- CONSTANTS: THE HOLY DATA STRUCTURES ---

# 1. THE SIGIL OUTER RING (Source: Sigil Dei Aemeth Analysis)
# "Thaaoth..." sequence used for modulo extraction.
SIGIL_RING = "thaaoth-aoiveae-thaoth-aoiveae-thaoth-aoiveae-thaoth"

# 2. THE WATCHTOWER GRID (Simplified 7x7 Fractal Block from Great Table)
# Used for coordinate mapping (X, Y).
ENOCHIAN_GRID = [
    ['r', 'Z', 'i', 'l', 'a', 'f', 'A'],
    ['y', 't', 'l', 'p', 'a', 'e', 'L'],
    ['o', 'a', 'C', 'V', 'c', 'a', 'u'],
    ['n', 'i', 'n', 'b', 'Z', 'i', 'x'],
    ['i', 'a', 's', 'o', 'm', 't', 'P'],
    ['e', 'x', 'a', 'r', 'p', 'h', 'o'],
    ['n', 'a', 'n', 't', 'a', 'b', 'M']
]

class Occultator:
    """
    The central processing unit for all esoteric calculations in MPL.
    UPDATED V2.0: Includes John Dee's Algorithmic logic.
    
    MODES:
    1. TESLA (3-6-9)     -> Vibrational Root
    2. FIBONACCI         -> Market Expansion
    3. SOLOMON (Prime)   -> Unique Identity
    4. ENOCHIAN (Dee)    -> Coordinate Extraction (X,Y)
    5. SIGIL (Galethog)  -> Circular Cipher
    """

    def __init__(self):
        pass

    # --- MODULE A: THE TESLA COIL (Vibration) ---
    def reduce_tesla(self, number):
        """
        Applies Tesla's 3-6-9 reduction logic (Digital Root).
        """
        try:
            n = int(number)
            if n == 0: return 0
            return (n - 1) % 9 + 1
        except ValueError:
            return 0

    # --- MODULE B: THE GOLDEN SPIRAL (Expansion) ---
    def expand_fibonacci(self, target_number):
        """
        Finds the nearest Fibonacci number.
        Aligns magic with market reality.
        """
        try:
            target = int(target_number)
            if target <= 0: return 0
            a, b = 0, 1
            while b < target:
                a, b = b, a + b
            return a if abs(target - a) <= abs(b - target) else b
        except ValueError:
            return 0

    # --- MODULE C: THE PRIME KEY (Identity) ---
    def generate_solomon_key(self, text_input):
        """
        Converts text into a unique Prime Number Seal.
        """
        raw_sum = sum(ord(char) for char in text_input)
        def is_prime(n):
            if n <= 1: return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0: return False
            return True
        candidate = raw_sum
        while not is_prime(candidate):
            candidate += 1
        return candidate

    # --- MODULE D: THE ENOCHIAN WATCHTOWER (Coordinates) ---
    # Based on Source [106, 121]: Vector-based extraction.
    def map_enochian_coordinates(self, text):
        """
        Maps an entity name to specific coordinates on the Great Table.
        Returns a 'Vector Sum' useful for Support/Resistance lines.
        """
        x_sum = 0
        y_sum = 0
        
        # Simple hash to map letters to our 7x7 Fractal Grid
        for char in text.lower():
            val = ord(char)
            x = val % 7
            y = (val * 3) % 7 # Stride of 3
            
            # Extract power from the grid
            grid_char = ENOCHIAN_GRID[y][x]
            x_sum += x
            y_sum += y
            
        # The "Vector Path" value
        vector_power = (x_sum * y_sum) + 49 # Adding the 49 Gate Constant
        return vector_power

    # --- MODULE E: THE SIGIL ENGINE (Galethog Algorithm) ---
    # Based on Source [46-52]: Polyalphabetic Cipher with Stride.
    def execute_galethog_cipher(self, text):
        """
        Calculates a 'Stride' based on the input, then extracts
        a hidden value from the Sigil Outer Ring.
        Formula: Index = (Start + (n * Stride)) % Length
        """
        # 1. Determine Stride (Key) from input
        stride = sum(ord(c) for c in text) % 40
        if stride == 0: stride = 7 # Default to planetary factor
        
        extracted_value = 0
        ring_len = len(SIGIL_RING)
        
        # 2. Run the extraction loop
        current_index = 0
        for i in range(len(text)):
            # The Galethog Jump
            current_index = (current_index + stride) % ring_len
            char_at_sigil = SIGIL_RING[current_index]
            extracted_value += ord(char_at_sigil)
            
        return extracted_value

    # --- HELPER: MASTER CALCULATOR ---
    def calculate(self, input_value, mode="TESLA"):
        """
        Main routing logic.
        """
        if mode == "TESLA":
            return self.reduce_tesla(input_value)
        elif mode == "FIBONACCI":
            return self.expand_fibonacci(input_value)
        elif mode == "SOLOMON":
            return self.generate_solomon_key(input_value)
        elif mode == "ENOCHIAN":
            return self.map_enochian_coordinates(input_value)
        elif mode == "SIGIL":
            return self.execute_galethog_cipher(input_value)
        else:
            return 0

# --- SYSTEM DIAGNOSTICS (UPDATED FOR DEEP RESEARCH) ---
if __name__ == "__main__":
    engine = Occultator()
    print("\n--- [MIELA LABS] DEEP RESEARCH DIAGNOSTICS ---")
    
    target = "MIELA"
    
    print(f">> TARGET ENTITY: {target}")
    
    # 1. BASIC LAYERS
    raw = sum(ord(c) for c in target)
    print(f"   [RAW ENERGY]       : {raw}")
    print(f"   [TESLA 3-6-9]      : {engine.calculate(raw, 'TESLA')}")
    print(f"   [FIBONACCI]        : {engine.calculate(raw, 'FIBONACCI')}")
    
    # 2. ADVANCED LAYERS (New Research)
    enochian_vector = engine.calculate(target, 'ENOCHIAN')
    print(f"   [ENOCHIAN VECTOR]  : {enochian_vector} (Grid Power)")
    
    sigil_code = engine.calculate(target, 'SIGIL')
    print(f"   [SIGIL/GALETHOG]   : {sigil_code} (Hidden Cipher)")
    
    print("\n>> SYSTEM STATUS: ENOCHIAN GATES OPEN.")
