# FILE: src/modules/occultator.py
# PROJECT: MPL (Magic Programming Language)
# MODULE: OCCULTATOR ENGINE (Core Math Library)
# AUTHOR: Miela Labs LLC

import math

class Occultator:
    """
    The central processing unit for all esoteric calculations in MPL.
    This engine supports multiple modes of operation:
    1. TESLA (3-6-9 Reduction) - For Vibrational Analysis
    2. FIBONACCI (Golden Ratio) - For Market Trends
    3. SOLOMON (Prime Keys) - For Entity Security/ID
    """

    def __init__(self):
        # Silent init typically, but printing for system check
        pass

    # --- MODULE A: THE TESLA COIL (Vibration) ---
    def reduce_tesla(self, number):
        """
        Applies Tesla's 3-6-9 reduction logic (Digital Root).
        Reduces any multi-digit number to a single digit (1-9).
        Example: 452 -> 4+5+2=11 -> 1+1=2.
        """
        try:
            n = int(number)
            if n == 0:
                return 0
            # Mathematical shortcut for Digital Root
            return (n - 1) % 9 + 1
        except ValueError:
            return 0

    # --- MODULE B: THE GOLDEN SPIRAL (Expansion) ---
    def expand_fibonacci(self, target_number):
        """
        Finds the nearest Fibonacci number to the input.
        This aligns abstract magic numbers with market reality.
        """
        try:
            target = int(target_number)
            if target <= 0: return 0
            
            # Generate Fibonacci sequence
            a, b = 0, 1
            while b < target:
                a, b = b, a + b
            
            # Check which is closer: the one below (a) or the one above (b)
            if abs(target - a) <= abs(b - target):
                return a
            else:
                return b
        except ValueError:
            return 0

    # --- MODULE C: THE PRIME KEY (Identity) ---
    def generate_solomon_key(self, text_input):
        """
        Converts text into a unique Prime Number sequence (ASCII Sum -> Next Prime).
        Used for generating unique IDs or 'Seals'.
        """
        # 1. Calculate raw ASCII sum
        raw_sum = sum(ord(char) for char in text_input)
        
        # 2. Find the next prime number >= raw_sum
        def is_prime(n):
            if n <= 1: return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        candidate = raw_sum
        while not is_prime(candidate):
            candidate += 1
            
        return candidate

    # --- HELPER: MASTER CALCULATOR ---
    def calculate(self, input_value, mode="TESLA"):
        """
        Main entry point. Routes the input to the correct module.
        """
        if mode == "TESLA":
            return self.reduce_tesla(input_value)
        elif mode == "FIBONACCI":
            return self.expand_fibonacci(input_value)
        elif mode == "SOLOMON":
            return self.generate_solomon_key(input_value)
        else:
            return None

# --- SYSTEM DIAGNOSTICS (Run this file directly to test) ---
if __name__ == "__main__":
    engine = Occultator()
    print("\n--- [MIELA LABS] OCCULTATOR DIAGNOSTICS ---")
    
    # Test 1: PAIMON (452)
    paimon_raw = 452
    print(f">> INPUT: PAIMON ({paimon_raw})")
    print(f"   [TESLA MODE]    Vibration: {engine.calculate(paimon_raw, 'TESLA')}") 
    print(f"   [FIBONACCI]     Market Lvl: {engine.calculate(paimon_raw, 'FIBONACCI')}")
    
    # Test 2: ABADDON (Text)
    abaddon_txt = "ABADDON"
    print(f"\n>> INPUT: {abaddon_txt}")
    print(f"   [SOLOMON MODE]  Prime Seal: {engine.calculate(abaddon_txt, 'SOLOMON')}")
    
    print("\n>> SYSTEM STATUS: OPERATIONAL 100%")
