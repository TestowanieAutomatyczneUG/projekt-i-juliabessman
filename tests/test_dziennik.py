import unittest
from hamcrest import *
from parameterized import parameterized
from src.Dziennik import Dziennik


class DziennikTest(unittest.TestCase):
    def setUp(self):
        self.dziennik = Dziennik()



    def tearDown(self):
        self.dziennik = None

