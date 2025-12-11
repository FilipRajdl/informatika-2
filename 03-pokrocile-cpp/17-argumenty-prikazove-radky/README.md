# **17 - Argumenty příkazové řádky**

Dosud naše programy běžely "samy od sebe" nebo si data načítaly přes `std::cin`. Profesionální nástroje (jako `ls`, `grep`, `git`) ale většinou ovládáme pomocí parametrů zadaných rovnou při spuštění.

## **Signatura funkce `main`**

Aby program mohl přijímat argumenty, musíme použít rozšířenou definici funkce `main`:

```cpp
int main(int argc, char* argv[]) {  
    // kód  
    return 0;  
}
```

### **`int argc` (ARGument Count)**

Udává **počet** argumentů.

* **Pozor:** Název samotného programu se počítá také!  
* Pokud spustíte `./program`, `argc` bude 1.  
* Pokud spustíte `./program a b`, `argc` bude 3.

### **`char* argv[]` (ARGument Vector)**

Je to pole textových řetězců (C-stringů), které obsahují jednotlivé argumenty.

* `argv[0]` = název programu (např. "`./program`")  
* `argv[1]` = první parametr  
* `argv[2]` = druhý parametr  
* ...

## **Převod textu na čísla**

Všechny argumenty v `argv` jsou texty (`char*`). Pokud chceme počítat, musíme je převést.

### **Moderní C++ (`std::string` a `<string>`)**

Doporučený způsob. Automaticky vyhazují výjimky při chybě.

* `std::stoi(str)` - String to Integer  
* `std::stod(str)` - String to Double

```cpp
#include <string>

std::string arg1 = argv[1]; // Převod char* na std::string  
int cislo = std::stoi(arg1);
```

### **Starší C-style (`<cstdlib>`)**

Funkce jako `atoi` (Ascii to Integer) nebo `atof`.

* Rychlejší, ale méně bezpečné (při chybě vrací 0, což může být matoucí).

## **Zpracování přepínačů**

V C++ neexistuje v základní knihovně nic jako Pythonní `argparse`. Musíme si parsování napsat sami (cyklem) nebo použít externí knihovnu (např. `Boost.Program_options`, `CLI11`).

Pro jednoduché školní projekty stačí projít pole `argv` v cyklu:

```cpp
for (int i = 1; i < argc; ++i) {  
    std::string arg = argv[i];  
    if (arg == "-h" || arg == "--help") {  
        // zobrazit nápovědu  
    }  
}
```