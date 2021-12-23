from src.Przedmiot import Przedmiot


class Uczen:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.lista_przedmiotow = []
        self.lista_uwag = []

    def dodaj_przedmiot(self, nowy_przedmiot):
        if type(nowy_przedmiot) is not str:
            raise TypeError('Zmienna "nowy_przedmiot" musi być typu string')

        if len(nowy_przedmiot) == 0:
            raise ValueError('Nie podano przedmiotu, który chcemy przypisać')

        przedmiot = Przedmiot(nowy_przedmiot)
        self.lista_przedmiotow.append(przedmiot)