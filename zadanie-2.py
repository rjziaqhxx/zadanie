class Book:
    def __init__(self, tytul, rok, wydawca, gatunek, autor, cena):
        self.__tytul = tytul
        self.__rok = rok
        self.__wydawca = wydawca
        self.__gatunek = gatunek
        self.__autor = autor
        self.__cena = cena

    def getinfo(self):
        print(f'Tytul = {self.__tytul}')
        print(f'Rok - {self.__rok}')
        print(f'Wydawca - {self.__wydawca}')
        print(f'Gatunek - {self.__gatunek}')
        print(f'Autor - {self.__autor}')
        print(f'Cena - {self.__cena}')

    def getinfo_tytul(self):
        print(f'Tytul - {self.__tytul}')

    def getinfo_rok(self):
        print(f'Rok - {self.__rok}')
    
    def getinfo_wydawca(self):
        print(f'Wydawca - {self.__wydawca}')
    
    def getinfo_gatunek(self):
        print(f'Gatunek - {self.__gatunek}')

    def getinfo_autor(self):
        print(f'Autor - {self.__autor}')
    
    def getinfo_cena(self):
        print(f'Cena - {self.__cena}')

    def __str__(self):
        print(f'Tytul = {self.__tytul}')
        print(f'Rok - {self.__rok}')
        print(f'Wydawca - {self.__wydawca}')
        print(f'Gatunek - {self.__gatunek}')
        print(f'Autor - {self.__autor}')
        print(f'Cena - {self.__cena}')

    @classmethod
    def create_from_input(cls):
        tytul = input('Tytul - ')
        rok = int(input('Rok - '))
        wydawca = input('Wydawca - ')
        gatunek = input('Gatunek - ')
        autor = input('Autor - ')
        cena = int(input('Cena - '))
        return cls(tytul, rok, wydawca, gatunek, autor, cena)