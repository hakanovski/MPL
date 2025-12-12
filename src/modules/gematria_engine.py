"""
FILE: gematria_engine.py
DESC: Core logic for converting metaphysical entities into numerical values suitable for algorithmic trading.
METHOD: ASCII Summation & Tesla Harmonic Reduction.
"""

def calculate_ascii_gematria(name):
    """
    Calculates the 'Technomantic Value' of a string by summing the ASCII values of its characters.
    
    Args:
        name (str): The name of the entity (e.g., "PAIMON").
    
    Returns:
        int: The sum of ASCII values (e.g., P(80)+A(65)... = 452).
    """
    if not name:
        return 0
    return sum(ord(char) for char in name.upper())

def apply_tesla_reduction(raw_value):
    """
    Reduces the high raw Gematria value into usable TradingView 'Lookback Periods'
    using Tesla's 3-6-9 harmonic principles.
    
    Args:
        raw_value (int): The raw ASCII sum (e.g., 452).
        
    Returns:
        dict: A dictionary containing the harmonics for different timeframe strategies.
    """
    return {
        "raw_trend": raw_value,              # Long-term Baseline (e.g., Yearly Trend)
        "harmonic_3": int(raw_value / 3),    # Medium-term Signal (Standard Entry)
        "harmonic_6": int(raw_value / 6),    # Short-term Signal (Fast Entry/Exit)
        "harmonic_9": int(raw_value / 9)     # Scalping Signal (High Frequency)
    }

# --- UNIT TEST (Uncomment to verify) ---
# if __name__ == "__main__":
#     spirit = "PAIMON"
#     val = calculate_ascii_gematria(spirit)
#     harmonics = apply_tesla_reduction(val)
#     print(f"Entity: {spirit}")
#     print(f"Raw Value: {val}")
#     print(f"Harmonics: {harmonics}")
