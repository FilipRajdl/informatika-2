"""
Toto je náš vlastní modul.
Můžeme sem odložit funkce, třídy a konstanty, které chceme používat jinde.
"""

# 1. Konstanta
PI = 3.14159

# 2. Funkce
def mocnina(zaklad, exponent):
    """Vrátí číslo umocněné na exponent."""
    return zaklad ** exponent

def faktorial(n):
    """Vypočítá faktoriál čísla n (rekurzivně)."""
    if n <= 1:
        return 1
    return n * faktorial(n - 1)

# 3. Třída
class Kalkulacka:
    """Jednoduchá třída uvnitř modulu."""
    def secti(self, a, b):
        return a + b
    
    def odecti(self, a, b):
        return a - b

# 4. Ochrana proti spuštění při importu
# Tento blok se provede JEN tehdy, když tento soubor spustíte přímo (ne jako import).
if __name__ == "__main__":
    print("--- Testování modulu matematika.py ---")
    print(f"PI je: {PI}")
    print(f"2^3 je: {mocnina(2, 3)}")
    # Pokud tento soubor importujete do main.py, tento text se nevypíše.