# **18 - Vlákna a Paralelní programování**

## **1. Teoretický úvod: Proč a jak?**

### **Motivace: Konec zvyšování frekvence**

Dlouhá léta se výkon počítačů zvyšoval zrychlováním taktu procesoru (frekvence). Kolem roku 2005 jsme však narazili na fyzikální limity (teplo, spotřeba). Výrobci procesorů proto přešli na jinou strategii: **více jader**.

Aby náš program běžel rychleji na moderním procesoru, nemůžeme jen čekat na rychlejší hardware. Musíme náš kód napsat tak, aby využíval více jader najednou.

### **Proces vs. Vlákno**

Je důležité rozlišovat mezi těmito dvěma pojmy:

1. **Proces (Process):**  
   * Je to běžící instance programu.  
   * Má **vlastní paměťový prostor**. Jeden proces nemůže přímo číst paměť jiného procesu (bez speciálních technik jako sdílená paměť).  
   * Je náročný na vytvoření a přepínání.  
2. **Vlákno (Thread):**  
   * Je to soubor operací k vykonání *uvnitř* procesu.  
   * Všechna vlákna v jednom procesu **sdílejí stejnou paměť** (globální proměnné, heap).  
   * Každé vlákno má ale vlastní **Zásobník (Stack)** (pro lokální proměnné a volání funkcí).

### **Jak to funguje? (Scheduling)**

I když máte 4jádrový procesor, můžete spustit 100 vláken. Jak je to možné?  
Operační systém obsahuje **Plánovač (Scheduler)**. Ten velmi rychle střídá vlákna na procesoru (tzv. **Context Switch**). Děje se to tisíckrát za sekundu, takže to vypadá, že běží vše najednou.

* **Paralelismus:** Vlákna běží fyzicky ve stejný okamžik na různých jádrech.  
* **Konkurence (Concurrency):** Vlákna se střídají na jednom jádře tak rychle, že to vyvolává iluzi paralelismu.

### **Realita výkonu: Amdahlův zákon**

Častým omylem je, že pokud program běží na 4jádrovém procesoru, bude 4× rychlejší. To v praxi téměř nikdy neplatí. Maximální možné zrychlení je limitováno tou částí programu, která **musí běžet sériově** (nelze paralelizovat – např. načítání souboru, inicializace, sčítání dílčích výsledků).

Tomuto pravidlu se říká **Amdahlův zákon**.

  * Pokud 50 % programu musí běžet sériově, maximální zrychlení je pouze **2×**, i kdybyste měli 1000 jader.
  * Pro efektivní paralelizaci je klíčové minimalizovat sériové části kódu a synchronizaci (čekání na zámky).


## **2. Vlákna v C++ (`std::thread`)**

Od standardu C++11 je podpora vláken součástí jazyka.

```cpp
#include <thread>

void pracuj(int id) {  
    // ... kód vlákna ...  
}

int main() {  
    // Spuštění vlákna  
    std::thread t1(pracuj, 1);  
      
    // Čekání na dokončení (join)  
    // Pokud nezavoláme join() a objekt 't1' zanikne, program spadne (std::terminate).  
    t1.join();   
      
    return 0;  
}
```

## **2.1 Úlohy místo vláken (`std::future` a `std::async`)**

Práce přímo s `std::thread` je nízkoúrovňová. Musíte manuálně řešit předávání výsledků a chytání výjimek (pokud vlákno vyhodí výjimku, program spadne).

Moderní C++ nabízí vyšší úroveň abstrakce pomocí **`std::async`**.

1.  **`std::future`**: Představuje příslib výsledku, který bude k dispozici v budoucnu.
2.  **`std::async`**: Spustí funkci (možná v novém vlákně, možná v thread poolu) a vrátí `std::future`.

