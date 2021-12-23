import csv

def zapisz_jako_csv(dziennik, test=False):
    plik = 'wyjscie.csv'
    if test is True:
        plik = 'wyjscie-test.csv'
    with open(plik, mode='w') as dziennik_wyjscie:
        e_journal_writer = csv.writer(dziennik_wyjscie, delimiter=',',
                                      quotechar='"', quoting=
                                      csv.QUOTE_MINIMAL)
        uczniowie = dziennik.wyswietl_liste_uczniow()
        e_journal_writer.writerow(['Imie', 'Nazwisko', 'Subjects', 'Warnings'])
        for student in uczniowie:
            subjects = []
            for subject in student.wyswietl_liste_przedmiotow():
                subjects.append((subject.przedmiot, subject.oceny_z_przedmiotu))
            e_journal_writer.writerow([student.imie, student.nazwisko, subjects,
                                       student.lista_uwag])
    return 'Zapisano'
