"""
08 - Dekorátory: Praktická ukázka

Dekorátory jsou funkce, které zabalí jinou funkci a tím jsou schopné ovlivnit
její vstup nebo výstup, nebo jestli bude vůbec zavolána,
aniž bychom přímo modifikovali samotnou funkci.
"""

import functools

# ==========================================
# 1. Funkce jako objekty (Opakování)
# ==========================================

def zvys_o_jedna(cislo):
    return cislo + 1

def vrat_funkci():
    """Funkce, která vrací jinou funkci."""
    return zvys_o_jedna

def ukazka_funkce_jako_objekt():
    print("--- 1. Funkce jako objekty ---")
    print(f"Výsledek volání zvys_o_jedna(1): {zvys_o_jedna(1)}")

    # V jazyku Python je možné funkce předávat, jako by se jednalo o proměnnou.
    moje_funkce = vrat_funkci()
    print(f"Vrácená funkce: {moje_funkce}")
    
    # Volání funkce uložené v proměnné
    vysledek = moje_funkce(5)
    print(f"Volání funkce z proměnné s parametrem 5: {vysledek}")
    print()


# ==========================================
# 2. Vnořené funkce (Nested functions)
# ==========================================

def rodic():
    print("-> Tisk z mateřské funkce")

    def prvni_potomek():
        print("  -> Tisk z prvního potomka")

    def druhy_potomek():
        print("  -> Tisk z druhého potomka")

    # Funkce jsou viditelné pouze uvnitř 'rodic'
    druhy_potomek()
    prvni_potomek()

def ukazka_vnorene_funkce():
    print("--- 2. Vnořené funkce ---")
    rodic()
    print()


# ==========================================
# 3. Princip dekorátoru (Ruční obalení)
# ==========================================

# Dekorátor přijímá funkci (func) a vrací novou funkci (wrapper)
def jednoduchy_dekorator(func):
    
    def wrapper():
        print("LOG: Před voláním funkce")
        func()
        func() # Zavoláme ji dvakrát pro efekt
        print("LOG: Po volání funkce")
    
    return wrapper

def rekni_ahoj():
    print("Ahoj!")

def ukazka_rucni_dekorator():
    print("--- 3. Ruční dekorování ---")
    # Zde předáváme funkci jako parametr
    ozdobene_ahoj = jednoduchy_dekorator(rekni_ahoj)
    
    print("Volám dekorovanou funkci:")
    ozdobene_ahoj()
    print()


# ==========================================
# 4. Syntaxe se zavináčem @
# ==========================================

@jednoduchy_dekorator
def rekni_nashle():
    print("Nashle")

def ukazka_zavinac():
    print("--- 4. Použití @dekorator ---")
    rekni_nashle()
    
    # Problém jednoduchého dekorátoru: Ztráta identity
    print(f"\nNázev funkce 'rekni_nashle' je nyní: {rekni_nashle.__name__}")
    # Vidíme 'wrapper', což je špatně pro debugging.
    print()


# ==========================================
# 5. Pokročilý dekorátor (s argumenty a fixem metadat)
# ==========================================

def loguj_argumenty(func):
    # functools.wraps zajistí, že si funkce zachová své jméno a dokumentaci
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"LOG: Volám funkci '{func.__name__}' s argumenty: {args} {kwargs}")
        # Předání argumentů dál
        vysledek = func(*args, **kwargs)
        return vysledek
    return wrapper

@loguj_argumenty
def scitani(a, b, zprava="Součet"):
    print(f"{zprava} je {a + b}")
    return a + b

def ukazka_pokrocila():
    print("--- 5. Pokročilý dekorátor (*args, **kwargs) ---")
    scitani(10, 20, zprava="Výsledek")
    
    # Díky @functools.wraps je jméno správně
    print(f"\nNázev funkce je nyní správně: {scitani.__name__}")


# ==========================================
# Hlavní spouštěcí blok
# ==========================================
if __name__ == "__main__":
    ukazka_funkce_jako_objekt()
    ukazka_vnorene_funkce()
    ukazka_rucni_dekorator()
    ukazka_zavinac()
    ukazka_pokrocila()