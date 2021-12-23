import unittest

from assertpy import *
from hamcrest import assert_that as assert_that_hamcrest, is_
from parameterized import parameterized

from src.Uczen import Uczen
from tests.matcher import custom_matcher


class UczenTest(unittest.TestCase):
    def setUp(self):
        self.uczen = Uczen('Julia', 'Bessman')

    def test_dodaj_przedmiot(self):
        self.uczen.dodaj_przedmiot('Niemiecki')
        assert_that(self.uczen.lista_przedmiotow).is_not_none()

    def test_dodaj_przedmiot_error_1(self):
        assert_that(self.uczen.dodaj_przedmiot).raises(TypeError).when_called_with(False)

    def test_dodaj_przedmiot_error_2(self):
        assert_that(self.uczen.dodaj_przedmiot).raises(ValueError).when_called_with('')

    def test_wyswietl_liste_przedmiotow(self):
        self.uczen.dodaj_przedmiot('Francuski')
        self.uczen.dodaj_przedmiot('Niemiecki')
        assert_that(self.uczen.wyswietl_liste_przedmiotow()).does_not_contain_duplicates()

    def tearDown(self):
        self.uczen = None
