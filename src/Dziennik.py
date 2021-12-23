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

    def edytuj_przedmiot_ucznia(self, imie, nazwisko, przedmiot, nowy_przedmiot):
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
                self.lista_uczniow[i].edytuj_przedmiot(przedmiot, nowy_przedmiot)
                return 'Edytowano przedmiot ucznia'
        raise ValueError('Brak ucznia o podanych danych')

    def usun_przedmiot_do_ucznia(self, imie, nazwisko, przedmiot):
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
                self.lista_uczniow[i].usun_przedmiot(przedmiot)
                return 'Usunieto przedmiot do ucznia'
        raise ValueError('Nie ma takiego ucznia w bazie')


    def dodaj_ocene_do_przedmiotu_ucznia(self, imie, nazwisko, przedmiot, ocena):
        if type(imie) is not str:
            raise TypeError('Zmienna "imię" musi być typu string')
        if type(nazwisko) is not str:
            raise TypeError('Zmienna "nazwisko" musi być typu string')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(nazwisko) == 0:
            raise ValueError('Nie podano nazwiska')

        for i in range(len(self.lista_uczniow)):
            if self.lista_uczniow[i].imie == imie and self.lista_uczniow[i].nazwisko == nazwisko:
                self.lista_uczniow[i].dodaj_ocene_do_przedmiotu(przedmiot, ocena)
                return 'Dodano ocene do przedmiotu ucznia'
        raise ValueError('Nie ma takiego ucznia w bazie')

    def edytuj_ocene_z_przedmiotu_ucznia(self, imie, nazwisko, przedmiot, id_oceny, nowa_ocena):
        if type(imie) is not str:
            raise TypeError('Zmienna "imię" musi być typu string')
        if type(nazwisko) is not str:
            raise TypeError('Zmienna "nazwisko" musi być typu string')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(nazwisko) == 0:
            raise ValueError('Nie podano nazwiska')

        for i in range(len(self.lista_uczniow)):
            if self.lista_uczniow[i].imie == imie and self.lista_uczniow[i].nazwisko == nazwisko:
                self.lista_uczniow[i].edytuj_ocene_z_przedmiotu(przedmiot, id_oceny, nowa_ocena)
                return 'Edytowano ocene z przedmiotu ucznia'
        raise ValueError('Nie ma takiego ucznia w bazie')


    def dodaj_uwage_do_ucznia(self, imie, nazwisko, uwaga):
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
                self.lista_uczniow[i].dodaj_uwage(uwaga)
                return 'Dodano uwage do ucznia'
        raise ValueError('Nie ma takiego ucznia w bazie')

    def edytuj_uwage_ucznia(self, imie, nazwisko, id_uwagi, nowa_uwaga):
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
                self.lista_uczniow[i].edytuj_uwage(id_uwagi, nowa_uwaga)
                return 'Edytowano uwage ucznia'

        raise ValueError('Brak ucznia o podanych danych')

    def srednia_przedmiotu_ucznia(self, imie, nazwisko, przedmiot):
        if type(imie) is not str:
            raise TypeError('Zmienna "imię" musi być typu string')
        if type(nazwisko) is not str:
            raise TypeError('Zmienna "nazwisko" musi być typu string')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(nazwisko) == 0:
            raise ValueError('Nie podano nazwiska')

        for i in range(len(self.lista_uczniow)):
            if self.lista_uczniow[i].imie == imie and self.lista_uczniow[i].nazwisko == nazwisko:
                return self.lista_uczniow[i].srednia_przedmiotu(przedmiot)
        raise ValueError('Brak ucznia o podanych danych')

    def srednia_ucznia(self, imie, nazwisko):
        if type(imie) is not str:
            raise TypeError('Zmienna "imię" musi być typu string')
        if type(nazwisko) is not str:
            raise TypeError('Zmienna "nazwisko" musi być typu string')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(imie) == 0:
            raise ValueError('Nie podano imienia')
        if len(nazwisko) == 0:
            raise ValueError('Nie podano nazwiska')
        for i in range(len(self.lista_uczniow)):
            if self.lista_uczniow[i].imie == imie and self.lista_uczniow[i].nazwisko == nazwisko:
                return self.lista_uczniow[i].srednia()
        raise ValueError('Brak ucznia o podanych danych')