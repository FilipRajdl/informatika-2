from typing import Any, List, Dict, Optional # Pro starší verze Pythonu, dnes už méně třeba

class Produkt:
    def __init__(self, nazev: str, cena: float) -> None:
        self.nazev = nazev
        self.cena = cena

    def __str__(self) -> str:
        return f"{self.nazev} ({self.cena} Kč)"


class Objednavka:
    def __init__(self, id_objednavky: int) -> None:
        self.id = id_objednavky
        # Seznam, který obsahuje pouze instance třídy Produkt
        self.polozky: list[Produkt] = []
        # Stav může být text nebo None, pokud zatím nevíme
        self.stav: str | None = None

    def pridej_polozku(self, produkt: Produkt) -> None:
        self.polozky.append(produkt)
        print(f"Přidáno: {produkt.nazev}")

    def celkova_cena(self) -> float:
        suma: float = 0.0
        for p in self.polozky:
            suma += p.cena
        return suma

    def aplikuj_slevu(self, sleva: int | float) -> float:
        """
        Sleva může být zadána jako celé číslo nebo desetinné číslo.
        """
        cena = self.celkova_cena()
        nova_cena = cena - sleva
        return nova_cena if nova_cena > 0 else 0.0


def zpracuj_data(data: Any) -> None:
    """
    Funkce, která přijme cokoliv (Any).
    Zde ztrácíme výhody typové kontroly.
    """
    print(f"Zpracovávám data typu: {type(data)}")


# --- Hlavní část ---
if __name__ == "__main__":
    # Díky typování nám editor napovídá metody třídy Produkt i Objednavka
    p1: Produkt = Produkt("Notebook", 25000.0)
    p2: Produkt = Produkt("Myš", 500) # Int se automaticky bere jako kompatibilní s float

    obj: Objednavka = Objednavka(101)
    obj.pridej_polozku(p1)
    obj.pridej_polozku(p2)

    cena_celkem: float = obj.celkova_cena()
    print(f"Celkem: {cena_celkem} Kč")

    # Ukázka Union typu (int nebo float)
    print(f"Po slevě 100 Kč: {obj.aplikuj_slevu(100)}")
    print(f"Po slevě 200.50 Kč: {obj.aplikuj_slevu(200.50)}")

    # Ukázka chyby, kterou by odhalil mypy (statická analýza), 
    # ale Python ji spustí a spadne až při běhu nebo udělá nesmysl:
    # obj.pridej_polozku("Toto není produkt") 
    
    zpracuj_data(123)
    zpracuj_data("Test")