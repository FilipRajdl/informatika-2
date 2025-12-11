class BankovniUcet:
    """
    Třída demonstrující použití privátních atributů a properties (vlastností)
    pro bezpečný přístup k datům.
    """

    def __init__(self, majitel, pocatecni_vklad):
        self.majitel = majitel          # Public atribut
        self._typ_uctu = "Běžný"        # Protected atribut (konvence)
        self.__zustatek = pocatecni_vklad # Private atribut (name mangling)

    # --- Property pro 'zustatek' ---
    
    # Getter: Umožňuje číst zůstatek jako 'objekt.zustatek'
    @property
    def zustatek(self):
        return self.__zustatek

    # Setter: Umožňuje zapisovat do zůstatku jako 'objekt.zustatek = hodnota'
    # Zde implementujeme validaci dat.
    @zustatek.setter
    def zustatek(self, nova_hodnota):
        if nova_hodnota < 0:
            print(f"CHYBA: Nelze nastavit záporný zůstatek ({nova_hodnota}).")
        else:
            print(f"INFO: Změna zůstatku z {self.__zustatek} na {nova_hodnota}.")
            self.__zustatek = nova_hodnota

    # --- Další metody ---

    def vloz_penize(self, castka):
        if castka > 0:
            self.__zustatek += castka
            print(f"Vloženo: {castka}")
        else:
            print("Částka pro vklad musí být kladná.")

    def vyber_penize(self, castka):
        if 0 < castka <= self.__zustatek:
            self.__zustatek -= castka
            print(f"Vybráno: {castka}")
        else:
            print("Nedostatek prostředků nebo neplatná částka.")

    def _interni_log(self, zprava):
        """Protected metoda - určena jen pro vnitřní použití."""
        print(f"[LOG]: {zprava}")


if __name__ == "__main__":
    ucet = BankovniUcet("Petr Novák", 1000)

    # 1. Přístup přes Property (čtení)
    print(f"Majitel: {ucet.majitel}")
    print(f"Aktuální zůstatek: {ucet.zustatek}")  # Volá metodu pod @property

    # 2. Přístup přes Property (zápis s validací)
    print("\n--- Pokus o nastavení záporného zůstatku ---")
    ucet.zustatek = -500  # Toto zavolá setter a vypíše chybu

    print("\n--- Validní změna ---")
    ucet.zustatek = 2000  # Toto projde

    # 3. Ukázka Private atributu
    print("\n--- Pokus o přímý přístup k __zustatek ---")
    try:
        print(ucet.__zustatek)
    except AttributeError as e:
        print(f"Chyba přístupu: {e}")
        # Atribut ve skutečnosti existuje, ale jmenuje se _BankovniUcet__zustatek
    
    # Name Mangling v praxi (nedoporučuje se používat, jen pro demonstraci)
    print(f"Tajný přístup (mangeld name): {ucet._BankovniUcet__zustatek}")