```cpp
#include <future>
#include <iostream>

int slozityVypocet(int x) {
    if (x < 0) throw std::runtime_error("Chyba!");
    return x * x; 
}

int main() {
    // Spustí výpočet asynchronně
    std::future<int> vysledek = std::async(std::launch::async, slozityVypocet, 10);

    // Zde může hlavní vlákno dělat jinou práci...
    
    try {
        // get() počká na dokončení a vrátí hodnotu (nebo vyhodí výjimku z vlákna)
        std::cout << "Vysledek: " << vysledek.get() << std::endl; 
    } catch (const std::exception& e) {
        std::cout << "Ve vlákně nastala chyba: " << e.what() << std::endl;
    }
    return 0;
}
```

## **3. Problematika sdílení dat**

Protože vlákna sdílejí paměť, je komunikace mezi nimi velmi rychlá. Přináší to ale obrovské riziko: **Race Condition (Souběh)**.

### **Co je Race Condition?**

Nastává, když dvě vlákna přistupují ke stejné paměti současně, alespoň jedno z nich zapisuje a přístup není synchronizovaný.

Představte si operaci `i++` (inkrementace). Ta není atomická (nedělitelná), ale skládá se ze tří instrukcí procesoru:

1. **READ:** Načti hodnotu `i` z paměti do registru.  
2. **MODIFY:** Přičti 1 k registru.  
3. **WRITE:** Zapiš hodnotu z registru zpět do paměti.

Pokud dvě vlákna udělají `i++` současně nad `i=0`:

* Vlákno A načte 0.  
* Vlákno B načte 0 (ještě se nestihlo zapsat).  
* Vlákno A přičte 1 a zapíše 1.  
* Vlákno B přičte 1 a zapíše 1.  
* **Výsledek:** `i` je 1, ale mělo být 2!

## **4. Synchronizační techniky**

Abychom zabránili Race Condition, používáme synchronizační primitiva.

### **A. Mutex (`std::mutex`)**

*Mutual Exclusion* (Vzájemné vyloučení). Funguje jako zámek na dveřích. Kdo má klíč (zámek), ten je uvnitř. Ostatní musí čekat ve frontě.

Best Practice: RAII (`std::lock_guard`)  
Nikdy nevolejte `lock()` a `unlock()` manuálně, pokud nemusíte. Pokud mezi nimi vyletí výjimka nebo zapomenete na unlock, program "zamrzne" navždy (tzv. Deadlock). Používejte wrappery:  

```cpp
std::mutex mtx;

void bezpecnaFunkce() {  
    // Konstruktor zamkne mutex  
    std::lock_guard<std::mutex> zamek(mtx);   
      
    // ... kritická sekce ...  
    // sdilena_promenna++;  
      
    // Destruktor 'zamek' automaticky odemkne mutex (i při vyhození výjimky)  
}
```

* **`std::unique_lock`**: Podobné jako `lock_guard`, ale flexibilnější. Umožňuje zamknout/odemknout mutex vícekrát, nebo převzít vlastnictví zámku. Nutné pro Condition Variables.

#### **Nebezpečí: Deadlock (Uváznutí)**

Při používání více mutexů hrozí tzv. **Deadlock**. Nastane situace, kdy vlákno A drží zámek M1 a čeká na M2, zatímco vlákno B drží M2 a čeká na M1. Obě vlákna čekají věčně.

**Řešení (C++17): `std::scoped_lock`**
Tento chytrý zámek umí zamknout více mutexů najednou bez rizika deadlocku (používá speciální algoritmus pro bezpečné pořadí zamykání).

```cpp
std::mutex m1, m2;

void bezpecnaVymena() {
    // Zamkne oba mutexy najednou a bezpečně
    std::scoped_lock lock(m1, m2);
    
    // ... bezpečná práce se zdroji chráněnými m1 i m2 ...
}
```

#### **Další rizika: Livelock a Starvation**

Kromě úplného zastavení (Deadlock) existují i další stavy, kdy program neběží správně:

