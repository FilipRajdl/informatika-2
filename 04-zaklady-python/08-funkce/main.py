import os

def vycisti_konzoli():
    """Vyčistí konzoli podle operačního systému."""
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. Jednoduchá funkce bez parametrů
def vypis_nadpis():
    print("-" * 30)
    print("      UKÁZKA FUNKCÍ")
    print("-" * 30)

# 2. Funkce s parametry
def pozdrav_uzivatele(jmeno, den_v_tydnu):
    print(f"Ahoj {jmeno}, přeji ti krásné {den_v_tydnu}!")

# 3. Funkce s návratovou hodnotou (return)
def vypocet_obvodu_obdelnika(a, b):
    obvod = 2 * (a + b)
    return obvod

# 4. Funkce s výchozím (defaultním) parametrem
def mocnina(zaklad, exponent=2):
    """Vrátí zaklad umocněný na exponent. Defaultně na druhou."""
    return zaklad ** exponent

# 5. Lambda funkce
# Lambda funkce pro výpočet obsahu čtverce
obsah_ctverce = lambda a: a * a

# Hlavní část programu
if __name__ == "__main__":
    vycisti_konzoli()
    vypis_nadpis()
    
    # Volání funkce s parametry
    pozdrav_uzivatele("Karle", "pondělí")
    
    # Volání funkce s return a uložení výsledku
    strana_a = 5
    strana_b = 10
    vysledek_obvod = vypocet_obvodu_obdelnika(strana_a, strana_b)
    print(f"Obvod obdélníka o stranách {strana_a} a {strana_b} je: {vysledek_obvod}")
    
    print("-" * 30)
    
    # Ukázka defaultních parametrů
    cislo = 4
    na_druhou = mocnina(cislo) # Použije se defaultní exponent 2
    na_treti = mocnina(cislo, 3) # Přepíšeme exponent na 3
    
    print(f"{cislo} na druhou je: {na_druhou}")
    print(f"{cislo} na třetí je: {na_treti}")
    
    # Ukázka použití lambda funkce
    print("-" * 30)
    print(f"Obsah čtverce (strana 6) pomocí lambdy: {obsah_ctverce(6)}")