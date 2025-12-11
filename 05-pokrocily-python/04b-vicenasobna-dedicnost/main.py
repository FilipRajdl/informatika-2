"""
Ukázka vícenásobné dědičnosti a řešení Diamantového problému.
"""

class Zaklad:
    def __init__(self):
        print("  -> START init: Zaklad")
        # I základní třída by měla volat super(), aby řetězec pokračoval (k 'object')
        super().__init__() 
        print("  <- KONEC init: Zaklad")

class LevaVevet(Zaklad):
    def __init__(self):
        print("  -> START init: LevaVevet")
        super().__init__()
        print("  <- KONEC init: LevaVevet")

class PravaVevet(Zaklad):
    def __init__(self):
        print("  -> START init: PravaVevet")
        super().__init__()
        print("  <- KONEC init: PravaVevet")

class Vrchol(LevaVevet, PravaVevet):
    def __init__(self):
        print("-> START init: Vrchol")
        super().__init__()
        print("<- KONEC init: Vrchol")

# --- Co se stane bez super()? ---
# Kdybychom v LevaVevet napsali 'Zaklad.__init__(self)'
# a v PravaVevet napsali 'Zaklad.__init__(self)',
# tak se Zaklad provede 2x.

# --- Hlavní program ---
if __name__ == "__main__":
    print("=== Vytvářím instanci třídy Vrchol ===")
    v = Vrchol()
    
    print("\n=== Pořadí MRO (Method Resolution Order) ===")
    # Ukáže, v jakém pořadí Python prochází třídy
    mro_list = Vrchol.mro()
    
    for i, cls in enumerate(mro_list):
        print(f"{i}. {cls.__name__}")

    print("\n=== Vysvětlení ===")
    print("Všimněte si, že 'Zaklad' se vypsal pouze JEDNOU, i když dědíme dvěma cestami.")
    print("Dále si všimněte, že v 'LevaVevet' funkce super() zavolala 'PravaVevet',")
    print("nikoliv 'Zaklad'. To je kouzlo MRO.")