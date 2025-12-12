# FILE: hybrid_oracle.ms
# PROJECT: VASSAGO EYE V2 (Abramelin Integration)
# AUTHOR: H-Ankh-An
# TYPE: Direct Python Execution Script

import sys
import os
import json

# Python'un 'src' klasörünü bulabilmesi için yol ayarı
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Kendi motorumuzu çağırıyoruz
try:
    from src.modules import gematria_engine as Gematria
except ImportError:
    print("HATA: src/modules/gematria_engine.py bulunamadı. Klasör yapısını kontrol et.")
    sys.exit(1)

# --- 1. ENTITY SELECTION ---
# Primary: PAIMON (Ruler of Secret Knowledge)
# Secondary: ASTAROTH (Ruler of Past & Future)
entity_primary = "PAIMON"
entity_secondary = "ASTAROTH"

# --- 2. THE CALCULATION (Tesla Harmonic Reduction) ---

# Paimon dictates the TREND (Baseline)
paimon_raw = Gematria.calculate_ascii_gematria(entity_primary)
paimon_harmonics = Gematria.apply_tesla_reduction(paimon_raw)

# Astaroth dictates the SIGNAL (Entry/Exit)
astaroth_raw = Gematria.calculate_ascii_gematria(entity_secondary)
astaroth_harmonics = Gematria.apply_tesla_reduction(astaroth_raw)

# --- 3. SYSTEM OUTPUT ---
print("\n--- VASSAGO EYE V2 SYSTEM CHECK ---")
print(f">> Connection Established: {entity_primary} & {entity_secondary}")

print(f">> Trend Baseline ({entity_primary} Raw): {paimon_harmonics['raw_trend']}")
print(f">> Entry Signal ({entity_secondary} / 3): {astaroth_harmonics['harmonic_3']}")
print(f">> Scalp Signal ({entity_primary} / 9): {paimon_harmonics['harmonic_9']}")

# --- 4. EXPORT TO PINESCRIPT ---
print("\n--- PINESCRIPT PARAMETERS (Copy to TradingView) ---")
print(f"Trend Length: {paimon_harmonics['raw_trend']}")
print(f"Signal Length: {astaroth_harmonics['harmonic_3']}")
print(f"Volatility Factor: {paimon_harmonics['harmonic_9']}")
print("Matrix Seed: MILON")
