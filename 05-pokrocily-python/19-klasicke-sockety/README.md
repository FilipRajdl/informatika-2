# **19 - Klasické Sockety (Blocking I/O)**

Tento modul se zaměřuje na nízkoúrovňovou práci se sítí pomocí modulu socket.  
Princip je identický jako v C++ (Berkeley Sockets API).

## **1. Příklad: Blokující I/O a Vlákna**

Standardní sockety jsou blokující. Když zavoláte `recv()`, program se zastaví a čeká.  
Aby TCP server mohl obsloužit více lidí najednou, musíme pro každého vytvořit vlákno (viz `server.py`). U UDP to často není nutné, protože zprávy chodí samostatně a vyřizují se rychle.

## **5. Specifika Pythonu (vs. C++)**

Ačkoliv je API téměř shodné, Python nabízí několik "vychytávek", které v C++ nemáme.

### **A. GIL a Sítě (Důležité!)**

V lekci o vláknech jsme říkali, že GIL (Global Interpreter Lock) brzdí paralelní běh.  
Výjimka: Blokující I/O operace (`recv`, `send`, `accept`) v Pythonu uvolňují GIL.  
To znamená, že zatímco jedno vlákno čeká na data ze sítě, ostatní vlákna mohou volně běžet. Proto je v Pythonu architektura "Vlákno pro každého klienta" překvapivě efektivní (pro I/O bound úlohy).

### **B. Context Managery (`with`)**

V C++ musíte myslet na close(). V Pythonu používejte blok `with`:

```python
with socket.socket(...) as s:  
    s.bind(...)  
    s.listen()  
    # Po opuštění bloku se socket automaticky a bezpečně zavře
```

### **C. Metoda `makefile()`**

Socket posílá surové byty (`b'ahojn'`). Často ale chceme posílat textové řádky.  
Místo složitého bufferování v C++ můžeme v Pythonu socket považovat za soubor: 

```python
# Vytvoříme ze socketu "soubor" pro čtení (r) a psaní (w)  
soubor = conn.makefile('rw')

# Nyní můžeme používat print() a readline()!  
soubor.write("Ahoj kliente!n")  
soubor.flush() # Vynutit odeslání

odpoved = soubor.readline() # Přečte řádek ukončený n  
```