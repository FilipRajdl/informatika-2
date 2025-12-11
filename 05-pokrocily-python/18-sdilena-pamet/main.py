"""
Základní ukázka sdílené paměti s využitím Multiprocessingu.
Hlavní proces vytvoří paměť, Potomek do ní zapíše a Hlavní proces data přečte.
"""

import multiprocessing
from multiprocessing.shared_memory import SharedMemory
import time

def pracuj_jako_potomek(shm_name):
    """
    Kód, který běží v samostatném procesu.
    """
    print(f"[Potomek] Startuji. Připojuji se k paměti: {shm_name}")
    
    # Připojení k existující paměti (create=False je default)
    existing_shm = SharedMemory(name=shm_name)
    
    # Zápis dat do bufferu
    # buffer se chová jako pole bytů (bytearray)
    zprava = "Zdravím z druhého procesu!"
    data = zprava.encode('utf-8')
    
    # Zapíšeme data na začátek paměti
    existing_shm.buf[:len(data)] = data
    
    print(f"[Potomek] Data zapsána. Končím.")
    
    # Každý proces musí zavřít svůj přístup k paměti
    existing_shm.close() 

def main():
    # 1. Vytvoření sdílené paměti (velikost 1024 bytů)
    # create=True říká, že žádáme OS o alokaci nové paměti
    shm = SharedMemory(create=True, size=1024)

    try:
        print(f"[Rodič] Paměť vytvořena: {shm.name}")

        # 2. Spuštění potomka
        # Předáme mu POUZE JMÉNO paměti (string), nikoliv objekt paměti samotný.
        p = multiprocessing.Process(target=pracuj_jako_potomek, args=(shm.name,))
        p.start()
        
        # Čekáme, až potomek dokončí práci
        p.join()

        # 3. Čtení dat v rodiči
        # Přečteme data, ořízneme prázdné nuly (b'\x00') a dekódujeme
        data_z_pameti = bytes(shm.buf).rstrip(b'\x00')
        print(f"[Rodič] Přečteno z paměti: {data_z_pameti.decode('utf-8')}")

    finally:
        # 4. Úklid
        # unlink() volá pouze ten proces, který paměť vytvořil (vlastník)
        # Pokud to neuděláme, paměť zůstane v RAM i po skončení skriptu!
        shm.close()
        shm.unlink()
        print("[Rodič] Paměť uvolněna.")

if __name__ == "__main__":
    main()