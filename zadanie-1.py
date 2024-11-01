class Car:
    def __init__(self, model, year, producent, pojemnosc, kolor, cena):
        self.__model = model
        self.__year = year
        self.__producent = producent
        self.__pojemnosc = pojemnosc
        self.__kolor = kolor
        self.__cena = cena
    
    def getinfo(self):
        print(f'Model - {self.__model}')
        print(f'Rok - {self.__year}')
        print(f'Producent - {self.__producent}')
        print(f'Pojemnosc - {self.__pojemnosc}')
        print(f'Kolor - {self.__kolor}')
        print(f'Cena - {self.__cena}')

    def getinfo_model(self):
        print(f'Model - {self.__model}')

    def getinfo_rok(self):
        print(f'Model - {self.__model}')

    def getinfo_producent(self):
        print(f'Producent - {self.__producent}')

    def getinfo_pojemnosc(self):
        print(f'Pojemnosc - {self.__pojemnosc}')

    def getinfo_kolor(self):
        print(f'Kolor - {self.__kolor}')
    
    def getinfo_cena(self):
        print(f'Cena - {self.__cena}')

    def __str__(self):
        return (f"Model - {self.__model}, Rok - {self.__year}, Producent - {self.__producent}, "
                f"Pojemnosc - {self.__pojemnosc}, Kolor - {self.__kolor}, Cena - {self.__cena}")

    @classmethod
    def create_from_input(cls):
        model = input('Model - ')
        year = int(input('Rok - '))
        producent = input('Producent - ')
        pojemnosc = int(input('Pojemnosc - '))
        kolor = input('Kolor - ')
        cena = int(input('Cena - '))
        return cls(model, year, producent, pojemnosc, kolor, cena)
