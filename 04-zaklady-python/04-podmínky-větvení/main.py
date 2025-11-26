# ==========================================
# 04 - PODMINKY A VETVENI
# Tema: Autentizace a Herni rozhodovani
# ==========================================

# 1. Simulator prihlaseni (if-else)
# ---------------------------------
print("--- SYSTEM PRIHLASENI ---")
spravne_heslo = "tajneheslo123"
zadane_heslo = input("Zadejte heslo: ")

if zadane_heslo == spravne_heslo:
    print("Pristup udelen. Vitejte v systemu.")
    je_prihlasen = True
else:
    print("Chybne heslo! Pristup odepren.")
    je_prihlasen = False

# Pokud neni prihlasen, ukoncime program (simulovane)
if not je_prihlasen:
    print("Konec programu.")
    exit() # Funkce exit() ukonci beh skriptu


# 2. Rozcestnik ve hre (if-elif-else)
# -----------------------------------
print("\n--- HERNI ROZCESTNIK ---")
print("Stojite na rozcesti v temnem lese.")
print("1. Jit vlevo (k rece)")
print("2. Jit vpravo (do jeskyne)")
print("3. Jit rovne (k hradu)")

volba = input("Kam se vydas? (napis 1, 2 nebo 3): ")

# Zde je dulezite pamatovat, ze input vraci string.
# Porovnavame tedy s "1", nikoliv s 1.
if volba == "1":
    print("Dosel jsi k rece. Voda je studena, ale pitna.")
elif volba == "2":
    print("Vstoupil jsi do jeskyne. Je tu tma a slysis vrceni...")
    # Vnorena podminka
    ma_pochoden = True
    if ma_pochoden:
        print("Jeste ze mas pochoden! Zapalil jsi ji a vidis medveda.")
    else:
        print("V te tme te neco sezralo. Konec hry.")
elif volba == "3":
    print("Cesta k hradu je zavrena. Musis se vratit.")
else:
    print("Neplatna volba. Zustal jsi stat na miste a setmelo se.")


# 3. Ternarni operator (Zkraceny zapis)
# -------------------------------------
print("\n--- HODNOCENI ZDRAVI ---")
zdravi = 25
# Chceme nastavit stav: "Kriticky" pokud je zdravi pod 30, jinak "V norme"
stav_hrace = "Kriticky" if zdravi < 30 else "V norme"

print(f"Zdravi: {zdravi} -> Stav: {stav_hrace}")


# 4. Match-Case (Python 3.10+)
# ----------------------------
# Prikaz pro zpracovani prikazu od uzivatele
print("\n--- OVLADANI ROBOTA ---")
prikaz = input("Zadej prikaz (w/a/s/d): ").lower() # .lower() prevede na mala pismena

match prikaz:
    case "w":
        print("Robot jede DOPREDU")
    case "s":
        print("Robot jede DOZADU")
    case "a":
        print("Robot zataci DOLEVA")
    case "d":
        print("Robot zataci DOPRAVA")
    case "q" | "exit": # Muzeme kombinovat vice moznosti pomoci |
        print("Vypinam robota...")
    case _: # _ znamena "cokoliv jineho" (default)
        print(f"Neznamy prikaz: {prikaz}")