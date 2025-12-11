"""
Toto je modul 'geometrie', který je součástí balíčku 'muj_balicek'.
"""

def obsah_obdelniku(strana_a, strana_b):
    return strana_a * strana_b

def obvod_obdelniku(strana_a, strana_b):
    return 2 * (strana_a + strana_b)

def obsah_kruhu(polomer):
    # Ukázka absolutního importu uvnitř balíčku (potřebujeme PI z modulu matematika)
    # Pozor: Toto bude fungovat jen, pokud spustíme program z kořene (main.py)
    # Pokud bychom chtěli, aby byl balíček nezávislý, měli bychom PI definovat zde nebo importovat jinak.
    import matematika 
    return matematika.PI * (polomer ** 2)