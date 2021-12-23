import unittest

from hamcrest import *
from parameterized import parameterized
from src.Dziennik import Dziennik


class DziennikTest(unittest.TestCase):
    def setUp(self):
        self.dziennik = Dziennik()

    def test_dodaj_ucznia(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        assert_that(self.dziennik.lista_uczniow, has_length(1))

    def test_dodaj_ucznia_error_1(self):
        assert_that(calling(self.dziennik.dodaj_ucznia).with_args(True,'Bessman'), raises(TypeError))

    def test_dodaj_ucznia_error_2(self):
        assert_that(calling(self.dziennik.dodaj_ucznia).with_args('Julia', True), raises(TypeError))

    def test_dodaj_ucznia_error_3(self):
        assert_that(calling(self.dziennik.dodaj_ucznia).with_args('', 'Bessman'), raises(ValueError))

    def test_dodaj_ucznia_error_4(self):
        assert_that(calling(self.dziennik.dodaj_ucznia).with_args('Julia', ''), raises(ValueError))

    def test_dodaj_ucznia_error_istnieje(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        assert_that(calling(self.dziennik.dodaj_ucznia).with_args('Julia', 'Bessman'), raises(ValueError))

    def test_wyswietl_liste_uczniow_pusta_lista(self):
        assert_that(self.dziennik.wyswietl_liste_uczniow(), empty())

    def test_wyswietl_liste_uczniow_nie_pusta(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        assert_that(self.dziennik.wyswietl_liste_uczniow()[0].imie, contains_string('Julia'))

    def test_usun_ucznia(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        assert_that(self.dziennik.usun_ucznia('Julia', 'Bessman'), starts_with('Uczeń o podanych'))

    @parameterized.expand([
        (1, 'Bessman', TypeError),
        ('', 'Bessman', ValueError),
        ('Julia', 1, TypeError),
        ('Julia', '', ValueError),
    ])
    def test_usun_ucznia_error(self, imie, nazwisko, blad):
        assert_that(calling(self.dziennik.usun_ucznia).with_args(
            imie, nazwisko
        ), raises(blad))

    def test_usun_ucznia_nie_istnieje(self):
        assert_that(calling(self.dziennik.usun_ucznia).with_args(
            'Julia', 'Bessman'
        ), raises(ValueError))

    def test_edytuj_ucznia(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        assert_that(self.dziennik.edytuj_ucznia('Julia', 'Bessman', 'Julia2', 'Bessman2'), starts_with('Dane ucznia zostały zaktualizowane'))

    def test_edycja_ucznia_imie_nie(self):
        assert_that(calling(self.dziennik.edytuj_ucznia).with_args('', 'Bessman', 'Juliaa', 'Bessmann'),
                    raises(ValueError))
    def test_edycja_ucznia_nowe_imie_nie(self):
        assert_that(calling(self.dziennik.edytuj_ucznia).with_args('Julia', 'Bessman', '', 'Bessmann'),
                    raises(ValueError))
    def test_edycja_ucznia_nazwisko_nie(self):
        assert_that(calling(self.dziennik.edytuj_ucznia).with_args('Julia', '', 'Juliaa', 'Bessmann'), raises(ValueError))

    def test_edycja_ucznia_nowe_nazwisko_nie(self):
        assert_that(calling(self.dziennik.edytuj_ucznia).with_args('Julia', 'Bessman', 'Juliaa', ''),
                    raises(ValueError))

    def test_edycja_ucznia_imie_niestr(self):
        assert_that(calling(self.dziennik.edytuj_ucznia).with_args(3, 'Bessman', 'Juliaa', 'Bessmann'),
                    raises(TypeError))

    def test_edycja_ucznia_nazwisko_niestr(self):
        assert_that(calling(self.dziennik.edytuj_ucznia).with_args('Julia', 3, 'Juliaa', 'Bessmann'), raises(TypeError))

    def test_edycja_ucznia_nowe_nazwisko_niestr(self):
        assert_that(calling(self.dziennik.edytuj_ucznia).with_args('Julia', 'Bessman', 'Juliaa', 3), raises(TypeError))

    def test_edycja_ucznia_nowe_imie_niestr(self):
        assert_that(calling(self.dziennik.edytuj_ucznia).with_args('Julia', 3, 'Juliaa', 'Bessmann'), raises(TypeError))
    def test_dodaj_przedmiot_ucznia(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        assert_that(self.dziennik.dodaj_przedmiot_do_ucznia('Julia', 'Bessman', 'Biologia'),
                    starts_with('Dodano przedmiot'))
    def test_dadaj_przedmiot_ucznia_imie_nie(self):
        assert_that(calling(self.dziennik.dodaj_przedmiot_do_ucznia).with_args('', 'Bessman',  'Biologia'),
                    raises(ValueError))
    def test_dodaj_przedmiot_ucznia_nazwisko_nie(self):
        assert_that(calling(self.dziennik.dodaj_przedmiot_do_ucznia).with_args('Julia', '', 'Biologia'), raises(ValueError))

    def test_dodaj_przedmiot_ucznia_imie_niestr(self):
        assert_that(calling(self.dziennik.dodaj_ucznia).with_args(3,'Bessman', 'Biologia'), raises(TypeError))

    def test_dodaj_przedmiot_ucznia_nazwisko_niestr(self):
        assert_that(calling(self.dziennik.dodaj_przedmiot_do_ucznia).with_args('Julia', 3, 'Biologia'), raises(TypeError))


    def test_edytuj_przedmiot_ucznia(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        self.dziennik.dodaj_przedmiot_do_ucznia('Julia', 'Bessman', 'Biologia')
        assert_that(self.dziennik.edytuj_przedmiot_ucznia('Julia', 'Bessman', 'Biologia', 'Angielski'),
                    starts_with('Edytowano przedmiot'))

    def test_edytuj_przedmiot_ucznia_imie_nie(self):
        assert_that(calling(self.dziennik.edytuj_przedmiot_ucznia).with_args('', 'Bessman', 'Biologia', 'Angielski'),
                    raises(ValueError))

    def test_edytuj_przedmiot_ucznia_nazwisko_nie(self):
        assert_that(calling(self.dziennik.edytuj_przedmiot_ucznia).with_args('Julia', '', 'Biologia', 'Angielski'),
                    raises(ValueError))

    def test_edytuj_przedmiot_ucznia_imie_niestr(self):
        assert_that(calling(self.dziennik.edytuj_przedmiot_ucznia).with_args(3, 'Bessman', 'Biologia', 'Angielski'),
                    raises(TypeError))

    def test_edytuj_przedmiot_ucznia_nazwisko_niestr(self):
        assert_that(calling(self.dziennik.edytuj_przedmiot_ucznia).with_args('Julia', 3, 'Biologia', 'Angielski'),
                    raises(TypeError))

    def test_edytuj_przedmiot_nie_istnieje(self):
        assert_that(calling(self.dziennik.edytuj_przedmiot_ucznia).with_args(
            'Julia', 'Bessman', 0, 'Angielski'
        ), raises(ValueError))

    def test_usun_przedmiot_ucznia(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        self.dziennik.dodaj_przedmiot_do_ucznia('Julia', 'Bessman','Biologia')
        assert_that(self.dziennik.usun_przedmiot_do_ucznia('Julia', 'Bessman', 'Biologia'),
                    starts_with('Usunieto przedmiot'))


    def test_usun_przedmiot_ucznia_imie_nie(self):
        assert_that(calling(self.dziennik.usun_przedmiot_do_ucznia).with_args('', 'Bessman', 'Biologia'),
                    raises(ValueError))

    def test_usun_przedmiot_ucznia_nazwisko_nie(self):
        assert_that(calling(self.dziennik.usun_przedmiot_do_ucznia).with_args('Julia', '', 'Biologia'),
                    raises(ValueError))

    def test_usun_przedmiot_ucznia_imie_niestr(self):
        assert_that(calling(self.dziennik.usun_przedmiot_do_ucznia).with_args(3, 'Bessman', 'Biologia'), raises(TypeError))

    def test_usun_przedmiot_ucznia_nazwisko_niestr(self):
        assert_that(calling(self.dziennik.usun_przedmiot_do_ucznia).with_args('Julia', 3, 'Biologia'),
             raises(TypeError))

    def test_usun_przedmiot_ucznia_nie_istnieje(self):
        assert_that(calling(self.dziennik.usun_przedmiot_do_ucznia).with_args(
            'Julia', 'Bessman', 'Francuski')
            ,
            raises(ValueError))

    def test_dodaj_ocene_ucznia(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        self.dziennik.dodaj_przedmiot_do_ucznia('Julia', 'Bessman', 'Biologia')
        assert_that(self.dziennik.dodaj_ocene_do_przedmiotu_ucznia('Julia', 'Bessman', 'Biologia', 6),
                    starts_with('Dodano ocene'))

    def test_dodaj_ocene_ucznia_imie_nie(self):
        assert_that(calling(self.dziennik.dodaj_ocene_do_przedmiotu_ucznia).with_args('', 'Bessman', 'Biologia', 6),
                    raises(ValueError))

    def test_dodaj_ocene_ucznia_nazwisko_nie(self):
        assert_that(calling(self.dziennik.dodaj_ocene_do_przedmiotu_ucznia).with_args('Julia', '', 'Biologia', 6),
                    raises(ValueError))

    def test_dodaj_ocene_ucznia_imie_niestr(self):
        assert_that(calling(self.dziennik.dodaj_ocene_do_przedmiotu_ucznia).with_args(3, 'Bessman', 'Biologia', 6), raises(TypeError))

    def test_dodaj_ocene_ucznia_nazwisko_niestr(self):
        assert_that(calling(self.dziennik.dodaj_ocene_do_przedmiotu_ucznia).with_args('Julia', 3, 'Biologia', 6),
                    raises(TypeError))

    def test_dodaj_ocene_ucznia_nie_istnieje(self):
        assert_that(calling(self.dziennik.dodaj_ocene_do_przedmiotu_ucznia).with_args(
            'Julia', 'Bessman', 'Francuski', 6)
            ,
            raises(ValueError))

    def test_edytuj_ocene_ucznia(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        self.dziennik.dodaj_przedmiot_do_ucznia('Julia', 'Bessman', 'Biologia')
        self.dziennik.dodaj_ocene_do_przedmiotu_ucznia('Julia', 'Bessman', 'Biologia', 6)
        assert_that(self.dziennik.edytuj_ocene_z_przedmiotu_ucznia('Julia', 'Bessman', 'Biologia', 0, 6),
                    starts_with('Edytowano ocene'))

    def test_edytuj_ocene_ucznia_imie_nie(self):
        assert_that(calling(self.dziennik.edytuj_ocene_z_przedmiotu_ucznia).with_args('', 'Bessman', 'Biologia', 0, 6),
                    raises(ValueError))

    def test_edytuj_ocene_ucznia_nazwisko_nie(self):
        assert_that(calling(self.dziennik.edytuj_ocene_z_przedmiotu_ucznia).with_args('Julia', '', 'Biologia', 0, 6),
                    raises(ValueError))

    def test_edytuj_ocene_ucznia_imie_niestr(self):
        assert_that(calling(self.dziennik.edytuj_ocene_z_przedmiotu_ucznia).with_args(3, 'Bessman', 'Biologia', 0, 6),
                    raises(TypeError))

    def test_edytuj_ocene_ucznia_nazwisko_niestr(self):
        assert_that(calling(self.dziennik.edytuj_ocene_z_przedmiotu_ucznia).with_args('Julia', 3, 'Biologia', 0, 6),
                    raises(TypeError))

    def tearDown(self):
        self.dziennik = None



