# 02 - Grafové algoritmy

Grafy jsou datové struktury, které modelují vztahy mezi objekty. Skládají se z **vrcholů** (nodes/vertices) a **hran** (edges), které je propojují. Využívají se v navigacích (nejkratší cesta), sociálních sítích, počítačových sítích a mnoha dalších oblastech.

## Reprezentace grafu

V paměti počítače nejčastěji reprezentujeme graf dvěma způsoby:

1.  **Matice sousednosti (Adjacency Matrix):** 2D pole, kde `matice[i][j] == 1` znamená, že existuje hrana z `i` do `j`. Rychlé na zjištění hrany, ale náročné na paměť pro řídké grafy.
2.  **Seznam sousednosti (Adjacency List):** Každý vrchol má seznam svých sousedů. Toto je nejčastější způsob (v C++ např. `std::map<int, std::vector<Edge>>`).

## BFS (Breadth-First Search) - Prohledávání do šířky

BFS prohledává graf po "vrstvách". Nejprve navštíví startovní vrchol, pak všechny jeho přímé sousedy, pak sousedy sousedů atd.

* **Princip:** Používá **Frontu (Queue)** (FIFO - First In, First Out).
* **Využití:** Nalezení nejkratší cesty v **neohodnoceném** grafu (počet hran), web crawling, šíření signálu.
* **Složitost:** $O(V + E)$ (V = vrcholy, E = hrany).

## DFS (Depth-First Search) - Prohledávání do hloubky

DFS se snaží jít co nejdále po jedné větvi, dokud nenarazí na konec, a teprve poté se vrací (backtracking) a zkouší jinou větev.

* **Princip:** Používá **Zásobník (Stack)** (LIFO) nebo **Rekurzi**.
* **Využití:** Topologické řazení, hledání cyklů v grafu, řešení bludišť.
* **Složitost:** $O(V + E)$.

## Dijkstrův algoritmus

Slouží k nalezení nejkratší cesty v grafu, kde mají hrany **váhy** (např. vzdálenost v km, čas v minutách).

* **Podmínka:** Váhy hran nesmí být záporné.
* **Princip:** "Hladový" algoritmus. Udržuje si aktuální nejkratší vzdálenost ke všem vrcholům (na začátku nekonečno). Vždy vybere nenavštívený vrchol s nejmenší vzdáleností, navštíví ho a zkusí "vylepšit" (zrelaxovat) vzdálenosti k jeho sousedům.
* **Datová struktura:** Prioritní fronta (`std::priority_queue`).
* **Složitost:** $O(E \log V)$.

---

### Srovnání průchodu

Představte si, že hledáte někoho v budově:
* **BFS:** Prohledáte celé přízemí, pak celé první patro, pak celé druhé patro...
* **DFS:** Vběhnete do prvních dveří, běžíte chodbou až na konec, pak do schodů až na půdu, a když narazíte na zeď, vracíte se o křižovatku zpět.