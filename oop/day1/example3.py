# def asd (self):
#     pass
import numbers

import self as self


class Konto :
    def __init__(self, stan_poczatkowy, imie,  nazwisko):  #atrybut obiektów
        print('Jestem konstruktorem')
        self .stan = stan_poczatkowy       #pole w klasie. Field
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"""Właściciel {self.imie} {self.nazwisko}
        Stan: {self.stan}
        """

    def wplac (self, kwota):
         self.stan += kwota

    def wyplata (self, kwota ):
        self.stan -= kwota
        return kwota

    def przelew (self, kwota, konto_docel):
        if not isinstance(kwota, int):
            raise Exception ('Kwota nie może być innego typu niż int')
        self. stan -=kwota
        konto_docel.stan+=kwota
    def przelew2 (self,kwota, konto_docel):
        self.wyplata(kwota)
        konto_docel.wplac(kwota)


x=Konto (500, 'Asia', 'Włoskowicz') #tworzony obiekt
x1=Konto (600, 'Kami', 'Kamilka') #tworzony obiekt

x.wplac (1000)
print(x.stan, x.imie)

x.wyplata(500)
print(x.stan, x.imie)

portfel = x.wyplata(500)

print (portfel)

# print(x.stan, x.imie)
# print(x.imie)
# print (x.nazwisko)
#
# print(x1.stan, x1.imie)
# print(x1.imie)
# print (x1.nazwisko)
#
# print(x)
print (x, x1)
x.przelew(500, x1)

print (x, x1)

try:
    x.przelew2('500', x1)
except Exception:
    print(f'Podana kwota "500"jest niepoprawna')

try:
        x.przelew2(500, x1)
except Exception:
    print(f'Podana kwota "500" jest niepoprawna')



print(x)
print(x1)





