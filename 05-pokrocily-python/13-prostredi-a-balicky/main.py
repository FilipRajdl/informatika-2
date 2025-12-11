"""
12 - Virtuální prostředí: Praktická ukázka

Tento skript dělá dvě věci:
1. Kontroluje, zda běží ve virtuálním prostředí.
2. Zkouší importovat externí knihovnu 'colorama'.

Pokud knihovna chybí, skript spadne (což je chtěné, abychom viděli chybu).
"""

import sys
import os

def check_venv():
    """Zjistí, zda běžíme ve virtuálním prostředí."""
    # sys.prefix je cesta k aktuálnímu Pythonu
    # sys.base_prefix je cesta k původnímu (systémovému) Pythonu
    # Ve venvu se tyto dvě cesty liší.
    je_venv = sys.prefix != sys.base_prefix
    
    print(f"Python spustitelný soubor: {sys.executable}")
    print(f"Běží ve virtuálním prostředí? {'ANO' if je_venv else 'NE (Doporučeno používat venv!)'}")
    print("-" * 40)

def barevny_vypis():
    """Zkusí použít externí knihovnu."""
    try:
        import colorama
        from colorama import Fore, Style
        
        # Inicializace pro Windows (pro Linux/Mac není nutná, ale nevadí)
        colorama.init()
        
        print(Fore.GREEN + "ÚSPĚCH: Knihovna 'colorama' je nainstalována!" + Style.RESET_ALL)
        print(Fore.CYAN + "Tento text je azurový." + Style.RESET_ALL)
        print(Fore.RED + "Tento text je červený." + Style.RESET_ALL)
        
    except ImportError:
        print("CHYBA: Knihovna 'colorama' nebyla nalezena.")
        print("Řešení:")
        print("1. Vytvořte venv: python -m venv .venv")
        print("2. Aktivujte ho (Windows: .venv\\Scripts\\activate, Linux/Mac: source .venv/bin/activate)")
        print("3. Nainstalujte závislosti: pip install -r requirements.txt")

if __name__ == "__main__":
    print("--- Diagnostika prostředí ---")
    check_venv()
    barevny_vypis()