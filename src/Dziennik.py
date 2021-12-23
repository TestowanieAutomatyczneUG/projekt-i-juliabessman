from src.Uczen import Uczen


class Dziennik:
    def __init__(self):
        self.lista_uczniow = []

    def dodaj_ucznia(self, imie, nazwisko):
        if type(imie) is not str:
            raise TypeError('Zmienna "imię" musi być typu string')
        if type(nazwisko) is not str:
            raise TypeError('Zmienna "nazwisko" musi być typu string')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(nazwisko) == 0:
            raise ValueError('Nie podano nazwiska')
        for j in range(len(self.lista_uczniow)):
            if self.lista_uczniow[j].imie == imie and self.lista_uczniow[j].nazwisko == nazwisko:
                raise ValueError('Uczeń o podanych danych już istnieje')

        uczen = Uczen(imie, nazwisko)

        self.lista_uczniow.append(uczen)
