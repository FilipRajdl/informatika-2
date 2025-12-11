class Zvire:
    """
    Rodičovská třída.
    Definuje základní atributy a metody společné pro všechna zvířata.
    """
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def spi(self):
        print(f"{self.jmeno} spí: Zzz...")

    def vydej_zvuk(self):
        print(f"{self.jmeno} vydává neznámý zvuk.")

    def info(self):
        return f"[Zvíře] Jméno: {self.jmeno}, Věk: {self.vek}"


class Pes(Zvire):
    """
    Potomek třídy Zvire.
    Dědí vše od rodiče, ale přepisuje metodu vydej_zvuk.
    """
    # __init__ nedefinujeme -> použije se automaticky ten z rodiče

    def vydej_zvuk(self):
        # Method Overriding (Přepisování metody)
        print(f"{self.jmeno} štěká: Haf haf!")

    def aportuj(self):
        # Nová metoda, kterou má pouze Pes
        print(f"{self.jmeno} běží pro míček!")


class Kocka(Zvire):
    """
    Potomek třídy Zvire.
    Ukazuje rozšíření konstruktoru pomocí super().
    """
    def __init__(self, jmeno, vek, barva):
        # 1. Voláme konstruktor rodiče pomocí super()
        # Tím zajistíme nastavení jmena a veku
        super().__init__(jmeno, vek)
        
        # 2. Nastavíme vlastní specifický atribut
        self.barva = barva

    def vydej_zvuk(self):
        print(f"{self.jmeno} mňouká: Mňau!")

    def info(self):
        # Rozšíření metody info
        # Nejdřív získáme text od rodiče
        zakladni_text = super().info()
        # A připojíme k němu naši specialitu
        return f"{zakladni_text}, Barva: {self.barva}"


if __name__ == "__main__":
    # 1. Vytvoření instance rodiče (zde to jde, protože není abstraktní)
    obecne_zvire = Zvire("Tvor", 10)
    obecne_zvire.vydej_zvuk()
    print(obecne_zvire.info())
    print("-" * 20)

    # 2. Vytvoření instance Psa (dědí __init__)
    alik = Pes("Alík", 5)
    alik.spi()          # Zděděná metoda
    alik.vydej_zvuk()   # Přepsaná metoda
    alik.aportuj()      # Nová metoda
    print("-" * 20)

    # 3. Vytvoření instance Kočky (používá super() v __init__)
    minda = Kocka("Minda", 3, "Mourovatá")
    minda.vydej_zvuk()
    print(minda.info()) # Volá rozšířenou metodu
    
    # 4. Ukázka isinstance
    print("-" * 20)
    print(f"Je Alík Pes? {isinstance(alik, Pes)}")
    print(f"Je Alík Zvire? {isinstance(alik, Zvire)}")
    # Logicky: Pes je Zvíře, proto True.