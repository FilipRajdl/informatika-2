# ==========================================
# 02 - PROMENNE, TYPY A VSTUP UZIVATELE
# Tema: Jednoduchy registrator do RPG hry
# ==========================================

import datetime # Modul pro praci s casem (pouzijeme pro aktualni rok)

print("--- VITEJTE V REGISTRU HRDINU ---")
print("Prosim, vyplnte nasledujici udaje pro vytvoreni postavy.\n")

# 1. Ziskani vstupu (Input)
# -------------------------
# input() vzdy vraci retezec (str). U jmena je to v poradku.
prezdivka = input("Zadej prezdivku hrdiny: ")

# U veku chceme cislo, abychom mohli pocitat.
# Pouzijeme int(), ktery prevede textovy vstup na cele cislo.
vstup_vek = input("Zadej vek hrdiny: ")
vek = int(vstup_vek) 

# U vysky chceme desetinne cislo (napr. 1.85). Pouzijeme float().
vyska = float(input("Zadej vysku v metrech (napr. 1.80): "))

# Boolean (True/False) ziskame trochu oklikou.
# Zeptame se na "ano" a porovname vysledek.
je_clovek_vstup = input("Je hrdina clovek? (ano/ne): ")
je_clovek = (je_clovek_vstup == "ano") # Toto vyhodnoti True pokud uzivatel napsal "ano"

# Ukazka mene bezneho typu - Komplexni cislo
# V hernim svete muze reprezentovat treba souradnice v magickem poli
magicka_aura = 3 + 4j 

# 2. Vypocty s promennymi
# -----------------------
aktualni_rok = datetime.datetime.now().year
rok_narozeni = aktualni_rok - vek
vyska_v_cm = int(vyska * 100) # Prevedeme metry na cm a orezeme desetinna mista

# 3. Vypis profilu (f-strings)
# ----------------------------
print("\n" + "="*30)
print(f"PROFIL HRDINY: {prezdivka.upper()}") # .upper() zvetsi pismena
print("="*30)

print(f"Rasa:         {'Clovek' if je_clovek else 'Jina rasa'}")
print(f"Vek:          {vek} let (narozen cca {rok_narozeni})")
print(f"Vyska:        {vyska} m ({vyska_v_cm} cm)")
print(f"Magicka aura: {magicka_aura} (Typ: {type(magicka_aura)})")

# Ukazka typu v pozadi
print("\n[DEBUG INFO]")
print(f"Promenna 'vek' je typu: {type(vek)}")
print(f"Promenna 'vyska' je typu: {type(vyska)}")
print(f"Promenna 'je_clovek' je typu: {type(je_clovek)}")