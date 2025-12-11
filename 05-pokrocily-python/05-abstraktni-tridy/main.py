from abc import ABC, abstractmethod
import math

# 1. Definice abstraktního rodiče
class GeometrickyTvar(ABC):
    """
    Abstraktní třída. Nelze vytvořit její instanci.
    Slouží jako předpis, co musí každý útvar umět.
    """

    def __init__(self, nazev):
        self.nazev = nazev

    @abstractmethod
    def obsah(self):
        """Tuto metodu musí každý potomek přepsat!"""
        pass

    @abstractmethod
    def obvod(self):
        """Tuto metodu musí každý potomek přepsat!"""
        pass

    def popis(self):
        """Společná metoda pro všechny (není abstraktní)."""
        return f"Jsem útvar typu: {self.nazev}"


# 2. Konkrétní třídy
class Obdelnik(GeometrickyTvar):
    def __init__(self, strana_a, strana_b):
        super().__init__("Obdélník")
        self.a = strana_a
        self.b = strana_b

    def obsah(self):
        return self.a * self.b

    def obvod(self):
        return 2 * (self.a + self.b)


class Kruh(GeometrickyTvar):
    def __init__(self, polomer):
        super().__init__("Kruh")
        self.r = polomer

    def obsah(self):
        return math.pi * self.r ** 2

    def obvod(self):
        return 2 * math.pi * self.r


# 3. Ukázka Polymorfismu
def analyzuj_utvar(tvar):
    """
    Tato funkce demonstruje polymorfismus.
    Přijme jakýkoliv objekt typu GeometrickyUtvar a pracuje s ním stejně.
    """
    if not isinstance(tvar, GeometrickyTvar):
        print("Chyba: Toto není geometrický útvar!")
        return

    print(f"--- Analýza: {tvar.popis()} ---")
    print(f"Obsah: {tvar.obsah():.2f}")
    print(f"Obvod: {tvar.obvod():.2f}")
    print()


if __name__ == "__main__":
    # tvar = GeometrickyUtvar("Obecný") # TOTO BY VYHODILO CHYBU (TypeError)

    o = Obdelnik(10, 5)
    k = Kruh(7)

    # Polymorfismus v akci - dáváme různé objekty do stejné funkce
    analyzuj_utvar(o)
    analyzuj_utvar(k)

    # Polymorfismus v cyklu
    print("--- Hromadné zpracování ---")
    seznam_tvaru = [Obdelnik(2, 2), Kruh(1), Obdelnik(100, 20)]
    
    for u in seznam_tvaru:
        # Voláme .obsah() a neřešíme, jestli je to kruh nebo obdélník
        # O to se postará Python na pozadí.
        print(f"{u.nazev} má obsah {u.obsah():.2f}")