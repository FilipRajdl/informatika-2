"""
15 - Vložený kód: Srovnání výkonu Python vs C

Tento skript porovnává rychlost výpočtu k-tého prvočísla
v čistém Pythonu a v našem kompilovaném C modulu 'fastprime'.

POZOR: Před spuštěním musíte modul zkompilovat a nainstalovat!
V terminálu spusťte:
    python3 setup.py build_ext --inplace
"""

import time
import sys

# Zkusíme importovat náš C modul.
# Pokud neexistuje, vypíšeme návod.
try:
    import fastprime
except ImportError:
    print("CHYBA: Modul 'fastprime' nebyl nalezen.")
    print("Musíte ho nejprve zkompilovat příkazem:")
    print("  python3 setup.py build_ext --inplace")
    sys.exit(1)

# --- Implementace v čistém Pythonu ---
def is_prime_py(n):
    if n <= 1: return False
    # Optimalizace: jdeme jen do odmocniny (stejně jako v C)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def kth_prime_py(k):
    candidate = 2
    count = 0
    while count < k:
        if is_prime_py(candidate):
            count += 1
        if count < k:
            candidate += 1
    return candidate

# --- Hlavní program ---
def main():
    K = 10_000 # Kolikáté prvočíslo hledáme
    
    print(f"--- Srovnání výkonu (hledáme {K}. prvočíslo) ---")

    # 1. Měření Pythonu
    start_py = time.time()
    vysledek_py = kth_prime_py(K)
    end_py = time.time()
    cas_py = end_py - start_py
    
    print(f"Python:\t {vysledek_py} (čas: {cas_py:.4f} s)")

    # 2. Měření C modulu
    start_c = time.time()
    vysledek_c = fastprime.kth_prime(K)
    end_c = time.time()
    cas_c = end_c - start_c
    
    print(f"C Ext:\t {vysledek_c} (čas: {cas_c:.4f} s)")

    # 3. Vyhodnocení
    zrychleni = cas_py / cas_c if cas_c > 0 else 0
    print("-" * 40)
    print(f"C modul je přibližně {zrychleni:.1f}x rychlejší!")

if __name__ == "__main__":
    main()