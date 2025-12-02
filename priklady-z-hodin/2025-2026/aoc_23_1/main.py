from os.path import join, realpath, dirname

# Sestavení cesty k souboru (předpokládá se, že data.txt je ve stejné složce)
cesta = join(dirname(realpath(__file__)), "data.txt")

celkovy_soucet = 0

try:
    with open(cesta, "r", encoding="utf-8") as f:  
        for radek in f:
            radek = radek.strip() # Odstraní neviditelné znaky na konci řádku (enter)
            
            # Vytvoří seznam pouze s číslicemi z daného řádku
            cisla = [znak for znak in radek if znak.isdigit()]
            
            # Pokud řádek obsahuje alespoň jednu číslici
            if cisla:
                # Vezme první a poslední číslici, spojí je jako text a převede na číslo
                # Příklad: z ['1', '2', '3'] udělá "13" -> 13
                # Příklad: z ['7'] udělá "77" -> 77 (první je zároveň poslední)
                hodnota = int(cisla[0] + cisla[-1])
                
                celkovy_soucet += hodnota
                
                # Výpis pro kontrolu (můžeš zakomentovat)
                # print(f"Řádek: {radek} -> Číslice: {cisla} -> Hodnota: {hodnota}")

    print("--- VÝSLEDEK ---")
    print(celkovy_soucet)

except FileNotFoundError:
    print(f"Chyba: Soubor 'data.txt' nebyl nalezen na cestě: {cesta}")