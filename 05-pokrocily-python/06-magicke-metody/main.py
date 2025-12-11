class Vektor:
    """
    Třída reprezentující 2D vektor.
    Demonstruje použití magických metod pro matematické operace.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 1. Reprezentace objektu
    def __str__(self):
        """Vrátí hezký řetězec pro print()."""
        return f"Vektor({self.x}, {self.y})"

    def __repr__(self):
        """Vrátí řetězec pro ladění (vývojáře)."""
        return f"Vektor(x={self.x}, y={self.y})"

    # 2. Matematické operace
    def __add__(self, other):
        """Implementuje operátor +"""
        # Musíme zkontrolovat, zda přičítáme taky Vektor
        if isinstance(other, Vektor):
            return Vektor(self.x + other.x, self.y + other.y)
        # Nebo jestli přičítáme jen číslo (posun)
        elif isinstance(other, (int, float)):
            return Vektor(self.x + other, self.y + other)
        return NotImplemented

    def __sub__(self, other):
        """Implementuje operátor -"""
        if isinstance(other, Vektor):
            return Vektor(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __eq__(self, other):
        """Implementuje operátor =="""
        if isinstance(other, Vektor):
            return self.x == other.x and self.y == other.y
        return False
    
    # 3. Další metody
    def __len__(self):
        """Implementuje funkci len(). Zde jako velikost vektoru (zaokrouhleno)."""
        return int((self.x**2 + self.y**2) ** 0.5)


class Batoh:
    """
    Třída reprezentující batoh s věcmi.
    Demonstruje __len__ a __getitem__.
    """
    def __init__(self):
        self.veci = []

    def pridej(self, vec):
        self.veci.append(vec)

    def __str__(self):
        return f"Batoh obsahuje: {', '.join(self.veci)}"

    def __len__(self):
        """Volá se při len(batoh)"""
        return len(self.veci)

    def __getitem__(self, index):
        """Umožňuje indexování: batoh[0]"""
        return self.veci[index]


if __name__ == "__main__":
    print("--- Práce s Vektory ---")
    v1 = Vektor(2, 3)
    v2 = Vektor(1, 4)

    print(f"v1: {v1}")      # Volá __str__
    print(f"v2: {repr(v2)}") # Volá __repr__

    v3 = v1 + v2           # Volá __add__
    print(f"Sčítání (v1 + v2): {v3}")

    v4 = v1 + 10           # Volá __add__ s číslem
    print(f"Přičtení čísla (v1 + 10): {v4}")

    print(f"Jsou v1 a v2 stejné? {v1 == v2}") # Volá __eq__
    print(f"Je v1 stejný jako nový vektor(2,3)? {v1 == Vektor(2, 3)}")

    print(f"Délka vektoru v1 (len): {len(v1)}") # Volá __len__

    print("\n--- Práce s Batohem ---")
    b = Batoh()
    b.pridej("Svačina")
    b.pridej("Mapa")
    b.pridej("Kompas")

    print(b)
    print(f"Počet věcí: {len(b)}")
    print(f"První věc: {b[0]}") # Volá __getitem__