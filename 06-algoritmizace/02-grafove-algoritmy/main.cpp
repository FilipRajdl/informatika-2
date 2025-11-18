#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <limits> // Pro "nekonečno"
#include <algorithm> // Pro std::reverse

// Struktura pro hranu (cilovy vrchol a vaha)
struct Hrana {
    int cil;
    int vaha;
};

// Třída reprezentující graf pomocí seznamu sousednosti
class Graf {
private:
    // Mapa: ID vrcholu -> Seznam hran (sousedů)
    std::map<int, std::vector<Hrana>> seznamSousedu;

public:
    // Přidání orientované hrany (pro neorientovaný přidejte i obráceně)
    void pridejHranu(int od, int do_vrcholu, int vaha = 1) {
        seznamSousedu[od].push_back({do_vrcholu, vaha});
        // Pokud by graf nebyl orientovaný, odkomentujte řádek níže:
        // seznamSousedu[do_vrcholu].push_back({od, vaha});
    }

    // --- BFS: Prohledávání do šířky ---
    void BFS(int start) {
        std::cout << "--- BFS (Start: " << start << ") ---" << std::endl;
        
        std::map<int, bool> navstiveno;
        std::queue<int> fronta;

        navstiveno[start] = true;
        fronta.push(start);

        while (!fronta.empty()) {
            int aktualni = fronta.front();
            fronta.pop();
            std::cout << aktualni << " ";

            // Projdi sousedy
            for (const auto& hrana : seznamSousedu[aktualni]) {
                if (!navstiveno[hrana.cil]) {
                    navstiveno[hrana.cil] = true;
                    fronta.push(hrana.cil);
                }
            }
        }
        std::cout << std::endl;
    }

    // --- DFS: Prohledávání do hloubky (Rekurzivně) ---
    void DFS(int start) {
        std::cout << "--- DFS (Start: " << start << ") ---" << std::endl;
        std::map<int, bool> navstiveno;
        DFS_rekurze(start, navstiveno);
        std::cout << std::endl;
    }

    void DFS_rekurze(int vrchol, std::map<int, bool>& navstiveno) {
        navstiveno[vrchol] = true;
        std::cout << vrchol << " ";

        for (const auto& hrana : seznamSousedu[vrchol]) {
            if (!navstiveno[hrana.cil]) {
                DFS_rekurze(hrana.cil, navstiveno);
            }
        }
    }

    // --- Dijkstrův algoritmus: Nejkratší cesta ---
    void Dijkstra(int start, int cil) {
        std::cout << "--- Dijkstra (Z " << start << " do " << cil << ") ---" << std::endl;

        // Mapa vzdáleností: vrchol -> nejmenší nalezená vzdálenost
        std::map<int, int> vzdalenosti;
        // Mapa předchůdců pro rekonstrukci cesty
        std::map<int, int> predchudci;

        // Inicializace vzdáleností na "nekonečno"
        for (auto const& [vrchol, hrany] : seznamSousedu) {
            vzdalenosti[vrchol] = std::numeric_limits<int>::max();
        }
        // Přidáme i cílový vrchol do mapy, pokud tam není (nemá odchozí hrany)
        if (vzdalenosti.find(cil) == vzdalenosti.end()) {
             vzdalenosti[cil] = std::numeric_limits<int>::max();
        }

        vzdalenosti[start] = 0;

        // Prioritní fronta: ukládá páry {vzdalenost, vrchol}, seřazené od nejmenší vzdálenosti
        // Používáme 'greater', aby nahoře byla nejmenší hodnota
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
        
        pq.push({0, start});

        while (!pq.empty()) {
            int aktualniVzdalenost = pq.top().first;
            int aktualniVrchol = pq.top().second;
            pq.pop();

            // Optimalizace: Pokud jsme našli delší cestu k již uzavřenému vrcholu, ignorujeme ji
            if (aktualniVzdalenost > vzdalenosti[aktualniVrchol]) continue;

            if (aktualniVrchol == cil) break; // Našli jsme cíl

            // Relaxace hran
            for (const auto& hrana : seznamSousedu[aktualniVrchol]) {
                int novyVrchol = hrana.cil;
                int vahaHrany = hrana.vaha;

                if (vzdalenosti[aktualniVrchol] + vahaHrany < vzdalenosti[novyVrchol]) {
                    vzdalenosti[novyVrchol] = vzdalenosti[aktualniVrchol] + vahaHrany;
                    predchudci[novyVrchol] = aktualniVrchol;
                    pq.push({vzdalenosti[novyVrchol], novyVrchol});
                }
            }
        }

        // Výpis výsledku
        if (vzdalenosti[cil] == std::numeric_limits<int>::max()) {
            std::cout << "Cesta neexistuje." << std::endl;
        } else {
            std::cout << "Nejkratší vzdálenost: " << vzdalenosti[cil] << std::endl;
            
            // Rekonstrukce cesty
            std::cout << "Cesta: ";
            std::vector<int> cesta;
            for (int v = cil; v != start; v = predchudci[v]) {
                cesta.push_back(v);
            }
            cesta.push_back(start);
            std::reverse(cesta.begin(), cesta.end());
            
            for (size_t i = 0; i < cesta.size(); ++i) {
                std::cout << cesta[i] << (i < cesta.size() - 1 ? " -> " : "");
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    Graf g;

    /* Definice grafu (orientovaný, s váhami):
       (0) --4--> (1)
        |          |
        2          1
        v          v
       (2) --3--> (3)
        |        ^ |
        |       /  |
        5      1   2
        |     /    |
        v    /     v
       (4) -/     (5)
    */

    g.pridejHranu(0, 1, 4);
    g.pridejHranu(0, 2, 2);
    g.pridejHranu(1, 3, 1); // Cesta 0->1->3 (délka 5)
    g.pridejHranu(2, 3, 3); // Cesta 0->2->3 (délka 5)
    g.pridejHranu(2, 4, 5);
    g.pridejHranu(4, 3, 1); // Zkrátka přes 4: 0->2->4->3 (délka 2+5+1 = 8)
    g.pridejHranu(3, 5, 2);

    // Ukázka BFS (ignoruje váhy, bere to jako počty kroků)
    g.BFS(0);

    // Ukázka DFS
    g.DFS(0);

    // Ukázka Dijkstra (hledá nejkratší cestu podle vah)
    // Zkusíme najít cestu z 0 do 5
    g.Dijkstra(0, 5); 
    // Očekáváno: 0 -> 1 -> 3 -> 5 (Vzdálenost: 4 + 1 + 2 = 7)
    // Nebo 0 -> 2 -> 3 -> 5 (Vzdálenost: 2 + 3 + 2 = 7)

    return 0;
}