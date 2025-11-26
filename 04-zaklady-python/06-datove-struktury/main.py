import os

def vycisti_konzoli():
    os.system('cls' if os.name == 'nt' else 'clear')

def ukazka_list():
    print("--- 1. SEZNAM (LIST) ---")
    # Seznam je měnitelný (mutable)
    auta = ["Škoda", "BMW", "Audi"]
    print(f"Původní: {auta}")
    
    # Přidání
    auta.append("Ford")
    print(f"Po append: {auta}")
    
    # Změna
    auta[1] = "Mercedes"
    print(f"Po změně indexu 1: {auta}")
    
    # Slicing (řezání) - [start:konec:krok]
    print(f"První dvě auta: {auta[0:2]}")
    print("-" * 30)
    
    # List comprehension
    print("\n--- List Comprehension ---")
    cisla = [1, 2, 3, 4, 5]
    # Vytvoříme seznam druhých mocnin na jeden řádek
    mocniny = [x * x for x in cisla]
    print(f"Původní: {cisla}")
    print(f"Mocniny: {mocniny}")
    
    # List comprehension s podmínkou (jen sudá čísla)
    suda = [x for x in cisla if x % 2 == 0]
    print(f"Jen sudá: {suda}")
    print("-" * 30)

def ukazka_tuple():
    print("--- 2. N-TICE (TUPLE) ---")
    # Tuple je neměnný (immutable)
    barvy = ("červená", "zelená", "modrá")
    print(f"Barvy: {barvy}")
    print(f"První barva: {barvy[0]}")
    
    try:
        barvy[0] = "žlutá"
    except TypeError as e:
        print(f"Chyba: {e}")
        print("-> Tuple nelze měnit!")
    print("-" * 30)

def ukazka_set():
    print("--- 3. MNOŽINA (SET) ---")
    # Set obsahuje pouze unikátní hodnoty
    vstup = [1, 2, 2, 3, 4, 4, 4, 5]
    mnozina = set(vstup)
    print(f"Původní seznam: {vstup}")
    print(f"Převedeno na set: {mnozina}")
    
    # Operace
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(f"Průnik (a & b): {a & b}")
    print(f"Sjednocení (a | b): {a | b}")
    print("-" * 30)

def ukazka_dict():
    print("--- 4. SLOVNÍK (DICTIONARY) ---")
    kniha = {
        "nazev": "1984",
        "autor": "George Orwell",
        "rok": 1949
    }
    
    # Výpis pomocí klíče
    print(f"Kniha: {kniha['nazev']}")
    
    # Iterace
    print("Všechny položky:")
    for klic, hodnota in kniha.items():
        print(f"  {klic}: {hodnota}")

if __name__ == "__main__":
    vycisti_konzoli()
    ukazka_list()
    ukazka_tuple()
    ukazka_set()
    ukazka_dict()