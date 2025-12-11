"""
11 - Argumenty příkazové řádky: Ukázka s argparse

Tento skript nelze efektivně testovat tlačítkem "Play" v editoru,
protože očekává argumenty. Musíte ho spustit z terminálu!

Příklady použití:
1. python main.py 5 10
2. python main.py 5 10 --operace nasobeni
3. python main.py 5 10 -v
4. python main.py -h  (zobrazí nápovědu)
"""

import argparse
import sys

def main():
    # 1. Vytvoření parseru
    parser = argparse.ArgumentParser(
        description="Mocná matematická kalkulačka pro příkazovou řádku."
    )

    # 2. Definice argumentů
    # Poziční argumenty (povinné, pořadí je důležité)
    parser.add_argument("x", type=int, help="První číslo")
    parser.add_argument("y", type=int, help="Druhé číslo")

    # Volitelné argumenty (začínají -- nebo -)
    parser.add_argument(
        "--operace", "-op", 
        type=str, 
        choices=["soucet", "rozdil", "nasobeni", "deleni"],
        default="soucet",
        help="Jakou operaci provést (výchozí: soucet)"
    )

    # Přepínač (flag) - pokud je uveden, uloží se True, jinak False
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Vypíše detailní (ukecaný) výstup"
    )

    # 3. Zpracování argumentů (Parsing)
    # Pokud uživatel zadal nesmysly, program se zde ukončí a vypíše chybu
    args = parser.parse_args()

    # --- Vlastní logika programu ---
    
    if args.verbose:
        print(f"[LOG] Zpracovávám čísla: {args.x} a {args.y}")
        print(f"[LOG] Zvolená operace: {args.operace}")

    vysledek = None

    if args.operace == "soucet":
        vysledek = args.x + args.y
    elif args.operace == "rozdil":
        vysledek = args.x - args.y
    elif args.operace == "nasobeni":
        vysledek = args.x * args.y
    elif args.operace == "deleni":
        if args.y == 0:
            print("Chyba: Nelze dělit nulou!", file=sys.stderr)
            sys.exit(1) # Ukončení s chybovým kódem
        vysledek = args.x / args.y

    # Výpis výsledku
    if args.verbose:
        print(f"--> Výsledek je: {vysledek}")
    else:
        print(vysledek)


if __name__ == "__main__":
    main()