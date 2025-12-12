# FILE: src/modules/occultator.py
# PROJECT: MPL (Magic Programming Language)
# MODULE: OCCULTATOR ENGINE (Core Math Library)
# AUTHOR: Miela Labs LLC
# VIZYON: Bridging Tesla Harmonics, Fibonacci Sequences, and Solomonic Math.

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

# --- SYSTEM DIAGNOSTICS (MIELA ANALYSIS) ---
if __name__ == "__main__":
    engine = Occultator()
    print("\n--- [MIELA LABS] ENTITY ANALYSIS ---")
    
    # Hedef İsim
    entity_name = "MIELA"
    
    # 1. RAW ENERGY (ASCII Toplamı)
    # Bilgisayar dilinde harflerin toplam enerjisi
    raw_energy = sum(ord(c) for c in entity_name)
    
    print(f">> TARGET: {entity_name}")
    print(f"   [RAW DIGITAL ENERGY] : {raw_energy}") 
    
    # 2. TESLA (Titreşim)
    tesla_vib = engine.calculate(raw_energy, 'TESLA')
    print(f"   [TESLA 3-6-9]        : {tesla_vib}")
    
    # 3. FIBONACCI (Piyasa Uyumu)
    fib_level = engine.calculate(raw_energy, 'FIBONACCI')
    print(f"   [FIBONACCI LEVEL]    : {fib_level}")
    
    # 4. SOLOMON (Mühür)
    solomon_key = engine.calculate(entity_name, 'SOLOMON')
    print(f"   [SOLOMON PRIME KEY]  : {solomon_key}")
    
    print("\n>> ANALYSIS COMPLETE.")
