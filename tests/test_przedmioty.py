import unittest

from parameterized import parameterized, parameterized_class

from src.Przedmiot import Przedmiot


class PrzedmiotTest(unittest.TestCase):
    def setUp(self):
        self.przedmiot = Przedmiot('przedmiot')



    def tearDown(self):
        self.przedmiot = None
