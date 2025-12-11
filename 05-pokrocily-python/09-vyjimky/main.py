"""
09 - Výjimky: Praktická ukázka

Tento skript demonstruje správné ošetřování chybových stavů.
Ukazuje rozdíl mezi pádem programu a zachycenou výjimkou.
"""

# 1. Definice vlastní výjimky
class NeplatnyVekError(Exception):
    """Vlastní výjimka pro případ, že věk nedává smysl."""
    pass


# 2. Funkce, která může selhat (vyvolá výjimku)
def over_vek(vek):
    if vek < 0:
        # Vyvoláváme vlastní chybu
        raise NeplatnyVekError(f"Věk nemůže být záporný: {vek}")
    if vek < 18:
        # Vyvoláváme vestavěnou chybu
        raise ValueError("Uživatel musí být plnoletý.")
    return True


def bezpecne_deleni(a, b):
    try:
        vysledek = a / b
    except ZeroDivisionError:
        print("CHYBA: Dělení nulou není povoleno.")
        return None
    except TypeError as e:
        print(f"CHYBA: Špatný datový typ. Detaily: {e}")
        return None
    else:
        # Provede se pouze, pokud NENASTALA chyba
        print("Dělení proběhlo v pořádku.")
        return vysledek
    finally:
        # Provede se VŽDY (ať už chyba nastala nebo ne)
        # Slouží k úklidu (zavření souboru, odpojení DB)
        print("--- Konec operace dělení ---")


def prace_se_souborem(nazev_souboru):
    try:
        # Zkusíme otevřít soubor (může selhat, pokud neexistuje)
        file = open(nazev_souboru, "r", encoding="utf-8")
        obsah = file.read()
        print(f"Přečteno {len(obsah)} znaků.")
        # file.close() # Kdyby nastala chyba při čtení, tento řádek se neprovede!
    except FileNotFoundError:
        print(f"CHYBA: Soubor '{nazev_souboru}' neexistuje.")
    except PermissionError:
        print(f"CHYBA: Nemáte práva číst soubor '{nazev_souboru}'.")
    finally:
        # Zde bychom správně měli soubor zavřít, pokud byl otevřen.
        # V Pythonu se k tomuto ale lépe používá blok 'with'.
        print("Pokus o čtení souboru ukončen.")


# --- Hlavní program ---
if __name__ == "__main__":
    
    print("=== 1. Ošetření dělení ===")
    print(f"Výsledek: {bezpecne_deleni(10, 2)}\n")
    print(f"Výsledek: {bezpecne_deleni(10, 0)}\n")
    print(f"Výsledek: {bezpecne_deleni(10, 'pět')}\n")

    print("=== 2. Vlastní výjimky ===")
    vstupy = [20, 15, -5, "text"]
    
    for v in vstupy:
        print(f"Ověřuji věk: {v}")
        try:
            # Musíme ošetřit i vstup, který není číslo
            if not isinstance(v, (int, float)):
                raise TypeError("Věk musí být číslo.")
            
            over_vek(v)
            print(" -> Vstup povolen.")
            
        except NeplatnyVekError as e:
            print(f" -> ZACHYCENO (Vlastní): {e}")
        except ValueError as e:
            print(f" -> ZACHYCENO (Hodnota): {e}")
        except TypeError as e:
            print(f" -> ZACHYCENO (Typ): {e}")
        except Exception as e:
            # Záchranná síť pro nečekané chyby (používat opatrně!)
            print(f" -> NEČEKANÁ CHYBA: {type(e).__name__}: {e}")
        
        print("-" * 20)