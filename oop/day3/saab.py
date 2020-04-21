# Napisz program który będzie składal się z 3 klas.
# Pierwsza klasa nazwana będzie `Vehicle` i będzie klasą bazową
# dla pozostałych tj. `Bus`, `Truck`.
# Klasa bazowa będzie posiadać prywatne atrybuty takie jak:
# _driving_cost -> reprezentujący składową kosztu wykonania metody drive()
# _per_passenger_cost -> reprezentujacy składową kosztu wykonania metody drive()
# pomnożoną przez ilośc pasażerów
# _passenger_limit -> limit osób mogących znaleść się w pojeździe
# _passenger_no -> ilość osób mogących znaleść się w pojeździe musi być
# zawsze większa od jeden
# _fuel_tank -> reprezentujacy obecny poziom paliwa w pojeździe
# Klasa `Vehicle` będzie miała zdefiniowane metody takie jak `drive` ->
# redukuje ilość dostępnego paliwa o `_driving_cost` plus dodatkowo
# `_per_passenger_cost` za każdego pasażera, jeżeli w trakcie ilość paliwa spadnie do zera
# to operacja `drive` się nie udaje i każde kolejne wykonanie operacji drive nie zadziała,
# `check_fuel` -> pokazuje stan paliwa, `find_petrol_station`
# -> wykonuje operacje drive i jeżeli się uda to tankuje paliwo, `check_passenger`
# -> sprawdza ilość pasażerów
# Klasa `Bus` będzie miała zdefiniowaną metodę `take_passager` która będzie dodawać losową liczbę osób (z zakresu 0 do 5) do obecnie znajdujących się w pojeździe
# Klasa `Bus` będzie miała zdefiniowaną metodę `unload_passager`
# która będzie usuwać wszystkich pasażerów
# Klasa `Truck` będzie miała metody `take_cargo`, `unload_cargo`
# które odpwiednio będą losowały wartości float i przypisywały do pola należącego tylko do obieku `Truck` o nazwie `_cargo_weight`.
# Dla metody `drive` w klasie `Truck` wywołana zostanie metoda z `drive`
# z klasy bazowej, a następnie wartość paliwa (_fuel_tank) obniży się o `_cargo_weight` * 0,5
# Niekiedy instrukcja dotycząca tego zadania nie jest kompletna w takim
# momecie należy zapytać sięimport random
import random


class Vehicle2:
    _driving_cost = None
    _per_passenger_cost = None
    _passenger_limit = None
    _passenger_no = None
    _fuel_tank = None
    _fuel_limit = None

    def drive(self):
        self._fuel_tank -= self._driving_cost
        self._fuel_tank -= self._per_passenger_cost * self._passenger_no
        if self._fuel_tank < 0:
            self._fuel_tank = 0
            raise Exception("Warning empty fuel!!")
        print(f'We got plenty of fuel - we are driving {self._fuel_tank}')

    def check_fuel(self):
        return self._fuel_tank

    def passenger_check(self):
        return self._passenger_no

    def find_petrol_station(self):
        self.drive()
        self._fuel_tank = self._fuel_limit

    @staticmethod
    def find_mechanic():
        print('got one in trunk')


class Saab_95(Vehicle2):
    _driving_cost = 150
    _per_passenger_cost = 50
    _passenger_limit = 5
    _passenger_no = 1
    _fuel_tank = 500
    _fuel_limit = 150

    def take_passenger(self):
        self._passenger_no += random.randint(0, 5)

        if self._passenger_no > self._passenger_limit:
            self._passenger_no = self._passenger_limit
            raise Exception('Overloaded!!! Too many people!!!')
        return self._passenger_no

    def unload_passenger(self, _passenger_out):
        self._passenger_out = _passenger_out
        self._passenger_no-= self._passenger_out
        if self._passenger_no < 0:
            self._passenger_no = 1
            raise Exception('All are out!!!')
        return self._passenger_no


saab1 = Saab_95()
saab2 = Saab_95()

saab1.drive()


print(saab1.take_passenger())
print(saab1.unload_passenger(1))
