#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <vector>
#include <set> // Pro unikátní seznam postav
#include <iterator>

// Funkce pro načtení souboru (z vašeho zadání)
std::string nactiSoubor(const std::string& nazev) {
    std::ifstream soubor(nazev);
    if (!soubor.is_open()) {
        std::cerr << "CHYBA: Nelze otevrit soubor '" << nazev << "'." << std::endl;
        return "";
    }
    return std::string((std::istreambuf_iterator<char>(soubor)),
                        std::istreambuf_iterator<char>());
}

// 1. Úkol: Analyzuj Roboty
void analyzujRoboty(const std::string& text) {
    std::cout << "--- ANALYZA SLOVA ROBOT ---" << std::endl;
    
    // \b       = hranice slova (aby to nebralo slova uprostřed jiných)
    // Robot    = hledaný kořen (citlivé na velikost písmen)
    // \w* = libovolný počet dalších znaků slova (písmena, číslice, podtržítko)
    std::regex re(R"(\bRobot\w*)");
    
    auto zacatek = std::sregex_iterator(text.begin(), text.end(), re);
    auto konec = std::sregex_iterator();
    
    // std::distance spočítá počet prvků mezi iterátory
    std::cout << "Pocet vyskytu slov s korenem 'Robot': " 
              << std::distance(zacatek, konec) << std::endl;
    std::cout << std::endl;
}

void najdiPrimouRec(const std::string& text) {
    std::cout << "--- PRVNICH 5 VET V UVOZOVKACH ---" << std::endl;
    
    // OPRAVA: Přidali jsme "rx" mezi uvozovku a závorku: R"rx(...)rx"
    // Tím říkáme: text končí až ve chvíli, kdy najdeš sekvenci )rx"
    std::regex re(R"rx("([^"]+)")rx");
    
    auto it = std::sregex_iterator(text.begin(), text.end(), re);
    auto end = std::sregex_iterator();
    
    int pocitadlo = 0;
    for (; it != end && pocitadlo < 5; ++it, ++pocitadlo) {
        std::smatch shoda = *it;
        std::cout << pocitadlo + 1 << ". " << shoda[1].str() << std::endl;
    }
    std::cout << std::endl;
}

// 3. Úkol: Najdi letopočty
void najdiLetopocty(const std::string& text) {
    std::cout << "--- NALEZENE LETOPOCTY ---" << std::endl;
    
    // \b       = hranice slova
    // \d{4}    = přesně 4 číslice
    // \b       = hranice slova
    std::regex re(R"(\b\d{4}\b)");
    
    auto it = std::sregex_iterator(text.begin(), text.end(), re);
    auto end = std::sregex_iterator();
    
    // Použijeme set, abychom vypsali každý rok jen jednou (pokud jich je v textu víc stejných)
    std::set<std::string> roky;
    
    for (; it != end; ++it) {
        roky.insert(it->str());
    }
    
    if (roky.empty()) {
        std::cout << "Zadne letopocty nenalezeny." << std::endl;
    } else {
        for (const auto& rok : roky) {
            std::cout << rok << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

// 4. Úkol: Najdi postavy
void najdiPostavy(const std::string& text) {
    std::cout << "--- POSTAVY (DLE SCENARE) ---" << std::endl;

    // (?:^|\n)     = Začátek textu NEBO nový řádek (neukládáme do skupiny)
    // \s* = Možné bílé znaky (mezery) na začátku
    // ([A-ZÁ-Ž ]+) = CAPTURE GROUP 1: Velká písmena (vč. českých odhadem) a mezery
    // [\.:]        = Následuje tečka nebo dvojtečka
    
    // Poznámka: Rozsah A-Ž v C++ regexu závisí na kódování, pro jednoduchost zde
    // předpokládáme standardní velká písmena. Pro robustní češtinu je třeba wstring.
    std::regex re(R"((?:^|\n)\s*([A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+)[\.:])");

    auto it = std::sregex_iterator(text.begin(), text.end(), re);
    auto end = std::sregex_iterator();

    std::set<std::string> postavy;

    for (; it != end; ++it) {
        std::smatch shoda = *it;
        // Získáme jméno (první závorka)
        std::string jmeno = shoda[1].str();
        
        // Filtrace: Chceme jen slova delší než 1 znak (abychom vyloučili např. iniciály nebo číslování A.)
        if (jmeno.length() > 1) {
            postavy.insert(jmeno);
        }
    }

    for (const auto& postava : postavy) {
        std::cout << postava << std::endl;
    }
    std::cout << std::endl;
}

int main() {
    std::cout << "Nacitam knihu..." << std::endl;
    std::string text = nactiSoubor("kniha.txt");
    
    if (text.empty()) {
        return 1; 
    }

    std::cout << "Kniha nactena. Velikost: " << text.length() << " znaku.\n" << std::endl;

    // Spuštění analýz
    analyzujRoboty(text);
    najdiPrimouRec(text);
    najdiLetopocty(text);
    najdiPostavy(text);

    return 0;
}