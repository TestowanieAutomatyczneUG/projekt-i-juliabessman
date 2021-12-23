class Przedmiot:
    def __init__(self, przedmiot):
        self.przedmiot = przedmiot
        self.oceny_z_przedmiotu = []

    def dodaj_ocene(self, nowa_ocena):
        if type(nowa_ocena) is not int:
            raise TypeError('Podany format oceny jest nieprawidłowy')
        if nowa_ocena< 1 or nowa_ocena > 6:
            raise ValueError('Ocena musi mieścić się w przedziale od 1 do 6')
        self.oceny_z_przedmiotu.append(nowa_ocena)

    def edytuj_ocene(self, id_oceny, nowa_ocena):
        if type(nowa_ocena) is not int:
            raise TypeError('Podany format oceny jest nieprawidłowy')
        if nowa_ocena< 1 or nowa_ocena > 6:
            raise ValueError('Ocena musi mieścić się w przedziale od 1 do 6')

        if type(id_oceny) is not int:
            raise TypeError('Podany format id oceny jest nieprawidłowy')

        if id_oceny < 0 or id_oceny >= len(self.oceny_z_przedmiotu):
            raise ValueError('Id oceny sie nie zgadza')
        self.oceny_z_przedmiotu[id_oceny] = nowa_ocena

    def srednia(self):
        if len(self.oceny_z_przedmiotu) == 0:
            return 0
        return sum(self.oceny_z_przedmiotu) / len(self.oceny_z_przedmiotu)