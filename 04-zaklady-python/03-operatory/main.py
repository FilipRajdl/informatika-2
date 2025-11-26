# ==========================================
# 03 - OPERATORY
# Tema: Jednoduche herni mechaniky a vypocty
# ==========================================

# 1. Aritmeticke operatory v praxi
# --------------------------------
max_zdravi = 100
aktualni_zdravi = 45
lecivy_lektvar = 30

print("--- ARITMETIKA: LECENI ---")
print(f"Aktualni zdravi: {aktualni_zdravi}/{max_zdravi}")
# Pouziti operatoru + a prirazovaciho operatoru +=
# (Simulace vypiti lektvaru)
aktualni_zdravi += lecivy_lektvar 
print(f"Po vypiti lektvaru (+{lecivy_lektvar}): {aktualni_zdravi}/{max_zdravi}")

# 2. Deleni a Modulo (Zbytek po deleni)
# -------------------------------------
pocet_zlataku = 125
cena_sipu = 10

# Kolik sipu si mohu koupit? (Celociselne deleni)
pocet_koupenych_sipu = pocet_zlataku // cena_sipu

# Kolik penez mi zbyde? (Modulo)
zbytek_penez = pocet_zlataku % cena_sipu

print("\n--- OBCHOD: NAKUP SIPU ---")
print(f"Mam {pocet_zlataku} zlataku. Jeden sip stoji {cena_sipu}.")
print(f"Mohu si koupit {pocet_koupenych_sipu} sipu.")
print(f"V penezence mi zbyde {zbytek_penez} zlataku.")

# 3. Porovnavaci a Logicke operatory
# ----------------------------------
level_hrace = 5
ma_klic_k_brane = False
ma_magickou_moc = True

# Podminka pro vstup do dungeonu:
# Hrac musi mit level alespon 5 A ZAROVEN musi mit klic NEBO magickou moc.
muze_vstoupit = (level_hrace >= 5) and (ma_klic_k_brane or ma_magickou_moc)

print("\n--- LOGIKA: VSTUP DO DUNGEONU ---")
print(f"Level >= 5: {level_hrace >= 5}")
print(f"Ma klic nebo magii: {ma_klic_k_brane or ma_magickou_moc}")
print(f"Vysledek (muze vstoupit): {muze_vstoupit}")

# 4. Operatory s retezci
# ----------------------
jmeno = "Barbar"
titul = "Hrozny"

# Spojovani retezcu
cele_jmeno = jmeno + " " + titul 

# Nasobeni retezcu (napr. pro oddelovac)
oddelovac = "-" * 30 

print(f"\n{oddelovac}")
print(f"Hrdina: {cele_jmeno}")
print(oddelovac)

# 5. Clenske operatory (in)
# -------------------------
zakazane_znaky = "@#$%"
vstup_uzivatele = "Heslo123"

# Testujeme, zda se znak zavinac nachazi ve vstupu
obsahuje_zakazany_znak = "@" in vstup_uzivatele

print("\n--- KONTROLA VSTUPU ---")
print(f"Obsahuje '{vstup_uzivatele}' znak '@'? {obsahuje_zakazany_znak}")