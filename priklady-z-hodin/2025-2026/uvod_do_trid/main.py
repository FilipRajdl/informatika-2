class Student:
    def __init__(self, jmeno:str, rocnik:int, znamky:list[int]):
        self.jmeno:str = jmeno
        self.__rocnik:int = rocnik
        self.__znamky:list[int] = znamky 
        
    @property
    def rocnik(self):
        return f"{self.__rocnik}. ročník"

    @rocnik.setter
    def rocnik(self, rocnik:int):
        if 1<=rocnik<=5:
            self.__rocnik=rocnik
        else:
            raise ValueError
        
    @property
    def znamka(self):
        return self.__znamky[-1]

    @znamka.setter
    def znamka(self, znamka:int):
        if 1<=znamka<=5:
            self.__znamky.append(znamka)
        else:
            raise ValueError
    
    def pridej_znamku(self, znamka:int):
        self.__znamky.append(znamka)
    
    def prumer(self)->float:
        return sum(self.__znamky)/len(self.__znamky)

def funkce():
    """
    Docstring for funkce
    """
    pass

def main():
    s1 = Student("Jakub", 4, [1,2,3,4])
    print(s1.prumer())
    s1.znamka = 4
    print(s1.znamka)
    print(s1.prumer())

if __name__ == "__main__":
    main()