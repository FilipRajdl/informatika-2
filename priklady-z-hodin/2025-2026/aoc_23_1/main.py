from os.path import join, realpath, dirname

cesta = join(dirname(realpath(__file__)),"data.txt")

sum = 0

with open(cesta, "r", encoding="utf-8") as f:  
    for c, radek in enumerate(f):
        # print(c,line)
        cisla = [znak for znak in radek if znak.isdigit()]
        sum+=int(cisla[0]+cisla[-1])
        # for znak in radek:
        #     if znak.isdigit(): print(znak, end=", ")
        print(cisla)
print(sum)