import os

# Název souboru, se kterým budeme pracovat
SOUBOR = "denik.txt"

def zapis_do_souboru():
    print("--- ZÁPIS DO SOUBORU (mód 'w') ---")
    # 'w' vytvoří soubor, pokud neexistuje. Pokud existuje, smaže ho!
    with open(SOUBOR, mode="w", encoding="utf-8") as f:
        f.write("Toto je první řádek mého deníku.\n")
        f.write("Dnes se učím pracovat se soubory v Pythonu.\n")
    print("Data byla zapsána.")

def pridani_do_souboru():
    print("\n--- PŘIDÁNÍ DO SOUBORU (mód 'a') ---")
    # 'a' (append) přidá data na konec souboru
    with open(SOUBOR, mode="a", encoding="utf-8") as f:
        f.write("Tento řádek byl přidán později pomocí módu 'append'.\n")
    print("Data byla přidána.")

def cteni_souboru():
    print(f"\n--- ČTENÍ SOUBORU '{SOUBOR}' (mód 'r') ---")
    try:
        with open(SOUBOR, mode="r", encoding="utf-8") as f:
            # Čteme soubor řádek po řádku (paměťově efektivní)
            for i, radek in enumerate(f):
                # radek obsahuje i znak \n (enter), proto použijeme strip()
                print(f"Řádek {i+1}: {radek.strip()}")
                
    except FileNotFoundError:
        print(f"Chyba: Soubor '{SOUBOR}' nebyl nalezen. Nejdříve ho vytvořte zápisem.")

def main():
    # Pokud soubor existuje, smažeme ho, abychom začali s čistým štítem
    if os.path.exists(SOUBOR):
        os.remove(SOUBOR)
        
    zapis_do_souboru()
    cteni_souboru()
    
    pridani_do_souboru()
    cteni_souboru()

if __name__ == "__main__":
    main()