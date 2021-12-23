import os
import unittest
from unittest.mock import patch

from hamcrest import *

from src.Dziennik import Dziennik
from src.main import zapisz_jako_csv, pobierz_csv


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.dziennik = Dziennik()

    def test_zapisz_jako_csv(self):
        self.dziennik.dodaj_ucznia('Julia', 'Bessman')
        self.dziennik.dodaj_przedmiot_do_ucznia('Julia', 'Bessman', 'Niemiecki')
        self.dziennik.dodaj_ocene_do_przedmiotu_ucznia('Julia', 'Bessman', 'Niemiecki', 3)
        assert_that(zapisz_jako_csv(self.dziennik, True), equal_to('Zapisano'))
        os.remove('wyjscie-test.csv')

    @patch('builtins.input', side_effect=['../test.csv'])
    def test_get_from_csv(self, mock_input):
        assert_that(pobierz_csv(self.dziennik), not_none())



    def tearDown(self) -> None:
        self.dziennik = None
