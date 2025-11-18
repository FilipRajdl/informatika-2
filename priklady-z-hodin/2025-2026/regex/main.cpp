#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <vector>
#include <iterator>

std::string nactiSoubor(const std::string& nazev) {
    std::ifstream soubor(nazev);
    if (!soubor.is_open()) {
        std::cerr << "CHYBA: Nelze otevrit soubor '" << nazev << "'." << std::endl;
        std::cerr << "Ujistete se, ze jste ho stahli (viz README.md)." << std::endl;
        return "";
    }
    
    // Využijeme iterátory pro načtení celého souboru naraz
    return std::string((std::istreambuf_iterator<char>(soubor)),
                        std::istreambuf_iterator<char>());
}

int main() {
    std::cout << "Nacitam knihu..." << std::endl;
    std::string text = nactiSoubor("kniha.txt");
    
    if (text.empty()) {
        return 1; // Konec programu, chyba
    }

    std::cout << "Kniha nactena. Velikost: " << text.length() << " znaku.\n" << std::endl;

    return 0;
}