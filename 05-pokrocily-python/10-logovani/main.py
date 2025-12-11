"""
10 - Logování: Praktická ukázka

Tento skript ukazuje, jak nahradit print() profesionálním logováním.
Logování nám umožní zpětně zjistit, co se v programu dělo, i když u toho nesedíme.
"""

import logging

# 1. Základní nastavení (Konfigurace)
# Nastavíme, že chceme logovat vše od úrovně DEBUG výše
# a výstup chceme ukládat do souboru 'aplikace.log'
logging.basicConfig(
    level=logging.DEBUG,  # Minimální úroveň, která se zaznamená
    filename='aplikace.log', # Cíl logů (pokud vynecháte, jde to do konzole)
    filemode='w',         # 'w' přepíše soubor při každém startu, 'a' připojí na konec
    format='%(asctime)s - %(levelname)s - %(message)s', # Formát zprávy
    encoding='utf-8'
)

# Vytvoření loggeru (pokud chceme logovat do více míst, používáme pojmenované loggery)
# Pro jednoduchost zde používáme ten základní (root logger) nastavený výše.

def bezpecne_deleni(a, b):
    # Logujeme vstupní data (užitečné pro debugging)
    logging.debug(f"Volána funkce bezpecne_deleni s argumenty: a={a}, b={b}")
    
    try:
        vysledek = a / b
        logging.info(f"Dělení proběhlo úspěšně. Výsledek: {vysledek}")
        return vysledek
    
    except ZeroDivisionError:
        # Zaznamenáme chybu (ERROR), ale program nespadne
        logging.error("Pokus o dělení nulou!", exc_info=True) # exc_info přidá traceback
        return None
    
    except TypeError as e:
        logging.critical(f"Kritická chyba typu: {e}")
        return None

def zpracuj_seznam(data):
    logging.info(f"Začínám zpracovávat seznam o délce {len(data)}")
    
    for polozka in data:
        if not isinstance(polozka, (int, float)):
            logging.warning(f"Přeskakuji neplatnou položku: '{polozka}' (není číslo)")
            continue
            
        logging.debug(f"Počítám s položkou: {polozka}")
        bezpecne_deleni(100, polozka)
        
    logging.info("Zpracování seznamu dokončeno.")


# --- Hlavní program ---
if __name__ == "__main__":
    print("--- Spouštím aplikaci (výstup hledejte v 'aplikace.log') ---")
    
    testovaci_data = [10, 5, 0, "text", 20]
    
    zpracuj_seznam(testovaci_data)
    
    print("--- Hotovo. Podívejte se do souboru 'aplikace.log'. ---")