class Auto:
    """
    Třída reprezentující auto. Ukazuje práci s atributy a změnu stavu.
    """

    def __init__(self, znacka, model, barva):
        """
        Konstruktor (__init__) se volá při vytváření nového auta.
        Nastavuje počáteční stav atributů.
        """
        # Atributy instance (každé auto má svoje vlastní)
        self.znacka = znacka
        self.model = model
        self.barva = barva
        
        # Atributy, které nezadáváme při vytvoření, ale nastavíme je natvrdo
        self.je_nastartovano = False
        self.rychlost = 0

    def info(self):
        """Vypíše informace o autě."""
        stav_motoru = "běží" if self.je_nastartovano else "vypnutý"
        print(f"Auto: {self.znacka} {self.model} ({self.barva})")
        print(f"Motor: {stav_motoru}, Rychlost: {self.rychlost} km/h")
        print("-" * 30)

    def nastartuj(self):
        """Změní stav nastartování."""
        if self.je_nastartovano:
            print("Motor už běží!")
        else:
            print("Startuji motor!")
            self.je_nastartovano = True

    def vypni_motor(self):
        """Vypne motor, ale jen pokud auto stojí."""
        if self.rychlost > 0:
            print("Nemůžeš vypnout motor za jízdy! Nejdřív zastav.")
        else:
            print("Motor vypnut.")
            self.je_nastartovano = False

    def zrychli(self, o_kolik):
        """Zvýší rychlost auta, pokud je nastartováno."""
        if not self.je_nastartovano:
            print("Nemůžeš jet, motor je vypnutý!")
        else:
            self.rychlost += o_kolik
            print(f"Zrychluji na {self.rychlost} km/h.")

    def zabrzdi(self):
        """Okamžitě zastaví auto."""
        print("Brzdím na 0 km/h.")
        self.rychlost = 0


# --- Hlavní část programu (použití třídy) ---
if __name__ == "__main__":
    # 1. Vytvoření instancí (objektů)
    moje_auto = Auto("Škoda", "Octavia", "Bílá")
    sousedovo_auto = Auto("Ferrari", "F40", "Červená")

    # 2. Práce s prvním autem
    moje_auto.info()
    moje_auto.zrychli(50) # Nepůjde to, není nastartováno
    
    moje_auto.nastartuj()
    moje_auto.zrychli(50)
    moje_auto.zrychli(30)
    moje_auto.info()

    # 3. Práce s druhým autem (má vlastní data)
    print("\n--- Sousedovo auto ---")
    sousedovo_auto.nastartuj()
    sousedovo_auto.info() # Rychlost je 0, i když moje_auto jede 80
    
    # 4. Ukázka logiky (vypnutí motoru za jízdy)
    print("\n--- Pokus o vypnutí za jízdy ---")
    moje_auto.vypni_motor()
    moje_auto.zabrzdi()
    moje_auto.vypni_motor()