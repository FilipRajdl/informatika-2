# ==========================================
# 05 - CYKLY
# Tema: Automatizace, Hry a Vnorene smycky
# ==========================================

import time # Modul pro praci s casem (pouzivejme sleep pro zpozdovani vypisu)

# 1. Cyklus FOR a funkce RANGE
# -----------------------------
print("--- START SYSTEMU ---")
# Odpocitavani: range(start, stop, krok)
# Stop hodnota (0) se jiz nevypise, proto skonci u 1.
for i in range(3, 0, -1):
    print(f"Start za {i}...")
    # time.sleep(1) # Pocka 1 sekundu (zakomentovano pro rychlejsi beh)
print("START!\n")


# 2. Iterace pres retezec
# -----------------------
zprava = "Python"
print(f"Analyza zpravy: {zprava}")

for znak in zprava:
    # Vypise ciselny kod znaku (ASCII/Unicode hodnota)
    kod = ord(znak) 
    print(f"Znak '{znak}' ma kod {kod}")


# 3. Cyklus WHILE a BREAK (Hra hadani cisla)
# ------------------------------------------
print("\n--- HADACI HRA (While Loop) ---")
tajne_cislo = 7
pokusy = 0

while True: # Nekonecny cyklus, musime ho ukoncit breakem
    vstup = input("Hadej cislo (nebo 'q' pro konec): ")
    
    if vstup == 'q':
        print("Hra ukoncena hracem.")
        break # Vyskoci z cyklu ven
    
    cislo = int(vstup)
    pokusy += 1
    
    if cislo == tajne_cislo:
        print(f"Vyborne! Uhadl jsi cislo {tajne_cislo} na {pokusy}. pokus.")
        break # Vyskoci z cyklu ven po vyhre
    else:
        print("Spatne, zkus to znovu.")

print("Konec hadaci hry.\n")


# 4. CONTINUE - Preskoceni iterace
# --------------------------------
print("--- VYPIS LICHYCH CISEL (0-10) ---")
for i in range(11):
    # Pokud je cislo sude (zbytek po deleni 2 je 0), preskocime ho
    if i % 2 == 0:
        continue 
    
    # Tento kod se provede jen pro licha cisla
    print(i, end=" ")
print("\n")


# 5. VNORENE CYKLY (Nested Loops) - Vykresleni ctverce
# ----------------------------------------------------
print("--- VYKRESLENI CTVERCE ---")
velikost = 4

for radek in range(velikost):
    for sloupec in range(velikost):
        # Vypise hvezdicku a zustane na radku
        print("*", end="  ") 
    # Po vypsani jednoho radku (vnitrni cyklus) odradkujeme
    print() 


# 6. ELSE u cyklu (Hledani)
# -------------------------
print("\n--- HLEDANI CISEL ---")
hledane = 42
rozsah = range(0, 10, 2) # 0, 2, 4, 6, 8

for cislo in rozsah:
    if cislo == hledane:
        print("Cislo nalezeno!")
        break
else:
    # Provede se, pokud cyklus dobehl a NENARAZIL na break
    print(f"Cislo {hledane} nebylo v prohledavanem rozsahu nalezeno.")