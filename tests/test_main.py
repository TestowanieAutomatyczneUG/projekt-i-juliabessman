import os
import unittest
from unittest.mock import patch

from hamcrest import *

from src.Dziennik import Dziennik
from src.main import zapisz_jako_csv, pobierz_csv


class MainTest(unittest.TestCase):

    
    def tearDown(self) -> None:
        self.dziennik = None