1.  **Livelock (Živé uváznutí):**
    * Na rozdíl od Deadlocku vlákna nejsou zablokovaná (nespí). Neustále pracují a spotřebovávají CPU, ale program se neposouvá vpřed.
    * **Příklad:** Dva lidé se potkají v úzké chodbě. Oba ústoupí doleva. Oba narazí. Oba ústoupí doprava. Zase narazí. Stále se hýbou, ale nikam se nedostanou. V kódu se to stává, když se vlákna snaží být příliš "zdvořilá" a při detekci konfliktu obě okamžitě uvolní zdroje a zkusí to znovu ve stejný okamžik.

2.  **Starvation (Hladovění):**
    * Nastává, když se vlákno s nižší prioritou nikdy nedostane ke slovu, protože agresivnější vlákna (nebo vlákna s vyšší prioritou) neustále obsazují zámek/zdroj. Vlákno sice není zaseknuté, ale prakticky stojí.

### **B. Atomické operace (`std::atomic`)**

Pro jednoduché proměnné (int, bool) je Mutex je pomalý. Procesory podporují speciální instrukce, které umí udělat `i++` nedělitelně.

```cpp
#include <atomic>

std::atomic<int> pocitadlo(0);

void vlakno() {  
    pocitadlo++; // Toto je thread-safe bez mutexu!  
}
```

### **C. Podmíněné proměnné (`std::condition_variable`)**

Slouží k synchronizaci **událostí**. Řeší problém, kdy vlákno potřebuje čekat, až jiné vlákno dokončí práci nebo připraví data.

Místo toho, aby vlákno v cyklu neustále kontrolovalo proměnnou (Busy Wait - vytěžuje CPU na 100%), se "uspí" a čeká na signál.

**Příklad použití:** Producent-Konzument (Fronta úloh).

1. Konzument zamkne mutex a zkontroluje, zda je fronta prázdná.  
2. Pokud je prázdná, zavolá `cv.wait(lock)`. Tím **odemkne mutex** a uspí se.  
3. Producent vloží data, zamkne mutex a zavolá `cv.notify_one()`.  
4. Konzument se probudí, **znovu zamkne mutex** a zpracuje data.

### **D. Semafor (`std::counting_semaphore`) (C++20)**

Zatímco mutex je zámek (stavy 0/1), semafor je "počítadlo". Povolí vstup do sekce N vláknům současně. Užitečné pro správu omezených zdrojů (např. pool databázových spojení).

## **Shrnutí: Co kdy použít?**

1. **Potřebuji jen inkrementovat číslo nebo přepnout flag?** -> Použij `std::atomic`.  
2. **Potřebuji chránit složitější strukturu (vector, mapu)?** -> Použij `std::mutex` s `std::lock_guard`.  
3. **Potřebuji čekat, až se něco stane?** -> Použij `std::condition_variable`.  
4. **Potřebuji omezit počet vláken přistupujících ke zdroji?** -> Použij `std::counting_semaphore`.

## **5. Pokročilé koncepty a optimalizace**

Kromě správnosti kódu musíme u paralelního programování řešit i efektivitu a architekturu.

### **Thread Pool (Fond vláken)**

Vytvoření nového vlákna (`std::thread`) je pro operační systém drahá operace (alokace paměti pro zásobník, registrace v jádře OS). Pokud tvoříte vlákno pro každou malou úlohu, program bude pomalý.

**Řešení:** Vytvoříte skupinu vláken (Pool) pouze jednou při startu aplikace (např. 8 vláken). Ta ve smyčce čekají na přidělení práce z fronty úloh. Jakmile úlohu dokončí, nezruší se, ale vezmou si další.

### **False Sharing (Falešné sdílení)**

Skrytý zabiják výkonu na úrovni hardwaru.
Procesory nečtou paměť po bajtech, ale po blocích (tzv. **Cache Line**, obvykle 64 bytů).

Pokud dvě vlákna často zapisují do dvou *různých* proměnných, které ale leží v paměti *těsně vedle sebe* (na stejné Cache Line), jádra procesoru se budou neustále "přetahovat" o vlastnictví tohoto bloku cache. To drasticky zpomaluje program, i když logicky nedochází k Race Condition.

**Řešení:** Použití `alignas(64)` pro zarovnání proměnných v paměti tak, aby každá ležela na vlastní Cache Line.