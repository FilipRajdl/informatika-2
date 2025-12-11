"""
Pokročilá ukázka: Sdílení NumPy pole.
Toto je reálný use-case. Místo kopírování obrovských matic mezi procesy
(což trvá dlouho), sdílíme přímo podkladovou paměť.

POZOR: Vyžaduje instalaci numpy (pip install numpy)
"""

import multiprocessing
from multiprocessing.shared_memory import SharedMemory
import time

# Zkusíme importovat numpy
try:
    import numpy as np
except ImportError:
    print("CHYBA: Tento příklad vyžaduje knihovnu 'numpy'.")
    print("Nainstalujte ji pomocí: pip install numpy")
    exit(1)

def proces_vypocet(shm_name, shape, dtype):
    """
    Proces, který načte pole ze sdílené paměti a modifikuje ho.
    """
    print(f"[Potomek] Připojuji se k paměti...")
    shm = SharedMemory(name=shm_name)
    
    # Vytvoříme NumPy pole, které používá sdílenou paměť jako svůj buffer
    # Nemusíme alokovat novou paměť, jen vytvoříme "pohled" (view).
    np_array = np.ndarray(shape, dtype=dtype, buffer=shm.buf)
    
    print(f"[Potomek] Vidím pole: {np_array}")
    print(f"[Potomek] Provádím výpočet (mocnění na druhou)...")
    
    # Modifikace pole in-place (přímo v paměti)
    # Změny se okamžitě projeví v hlavním procesu
    np_array[:] = np_array ** 2
    
    shm.close()

def main():
    # Vytvoříme malé pole pro demonstraci
    pole_orig = np.array([1, 2, 3, 4, 5, 6])
    
    # 1. Alokace sdílené paměti
    # Velikost v bytech zjistíme z nbytes
    shm = SharedMemory(create=True, size=pole_orig.nbytes)

    try:
        # 2. Vytvoření pole v rodiči nad sdílenou pamětí
        pole_shared = np.ndarray(pole_orig.shape, dtype=pole_orig.dtype, buffer=shm.buf)
        
        # Zkopírujeme data do sdílené paměti
        pole_shared[:] = pole_orig[:]

        print(f"[Rodič] Původní pole: {pole_shared}")

        # 3. Spuštění procesu
        # Musíme předat metadata (tvar, typ), aby numpy vědělo, jak data interpretovat
        p = multiprocessing.Process(target=proces_vypocet, args=(shm.name, pole_orig.shape, pole_orig.dtype))
        p.start()
        p.join()

        # 4. Kontrola výsledku
        print(f"[Rodič] Pole po výpočtu potomka: {pole_shared}")
        print("(Všimněte si, že data se změnila, aniž bychom něco vraceli přes return)")

    finally:
        shm.close()
        shm.unlink()

if __name__ == "__main__":
    main()