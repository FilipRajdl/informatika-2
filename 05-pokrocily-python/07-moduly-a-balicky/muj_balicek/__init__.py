"""
Tento soubor označuje složku 'muj_balicek' jako Python Package (balíček).
Spustí se automaticky, jakmile importujete cokoliv z tohoto balíčku.
"""

print("[LOG] Inicializuji balíček 'muj_balicek'...")

# Můžeme zde nastavit proměnné, které budou přístupné přímo pod jménem balíčku
VERZE = "1.0.0"

# EXPORT API:
# Tímto říkáme: "Když někdo importuje tento balíček, zpřístupni mu tyto funkce přímo."
# Uživatel pak může psát: `muj_balicek.obsah_obdelniku(...)`
# Místo dlouhého: `muj_balicek.geometrie.obsah_obdelniku(...)`

from .geometrie import obsah_obdelniku, obvod_obdelniku, obsah_kruhu

# Definice toho, co se importuje při příkazu `from muj_balicek import *`
__all__ = ["obsah_obdelniku", "obvod_obdelniku", "obsah_kruhu", "VERZE"]