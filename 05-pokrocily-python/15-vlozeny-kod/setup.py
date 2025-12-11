from setuptools import setup, Extension

# Definice modulu
# name: název balíčku v Pythonu
# sources: seznam C/C++ souborů
module = Extension('fastprime', sources=['fastprime.c'])

setup(
    name='fastprime',
    version='1.0',
    description='Demonstrace C rozšíření pro Python',
    ext_modules=[module]
)