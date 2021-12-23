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
