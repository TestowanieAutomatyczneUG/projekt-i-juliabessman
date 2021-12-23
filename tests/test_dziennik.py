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

   