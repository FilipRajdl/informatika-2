"""
BENCHMARK: Sériově vs. Vlákna vs. Procesy
Tento skript demonstruje, proč je pro výpočty nutné použít multiprocessing.
"""

import time
import threading
import multiprocessing

# --- Výpočetně náročná funkce (CPU Bound) ---
def spocitej_prvocisla(n):
    # Hledá počet prvočísel do n (naivní pomalý algoritmus)
    count = 0
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

def run_serial(narocnost):
    print("--- 1. Sériový běh (Jeden proces) ---")
    start = time.time()
    spocitej_prvocisla(narocnost)
    spocitej_prvocisla(narocnost)
    end = time.time()
    print(f"Čas: {end - start:.2f} s\n")

def run_threads(narocnost):
    print("--- 2. Vlákna / Threading (GIL limituje) ---")
    start = time.time()
    t1 = threading.Thread(target=spocitej_prvocisla, args=(narocnost,))
    t2 = threading.Thread(target=spocitej_prvocisla, args=(narocnost,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print(f"Čas: {end - start:.2f} s (Žádné zrychlení!)")
    print("Důvod: Vlákna se střídají na jednom jádře kvůli GIL.\n")

def run_multiprocessing(narocnost):
    print("--- 3. Multiprocessing (Více jader) ---")
    start = time.time()
    # Vytvoříme dva samostatné procesy
    p1 = multiprocessing.Process(target=spocitej_prvocisla, args=(narocnost,))
    p2 = multiprocessing.Process(target=spocitej_prvocisla, args=(narocnost,))
    p1.start()
    p2.start()
    p1.join() # Čekáme na dokončení
    p2.join()
    end = time.time()
    print(f"Čas: {end - start:.2f} s (Zrychlení!)")
    print("Důvod: Každý proces má vlastní Python interpret a běží na jiném jádře.\n")

if __name__ == "__main__":
    # POZOR: Na Windows je tato podmínka NUTNÁ pro multiprocessing.
    
    # Nastavení náročnosti (upravte podle rychlosti vašeho PC)
    NAROCNOST = 1_000_000 
    
    print(f"Počítám prvočísla do {NAROCNOST} (2x)...")
    
    run_serial(NAROCNOST)
    run_threads(NAROCNOST)
    run_multiprocessing(NAROCNOST)