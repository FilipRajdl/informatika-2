# Výuka C++ a Pythonu - Materiály k předmětu

Tento repozitář obsahuje výukové materiály a příklady pro předmět zaměřený na **programování v jazycích C++ a Python.**

Kurz pokrývá široké spektrum témat nezbytných pro moderní vývoj aplikací, včetně:

* **Základy programování:** Principy, datové struktury a algoritmy v C++ a Pythonu.
* **Objektově orientované programování:** Zapouzdření, dědičnost a polymorfismus v obou jazycích.
* **Správa paměti v C++:** Práce s ukazateli a dynamickou alokací.
* **Moderní C++:** Využití standardní knihovny (STL).
* **Ekosystém Pythonu:** Práce s balíčky a populárními knihovnami (`requests`, `Flask`, `NumPy`, `Pandas`).
* **Nástroje a technologie:** Git, Docker, REST API.

## Předpoklady
V rámci předmětu projdeme základy nejdůležitějších nástrojů pro moderní vývoj. Vše potřebné pro běžné užívání bude vysvětleno v hodině, nicméně pro hlubší studium jsou zde připraveny doplňující materiály.

* **Git:** Základy verzování. ([Viz 00-predpoklady/git](./00-predpoklady/git/README.md))
* **Docker:** Základy kontejnerizace a Docker Compose. ([Viz 00-predpoklady/docker](./00-predpoklady/docker/README.md))

Dále se předpokládá základní algoritmické myšlení a znalost základů programování z předchozích semestrů.

## Struktura repozitáře

Materiály jsou organizovány do číslovaných adresářů podle témat probíraných na přednáškách a cvičeních:

* [`00-predpoklady/`](./00-predpoklady/): Materiály a příklady k Gitu a Dockeru.
* [`01-uvodni-hodina/`](./01-uvodni-hodina/README.md): Úvodní informace k předmětu, cíle, hodnocení, harmonogram. **Začněte zde!**
* [`02-zaklady-cpp/`](./02-zaklady-cpp/README.md): Materiály k základům jazyka C++.
* [`03-pokrocile-cpp/`](./03-pokrocile-cpp/README.md): Materiály k OOP, šablonám a STL v C++.
* [`04-zaklady-python/`](./04-zaklady-python/README.md): Materiály k základům jazyka Python.
* [`06-algoritmizace/`](./06-algoritmizace/README.md): Materiály shrnující klíčové koncepty algoritmizace.
* <!--
* [`05-pokrocile-python/`](./05-pokrocile-python/README.md): Materiály k OOP a knihovnám v Pythonu. -->

*(Struktura se může v průběhu semestru mírně upravovat)*

## Jak začít?

1.  Projděte si informace v adresáři [`01-uvodni-hodina/`](./01-uvodni-hodina/README.md).
2.  V sekci [`00-predpoklady/`](./00-predpoklady/README.md). Naleznete materiály pro hlubší studium Gitu a Dockeru. Především je nutné mít nainstalovaný a funkční Docker a Docker Compose.
3.  Celé vývojové prostředí pro tento kurz je připraveno jako Dev Container pro VS Code, který využívá Docker. Toto předkonfigurované prostředí vám automaticky připraví kontejnery pro vývoj v C++ i Pythonu, čímž se zcela zjednoduší nastavení. Podrobnější instrukce ke spuštění naleznete v úvodní hodině.
4.  Postupujte podle materiálů v jednotlivých číslovaných adresářích a dle aktuálního harmonogramu výuky.

## Používané nástroje (shrnutí)

* **Verzování:** Git
* **Kontejnerizace:** Celý repozitář je navržen pro běh v jednotném Docker Compose prostředí, které zajišťuje konzistentní nástroje pro C++ i Python.
* **IDE/Editor:** Doporučeno VS Code
* **Kompilátory a interprety:** g++/clang++ pro C++, interpret Pythonu 3.x.
* **Python nástroje:** `pip`, `Jupyter Notebook`.

## Projekty

Projekty tvoří klíčovou součást hodnocení. V průběhu semestru budete pracovat na několika menších či jednom větším projektu, kde si prakticky vyzkoušíte probírané technologie. Témata projektů budou navrhována a schvalována na začátku každého bloku, s pravidelnými prezentacemi postupu.

## Dotazy a problémy

Pokud narazíte na problém s materiály nebo budete mít dotaz, využijte prosím domluvené komunikační kanály (MS Teams, email). Pokud máte návrh na vylepšení nebo opravu materiálů, budu rád, pokud navrhnete změnu přímo v tomto repozitáři formou Pull Requestu.
