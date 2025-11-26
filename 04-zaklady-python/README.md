# **04 - Základy jazyka Python**

Tato sekce se zaměřuje na úvod do programovacího jazyka **Python**. Python je vysokoúrovňový interpretovaný jazyk, který klade důraz na čitelnost kódu.

## **Vývojové prostředí (DevContainer)**

Tento repozitář je nakonfigurován jako **DevContainer**. To znamená, že máte připravené kompletní prostředí pro vývoj bez nutnosti cokoliv instalovat do svého počítače.

**Co máte k dispozici:**

* **Python 3.x** - Interpret jazyka je již nainstalován.  
* **VS Code Extensions** - Doplňky pro Python, Jupyter Notebooky a lintery jsou aktivní.  
* **Terminál** - Příkazová řádka je integrovaná přímo v editoru.

## **Jak pracovat s materiály**

V každé složce naleznete tři typy souborů:

1. README.md - Teorie k danému tématu.  
2. main.py - Ukázkový skript.  
3. teorie.ipynb - Interaktivní sešit (Jupyter Notebook).

### **Možnost A: Spouštění Python skriptů (.py)**

Jelikož jste ve VS Code, máte dvě snadné možnosti:

1. **Tlačítko Play:** Otevřete soubor main.py a klikněte na ikonu "Play" v pravém horním rohu editoru. Kód se spustí v terminálu.  
2. **Terminál:** Otevřete terminál (zkratka Ctrl + ; nebo menu Terminal -> New Terminal) a napište:

   ```bash
   python cesta/k/souboru/main.py
   ```

### **Možnost B: Interaktivní sešity (.ipynb)**

Jupyter Notebooky umožňují spouštět kód po částech (buňkách) a vidět výsledek okamžitě pod nimi.

1. Otevřete soubor s koncovkou .ipynb.  
2. VS Code automaticky načte rozhraní pro notebooky (pokud se zeptá na "Kernel", zvolte **Python 3** nebo **Recommended**).  
3. Kliknutím na tlačitko spustit vlevo u každé buňky spustíte daný kus kódu.

## **Obsah sekce**

1. [Syntaxe, výstup a komentáře](./01-syntaxe-komentare/)  
2. [Proměnné a datové typy](./02-proměnné-datové-typy/)
3. [Operátory](./03-operatory/)  
4. [Podmínky a vetvení](./04-podmínky-větvení/)
5. [Cykly](./05-cykly/)
6. [Datové struktury](./06-datove-struktury/)
7. [Prace se soubory](./07-prace-se-soubory/)
8. [Funkce](./08-funkce/)