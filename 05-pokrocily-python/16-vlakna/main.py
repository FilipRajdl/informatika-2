"""
Ukázka práce s vlákny v Pythonu.
Demonstrujeme rozdíl mezi I/O bound a CPU bound úlohami a problém Race Condition.
"""

import threading
import time
import requests # Nutné nainstalovat: pip install requests (nebo použijeme time.sleep pro simulaci)

# --- 1. I/O Bound úloha (Zde vlákna pomáhají) ---
def stahuj_stranku(url):
    print(f"[{threading.current_thread().name}] Začínám stahovat: {url}")
    # Simulace čekání na síť (I/O operace uvolňuje GIL)
    time.sleep(2) 
    print(f"[{threading.current_thread().name}] Dokončeno: {url}")

def demo_io_bound():
    print("=== 1. I/O Bound Demo (Simulace stahování) ===")
    start = time.time()
    
    vlakna = []
    stranky = ["google.com", "seznam.cz", "github.com"]

    # Spuštění vláken
    for web in stranky:
        t = threading.Thread(target=stahuj_stranku, args=(web,), name=f"Vlákno-{web}")
        vlakna.append(t)
        t.start()

    # Čekání na dokončení
    for t in vlakna:
        t.join()

    end = time.time()
    print(f"Celkový čas (paralelně): {end - start:.2f} s")
    print("(Sériově by to trvalo 6 sekund!)\n")


# --- 2. CPU Bound úloha (Zde vlákna v Pythonu NEPOMÁHAJÍ kvůli GIL) ---
def narocny_vypocet(n):
    print(f"[{threading.current_thread().name}] Počítám do {n}...")
    while n > 0:
        n -= 1

def demo_cpu_bound():
    print("=== 2. CPU Bound Demo (Vliv GIL) ===")
    POCET = 50_000_000
    
    # A) Sériově (jedno vlákno)
    start = time.time()
    narocny_vypocet(POCET)
    narocny_vypocet(POCET)
    end = time.time()
    print(f"Sériově: {end - start:.2f} s")

    # B) Paralelně (dvě vlákna)
    start = time.time()
    t1 = threading.Thread(target=narocny_vypocet, args=(POCET,))
    t2 = threading.Thread(target=narocny_vypocet, args=(POCET,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print(f"Vlákna:  {end - start:.2f} s (Často pomalejší nebo stejné!)")
    print("TIP: Pro zrychlení výpočtů použijte modul 'multiprocessing'.\n")


# --- 3. Race Condition (Chyba souběhu) ---
sdileny_poklad = 0
zamek = threading.Lock() # Řešení: Mutex

def pridej_do_pokladu(pocet_opakovani):
    global sdileny_poklad
    for _ in range(pocet_opakovani):
        # KRITICKÁ SEKCE
        # Pokud odkomentujete 'with zamek:', chyba zmizí
        # with zamek:
            lokalni_kopie = sdileny_poklad
            lokalni_kopie += 1
            # Simulace přepnutí vlákna (v reálu se děje náhodně)
            # time.sleep(0) 
            sdileny_poklad = lokalni_kopie

def demo_race_condition():
    print("=== 3. Race Condition Demo ===")
    global sdileny_poklad
    sdileny_poklad = 0
    OPAKOVANI = 100000

    t1 = threading.Thread(target=pridej_do_pokladu, args=(OPAKOVANI,))
    t2 = threading.Thread(target=pridej_do_pokladu, args=(OPAKOVANI,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"Očekáváno: {2 * OPAKOVANI}")
    print(f"Výsledek:  {sdileny_poklad}")
    if sdileny_poklad != 2 * OPAKOVANI:
        print("CHYBA: Nastala Race Condition! (Použijte Lock)")
    else:
        print("OK (Měli jste štěstí, nebo je Lock aktivní)")


if __name__ == "__main__":
    demo_io_bound()
    demo_cpu_bound()
    demo_race_condition()