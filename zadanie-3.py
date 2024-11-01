class Stadium:
    def __init__(self, nazwa, data, kraj, miasto, liczba):
        self.__nazwa = nazwa
        self.__data = data
        self.__kraj = kraj
        self.__miasto = miasto
        self.__liczba = liczba

    def getinfo(self):
        print(f'Nazwa stadionu - {self.__nazwa}')
        print(f'Data otwarcia - {self.__data}')
        print(f'Kraj - {self.__kraj}')
        print(f'Miasto - {self.__miasto}')
        print(f'Liczba miejsc siedzacych - {self.__liczba}')
    
    def getinfo_nazwa(self):
        print(f'Nazwa stadionu - {self.__nazwa}')

    def getinfo_data(self):
        print(f'Data otwarcia - {self.__data}')
    
    def getinfo_kraj(self):
        print(f'Kraj - {self.__kraj}')
    
    def getinfo_miasto(self):
        print(f'Miasto - {self.__miasto}')

    def getinfo_liczba(self):
        print(f'Liczba miejsc siedzacych - {self.__liczba}')

    def __str__(self):
        print(f'Nazwa stadionu - {self.__nazwa}')
        print(f'Data otwarcia - {self.__data}')
        print(f'Kraj - {self.__kraj}')
        print(f'Miasto - {self.__miasto}')
        print(f'Liczba miejsc siedzacych - {self.__liczba}')

    @classmethod
    def create_from_input(cls):
        nazwa = input('Nazwa - ')
        data = input('Data - ')
        kraj = input('Kraj - ')
        miasto = input('Miasto - ')
        liczba = input('Liczba miejsc siedzacych - ')
        return cls(nazwa, data, kraj, miasto, liczba)