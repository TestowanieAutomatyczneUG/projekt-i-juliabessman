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


    def tearDown(self):
        self.uczen = None
