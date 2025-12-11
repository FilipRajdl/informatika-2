# 1. Import klasického modulu (leží ve stejné složce)
# Importování celého modulu
import matematika

# Importování konkrétních částí (abychom nemuseli psát matematika.PI)
from matematika import Kalkulacka, mocnina

# Importování s aliasem (přejmenování)
import matematika as mat

# 2. Import z balíčku (leží ve složce muj_balicek)
# Z balíčku 'muj_balicek' importujeme modul 'geometrie'
import muj_balicek.geometrie as geo

# Můžeme importovat i proměnné z __init__.py
from muj_balicek import VERZE

def main():
    print(f"\n--- Spuštěna aplikace (verze balíčku: {VERZE}) ---")
    
    # A) Použití klasického modulu
    print("--- 1. Použití celého modulu (matematika.neco) ---")
    # Musíme použít název modulu jako předponu (namespace)
    print(f"Hodnota PI z modulu: {matematika.PI}")
    print(f"Faktoriál 5: {matematika.faktorial(5)}")

    print("\n--- 2. Použití konkrétních importů (bez předpony) ---")
    # Tady už píšeme rovnou funkci, protože jsme ji importovali 'from ...'
    vysledek = mocnina(2, 10)
    print(f"2 na 10 je: {vysledek}")

    print("\n--- 3. Použití třídy z modulu ---")
    kalk = Kalkulacka() # Třída importovaná v sekci 'from'
    soucet = kalk.secti(10, 20)
    print(f"Součet 10 + 20 = {soucet}")

    print("\n--- 4. Použití aliasu ---")
    # Používáme zkratku 'mat', kterou jsme definovali nahoře
    print(f"Opět PI, ale přes alias: {mat.PI}")
    
    # B) Použití balíčku
    a = 4
    b = 6
    plocha = geo.obsah_obdelniku(a, b)
    print(f"Geometrie (balíček): Obdélník {a}x{b} má obsah {plocha}")
    
    # C) Kombinace
    r = 3
    # Funkce obsah_kruhu uvnitř balíčku využívá modul matematika
    kruh = geo.obsah_kruhu(r)
    print(f"Geometrie (balíček): Kruh s poloměrem {r} má obsah {kruh:.2f}")


# Toto je standardní vstupní bod programu
if __name__ == "__main__":
    main()