# ==========================================
# 01 - SYNTAXE, VÝSTUP A KOMENTÁŘE
# ==========================================

# 1. Jednoduchý výpis
# -------------------
print("Vítejte v systému.")  # Funkce print automaticky udělá nový řádek
print("Načítání konfigurace...")

# 2. Práce s parametry 'sep' a 'end'
# ----------------------------------
# Chceme vypsat odpočet na jednom řádku: 3.. 2.. 1.. START
print("Start za:", end=" ")
print(3, end=".. ")
print(2, end=".. ")
print(1, end=".. ")
print("TEĎ!")

# Parametr 'sep' nám dovolí formátovat výpis více hodnot najednou
print("Datum", "12", "10", "2025", sep=".")  # Vypíše: Datum.12.10.2025
print("Cesta k souboru", "C:", "Users", "Data", sep="\\") # Vypíše s lomítky

# 3. Formátování pomocí f-strings (To nejdůležitější!)
# ----------------------------------------------------
hrac = "Zaklínač"
zdravi = 100
max_zdravi = 150
lokace = "Novigrad"

# F-string umožňuje vložit proměnné přímo do textu pomocí {}
# Můžeme uvnitř {} provádět i jednoduché výpočty
print(f"\n--- STAV HRÁČE: {hrac} ---")
print(f"Lokace:\t\t{lokace}")  # \t je tabulátor pro zarovnání
print(f"Zdraví:\t\t{zdravi}/{max_zdravi} ({(zdravi/max_zdravi)*100:.1f}%)") 
# Všimněte si .1f -> zaokrouhlení na 1 desetinné místo přímo ve výpisu

# 4. Odsazování (Indentation) - Ukázka bloku
# ------------------------------------------
# V Pythonu definuje strukturu kódu odsazení. 
# Pokud je podmínka pravdivá, provede se odsazený blok.

system_ok = True

if system_ok:
    # Tady začíná odsazený blok (4 mezery)
    print("\n[SYSTÉM] Kontrola proběhla úspěšně.")
    print("[SYSTÉM] Všechny moduly načteny.")
    # Konec bloku

print("Toto se vypíše vždy, protože to není odsazené.")

# 5. Víceřádkový text
# -------------------
print("""
Důležité varování:
    1. Nezomínejte na zálohy.
    2. Pijte dostatek vody.
    3. Nepoužívejte tabulátory a mezery zároveň.
""")