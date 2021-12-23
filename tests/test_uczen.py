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

    @parameterized.expand([
        (True, 'Przedmiot', TypeError),
        ('Przedmiot', True, TypeError),
        ('Przedmiot', '', ValueError),
        ('', 'Przedmiot', ValueError),
        ('Przedmiot', 'Przedmiot', ValueError),
        ('Przedmiot', 'Przedmiot1', ValueError),
    ])
    def test_edytuj_przedmiot(self):
        self.uczen.dodaj_przedmiot('Niemiecki')
        assert_that(self.uczen.edytuj_przedmiot('Niemiecki', 'Francuski')).is_equal_to_ignoring_case('Zmieniono PRZEDMIOT')

    def test_edytuj_przedmiot_error(self, przedmiot, nowy_przedmiot, blad):
        self.assertRaises(blad, self.uczen.edytuj_przedmiot, przedmiot, nowy_przedmiot)

    def test_usun_przedmiot(self):
        self.uczen.dodaj_przedmiot('Niemiecki')
        assert_that(self.uczen.usun_przedmiot('Niemiecki')).contains_ignoring_case('Usu', 'PRZED')


    def test_usun_przedmiot_error_1(self):
        assert_that(self.uczen.usun_przedmiot).raises(TypeError).when_called_with(False)

    def test_usun_przedmiot_error_2(self):
        assert_that(self.uczen.usun_przedmiot).raises(ValueError).when_called_with('')

    def test_usun_przedmiot_error_3(self):
        assert_that(self.uczen.usun_przedmiot).raises(ValueError).when_called_with('Niemiecki')

    def test_dodaj_ocene_do_przedmiotu(self):
        self.uczen.dodaj_przedmiot('Niemiecki')
        assert_that(self.uczen.dodaj_ocene_do_przedmiotu('Niemiecki', 3)).contains_duplicates()

    @parameterized.expand([
        (True, 2, TypeError),
        ('', 2, ValueError),
        ('Niemiecki', 3, ValueError)
    ])
    def test_dodaj_ocene_do_przedmiotu_error(self, przedmiot, ocena, blad):
        self.assertRaises(blad, self.uczen.dodaj_ocene_do_przedmiotu, przedmiot, ocena)


    def test_edytuj_ocene_z_przedmiotu(self):
        self.uczen.dodaj_przedmiot('Niemiecki')
        self.uczen.dodaj_ocene_do_przedmiotu('Niemiecki', 2)
        assert_that(self.uczen.edytuj_ocene_z_przedmiotu('Niemiecki', 0, 3)).is_in('Edytowano ocene z przedmiotu', 'Usuniete ocene z przedmiotu')

    @parameterized.expand([
        (True, 0, 2, TypeError),
        ('', 0, 2, ValueError),
        ('Niemiecki', 0, 3, ValueError)
    ])

    def test_edytuj_ocene_z_przedmiotu_error(self, przedmiot, id_oceny, ocena, blad):
        self.assertRaises(blad, self.uczen.edytuj_ocene_z_przedmiotu, przedmiot, id_oceny, ocena)

    @parameterized.expand([
        (True, 0, 2, TypeError),
        ('', 0, 2, ValueError),
        ('Niemiecki', 0, 3, ValueError)
    ])
    # custom matcher
    def test_dodaj_uwage(self):
        self.uczen.dodaj_uwage('Uwaga jest')
        assert_that_hamcrest(True, is_(custom_matcher(self.uczen.lista_uwag[0])))

    @parameterized.expand([
        (True, TypeError),
        ('', ValueError),
    ])

    def test_dodaj_uwage_error(self, uwaga, blad):
        self.assertRaises(blad, self.uczen.dodaj_uwage, uwaga)

    def test_edytuj_uwage(self):
        self.uczen.dodaj_uwage('Uwaga')
        self.uczen.edytuj_uwage(0, 'Nowa Uwaga')
        assert_that(self.uczen.lista_uwag[0]).is_not_equal_to('Uwaga')

    @parameterized.expand([
        (0, False, TypeError),
        (0, '', ValueError),
        (False, 'Nowa uwaga', TypeError),
        (-1, 'Nowa uwaga', ValueError)
    ])
    def test_edytuj_uwage_error(self, id_uwagi, uwaga, blad):
        self.assertRaises(blad, self.uczen.edytuj_uwage, id_uwagi, uwaga)

    def test_srednia_przedmiotu(self):
        self.uczen.dodaj_przedmiot('Niemiecki')
        self.uczen.dodaj_ocene_do_przedmiotu('Niemiecki', 5)
        self.uczen.dodaj_ocene_do_przedmiotu('Niemiecki', 3)
        assert_that(self.uczen.srednia_przedmiotu('Niemiecki')).is_in(4,-4)

    def test_srednia_przedmiotu_error_1(self):
        assert_that(self.uczen.srednia_przedmiotu).raises(TypeError).when_called_with(False)

    def test_srednia_przedmiotu_error_2(self):
        assert_that(self.uczen.srednia_przedmiotu).raises(ValueError).when_called_with('')

    def test_srednia_przedmiotu_error_nie_istnieje(self):
        assert_that(self.uczen.srednia_przedmiotu).raises(ValueError).when_called_with('Niemiecki')


    def test_srednia_ucznia(self):
        self.uczen.dodaj_przedmiot('Niemiecki')
        self.uczen.dodaj_ocene_do_przedmiotu('Niemiecki', 5)
        self.uczen.dodaj_ocene_do_przedmiotu('Niemiecki', 3)

        self.uczen.dodaj_przedmiot('Francuski')
        self.uczen.dodaj_ocene_do_przedmiotu('Francuski', 2)
        self.uczen.dodaj_ocene_do_przedmiotu('Francuski', 4)

        assert_that(self.uczen.srednia()).is_equal_to(3.5)

    def test_srednia_ucznia_0(self):
        assert_that(self.uczen.srednia()).is_zero()

    def tearDown(self):
        self.uczen = None
