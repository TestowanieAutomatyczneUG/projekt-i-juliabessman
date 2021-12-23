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

    def wyswietl_liste_uczniow(self):
        return self.lista_uczniow

    def usun_ucznia(self, imie, nazwisko):
        if type(imie) is not str:
            raise TypeError('Zmienna "imię" musi być typu string')
        if type(nazwisko) is not str:
            raise TypeError('Zmienna "nazwisko" musi być typu string')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(nazwisko) == 0:
            raise ValueError('Nie podano nazwiska')

        for i in range(len(self.lista_uczniow)):
            if self.lista_uczniow[i].imie == imie and self.lista_uczniow[i].nazwisko == nazwisko:
                del self.lista_uczniow[i]
                return 'Uczeń o podanych danych został usunięty'
        raise ValueError('Uczeń o podanych danych nie występuje w bazie')

    def edytuj_ucznia(self, imie, nazwisko, nowe_imie, nowe_nazwisko):
        if type(imie) is not str:
            raise TypeError('Zmienna "imię" musi być typu string')
        if type(nowe_imie) is not str:
            raise TypeError('Zmienna "nowe_imię" musi być typu string')
        if type(nazwisko) is not str:
            raise TypeError('Zmienna "nazwisko" musi być typu string')
        if type(nowe_nazwisko) is not str:
            raise TypeError('Zmienna "nowe_nazwisko" musi być typu string')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(nowe_imie) == 0:
            raise ValueError('Nie podano nowego imienia')
        if len(nazwisko) == 0:
            raise ValueError('Nie podano nazwiska')
        if len(nowe_nazwisko) == 0:
            raise ValueError('Nie podano nowego nazwiska')
        for i in range(len(self.lista_uczniow)):
            if self.lista_uczniow[i].imie == imie and self.lista_uczniow[i].nazwisko == nazwisko:
                self.lista_uczniow[i].imie = nowe_imie
                self.lista_uczniow[i].nazwisko = nowe_nazwisko
            return 'Dane ucznia zostały zaktualizowane'
        raise ValueError('Uczeń o podanych danych nie występuje w bazie')

    def dodaj_przedmiot_do_ucznia(self, imie, nazwisko, nowy_przedmiot):
        if type(imie) is not str:
            raise TypeError('Zmienna "imię" musi być typu string')
        if type(nazwisko) is not str:
            raise TypeError('Zmienna "nazwisko" musi być typu string')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(nazwisko) == 0:
            raise ValueError('Nie podano nazwiska')

        for i in range(len(self.lista_uczniow)):
            if self.lista_uczniow[i].imie == imie and self.lista_uczniow[i].nazwisko == nazwisko:
                self.lista_uczniow[i].dodaj_przedmiot(nowy_przedmiot)
                return 'Dodano przedmiot do ucznia'
        raise ValueError('Nie ma takiego ucznia w bazie')

    