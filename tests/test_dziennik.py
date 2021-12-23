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

   

    def tearDown(self):
        self.dziennik = None

