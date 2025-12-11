"""
13 - Generátory a Iterátory: Praktická ukázka

Tento skript demonstruje rozdíl mezi klasickým seznamem (list) a generátorem.
Ukazuje, jak generátory šetří paměť tím, že hodnoty vytvářejí "za běhu" (lazy evaluation).
"""

import sys
import time

# 1. Vlastní Iterátor (Starý, složitý způsob - pro pochopení principu)
class MujRange:
    """Třída, která se chová jako vestavěná funkce range()."""
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        # Musí vrátit sám sebe
        return self

    def __next__(self):
        # Musí vrátit další hodnotu nebo vyvolat StopIteration
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

# 2. Generátor (Moderní, jednoduchý způsob pomocí yield)
def muj_range_generator(start, end):
    """Funkce, která dělá to samé jako třída výše, ale mnohem jednodušeji."""
    current = start
    while current < end:
        yield current # Tady se funkce "pozastaví" a vrátí hodnotu
        current += 1

# 3. Fibonacciho posloupnost (Nekonečný generátor)
def fibonacci():
    """Generuje Fibonacciho čísla do nekonečna."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# --- Hlavní program ---
if __name__ == "__main__":
    print("=== 1. Vlastní iterátor (Třída) ===")
    iterator = MujRange(0, 3)
    # Interně se volá iterator.__next__()
    for i in iterator:
        print(i, end=" ")
    print("\n")

    print("=== 2. Generátor (yield) ===")
    gen = muj_range_generator(0, 3)
    for i in gen:
        print(i, end=" ")
    print("\n")

    print("=== 3. Srovnání paměti (List vs Generator) ===")
    N = 1_000_000 # Milion čísel
    
    # A) List Comprehension (vytvoří vše v paměti hned)
    t0 = time.time()
    seznam = [x**2 for x in range(N)]
    t1 = time.time()
    velikost_list = sys.getsizeof(seznam)
    print(f"List:      Čas={t1-t0:.4f}s, Velikost v paměti={velikost_list / 1024 / 1024:.2f} MB")

    # B) Generator Expression (vytváří postupně)
    t0 = time.time()
    generator = (x**2 for x in range(N)) # Všimněte si kulatých závorek
    t1 = time.time()
    velikost_gen = sys.getsizeof(generator)
    print(f"Generátor: Čas={t1-t0:.4f}s, Velikost v paměti={velikost_gen} BYTES (!!!)")
    
    print(f"\nGenerátor je {velikost_list / velikost_gen:.0f}x menší!")

    print("\n=== 4. Nekonečný generátor ===")
    fib = fibonacci()
    print("Prvních 5 Fibonacciho čísel:")
    for _ in range(5):
        # Ruční volání next()
        print(next(fib), end=" ")
    print("\n(Generátor čeká na další zavolání...)")