from biblioteki import pliki as p
from biblioteki import zapotrzebowanie as z
from biblioteki import menu as m
from biblioteki import sortuj as s
from biblioteki import watki as w
from datetime import datetime
import threading
import os

def main():
    # odczyt danych na temat potraw
    pola, dane = p.zczytaj_dane('dane.csv')
    liczba_wszystkich = len(dane)

    # odczyt zapisanych danych
    if not os.path.isfile('zapotrzebowanie.csv') or not os.path.isfile('data.txt'):
        waga, wzrost, wiek, plec, aktywnosc = m.zapytaj_o_dane()
        dzienne_zapotrzebowanie = z.Zapotrzebowanie(waga, wzrost, wiek, plec, aktywnosc)
        dzienna_suma = z.Zapotrzebowanie()
        aktualna_data = datetime.now().strftime("%d:%m:%Y")
    else:
        dzienne_zapotrzebowanie, dzienna_suma, aktualna_data = p.odczyt_zapisanych_danych('data.txt', 'zapotrzebowanie.csv')

    if os.path.isfile('preferencje.csv'):
        jest_weganinem, jest_wegetarianinem = p.odczyt_preferencji('preferencje.csv')
    else:
        jest_weganinem, jest_wegetarianinem = m.dokladne_preferencje()

    dane = m.modyfikuj_dane(dane, 'dane.csv', liczba_wszystkich, jest_weganinem, jest_wegetarianinem)
    lista_watku = [aktualna_data, True]
    T = threading.Thread(target=w.run, args=(lista_watku, dzienna_suma))
    T.start()
    s.quickSort(dane, 0, len(dane) - 1, 0, s.letter_greater, s.letter_less)
    m.menu(pola, dane, dzienne_zapotrzebowanie, dzienna_suma, lista_watku, liczba_wszystkich, jest_weganinem, jest_wegetarianinem, 'dane.csv', 'zapotrzebowanie.csv', 'data.txt', 'preferencje.csv')

if __name__=='__main__': main()