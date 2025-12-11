"""
11 - Regulární výrazy (RegEx): Praktická ukázka

Tento skript demonstruje použití modulu 're' pro vyhledávání, 
validaci a nahrazování textu podle vzorů.
"""

import re

# ==========================================
# 1. Základní vyhledávání (Search vs Match)
# ==========================================
def zakladni_hledani():
    text = "Moje telefonní číslo je 123456789 a směrovací číslo je 602."
    
    # Hledáme vzor: 9 číslic za sebou (\d znamená digit/číslice, {9} počet opakování)
    vzor_telefon = r"\d{9}" 
    
    # re.search hledá kdekoliv v textu (vrátí první výskyt)
    nalezeno = re.search(vzor_telefon, text)
    
    print("--- 1. Vyhledávání ---")
    if nalezeno:
        print(f"Nalezeno číslo: {nalezeno.group()} (na indexu {nalezeno.start()}-{nalezeno.end()})")
    else:
        print("Telefonní číslo nenalezeno.")

    # re.match hledá POUZE na začátku řetězce
    match_na_zacatku = re.match(vzor_telefon, text)
    print(f"Je číslo na začátku textu? {'ANO' if match_na_zacatku else 'NE'}")
    print()


# ==========================================
# 2. Hromadné hledání (Findall)
# ==========================================
def extrakce_dat():
    log_soubor = """
    ERROR [2023-10-01 14:00]: Spojení ztraceno
    INFO [2023-10-01 14:05]: Uživatel přihlášen
    WARNING [2023-10-01 14:10]: Disk je téměř plný
    """
    
    # Hledáme vzor data v hranatých závorkách: [rok-mesic-den cas]
    # \[ a \] jsou escapované závorky (protože [] mají v regexu speciální význam)
    # (.*?) je tzv. capture group - to co nás zajímá uvnitř
    vzor_datum = r"\[(.*?)\]"
    
    print("--- 2. Extrakce dat (findall) ---")
    vsechna_data = re.findall(vzor_datum, log_soubor)
    print(f"Nalezené časové známky: {vsechna_data}")
    print()


# ==========================================
# 3. Validace (E-mail)
# ==========================================
def validace_emailu(email):
    # Komplexní regex pro email (zjednodušený, ale funkční pro většinu)
    # ^ = začátek řetězce
    # [\w\.-]+ = písmena, čísla, tečky nebo pomlčky (uživatel)
    # @ = zavináč
    # [\w\.-]+ = doména
    # \. = tečka před koncovkou
    # [a-zA-Z]{2,} = koncovka (alespoň 2 písmena)
    # $ = konec řetězce
    vzor = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    
    je_validni = re.match(vzor, email) is not None
    print(f"Validace e-mailu '{email}': {'OK' if je_validni else 'CHYBA'}")


# ==========================================
# 4. Nahrazování (Sub)
# ==========================================
def cenzura_textu():
    zprava = "Ten chlap je blbec a idiot!"
    
    # Hledáme hrubá slova oddělená svislítkem (NEBO)
    # re.IGNORECASE zajistí, že to najde i "Blbec" nebo "IDIOT"
    hruby_vzor = r"blbec|idiot|hlupák"
    
    # Nahradíme hvězdičkami
    cenzurovano = re.sub(sprosty_vzor, "***", zprava, flags=re.IGNORECASE)
    
    print("\n--- 4. Nahrazování (Cenzura) ---")
    print(f"Původní: {zprava}")
    print(f"Po cenzuře: {cenzurovano}")


# --- Hlavní program ---
if __name__ == "__main__":
    zakladni_hledani()
    extrakce_dat()
    
    print("--- 3. Validace ---")
    validace_emailu("jan.novak@firma.cz")
    validace_emailu("spatny-email.com") # Chybí zavináč
    validace_emailu("dalsi@chyba")      # Chybí koncovka
    
    cenzura_textu()