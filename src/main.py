from src.Dziennik import Dziennik
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


def pobierz_csv(dziennik):

    #podaj nazwe csv
    file_name = input()
    line_count = 0
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count != 0:
                dziennik.dodaj_ucznia(row[0], row[1])
                dziennik.dodaj_przedmiot_do_ucznia(row[0], row[1], row[2])
                dziennik.dodaj_ocene_do_przedmiotu_ucznia(row[0], row[1], row[2], int(row[3]))
                dziennik.dodaj_uwage_do_ucznia(row[0], row[1], row[4])
            line_count += 1
    return dziennik
