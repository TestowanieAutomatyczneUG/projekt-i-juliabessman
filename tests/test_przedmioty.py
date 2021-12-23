import unittest

from parameterized import parameterized, parameterized_class

from src.Przedmiot import Przedmiot


class PrzedmiotTest(unittest.TestCase):
    def setUp(self):
        self.przedmiot = Przedmiot('przedmiot')

    def test_dodaj_nowa_ocene(self):
        file = open("../data/przedmiot_tests")
        for line in file:
            ocena = int(line)
            self.przedmiot.dodaj_ocene(ocena)
        self.assertEqual(len(self.przedmiot.oceny_z_przedmiotu), 3)
        file.close()

    @parameterized.expand([
        (True, TypeError),
        (-1, ValueError)
    ])
   

    def tearDown(self):
        self.przedmiot = None
