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

    def wyswietl_liste_przedmiotow(self):
        return self.lista_przedmiotow

    def edytuj_przedmiot(self, przedmiot, nowy_przedmiot):
        if type(przedmiot) is not str:
            raise TypeError('Zmienna "nowy_przedmiot" musi być typu string')
        if type(nowy_przedmiot) is not str:
            raise TypeError('Zmienna "nowa_nazwa_przedmiotu" musi być typu string')
        if len(przedmiot) == 0:
            raise ValueError('Nie podano przedmiuotu, który chcemy przypisać')
        if len(nowy_przedmiot) == 0:
            raise ValueError('Nie podano nowej nazwy przedmiuotu')
        if przedmiot == nowy_przedmiot:
            raise ValueError('Nowa nazwa przedmiotu musi być inna niż dotychczasowa')
        for i in range(len(self.lista_przedmiotow)):
            if self.lista_przedmiotow[i].przedmiot == przedmiot:
                self.lista_przedmiotow[i].przedmiot = nowy_przedmiot
                return 'Zmieniono przedmiot'
        raise ValueError('Nie znaleziono przedmiotu')

    def usun_przedmiot(self, przedmiot):
        if type(przedmiot) is not str:
            raise TypeError('Zmienna "nowy_przedmiot" musi być typu string')
        if len(przedmiot) == 0:
            raise ValueError('Nie podano przedmiuotu, który chcemy przypisać')

        for i in range(len(self.lista_przedmiotow)):
            if self.lista_przedmiotow[i].przedmiot == przedmiot:
                del self.lista_przedmiotow[i]
                return 'Usunieto przedmiot'
        raise ValueError('Nie znaleziono przedmiotu')

    def dodaj_ocene_do_przedmiotu(self, przedmiot, ocena):
        if type(przedmiot) is not str:
            raise TypeError('Zmienna "nowy_przedmiot" musi być typu string')
        if len(przedmiot) == 0:
            raise ValueError('Nie podano przedmiuotu, który chcemy przypisać')

        for i in range(len(self.lista_przedmiotow)):
            if self.lista_przedmiotow[i].przedmiot == przedmiot:
                self.lista_przedmiotow[i].dodaj_ocene(ocena)
                return 'Dodano ocene do przedmiotu'
        raise ValueError('Przedmiot nie istnieje')