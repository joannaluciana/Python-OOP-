import csv
from functools import reduce



class CsvReader:

    # __init__ wczytanie pliku csv poprzez podanie scieżki + stworzenie 2 pól _path, _sheet (2d list)
    # get_sheet zwórcenie sheeta

    def __init__(self, filepath):
        self._path = filepath
        with open(filepath) as file:
            temp_l=csv.reader(file)  # czytacz CSV
            self._sheet = list(temp_l)[1:]  # wczytane bez pierwszej linijki bez list bedzie ioo wrapper - zwraca wszystko poza pierwszym elem listy

    def get_sheet(self):
        return self._sheet




class SheetCalculator:
    def __init__(self,content):
        self._content=content
    def count_row(self):
        return len(self._content)

    def get_row(self, num):
        return self._content[num]

    def count_col (self,num):
        return len(self._content[1])



    def get_colum (self, column):
        return list (x[column] for  x in self._content)

    # x[number] for x in self._sheet

    def sum_column (self, column):
        return reduce (lambda el1, el2: int(el1)+ int(el2),  self.get_colum(column))
    def mul_column (self, column):
        return reduce (lambda el1, el2: int(el1)*int(el2), self.get_colum(column))
    def mean_column (self,column):
        return self.sum_column(column)/self.count_row()



    def apply_function_on_column(self,number, function):
        return reduce(function, self. get_column(number))









#  __init__ pobranie CsvReadera i wczytanie sheeta do własnego pola
# get_column
# get_row
# count_column
# count_row
# sum_column
# mul_column
# mean_column
# apply_function_on_column
file1 = CsvReader('./data.csv')  #-- pobranie z wczesniejszej metody rozebrany plik

content = file1.get_sheet()

l1 = SheetCalculator(content)
print(l1.count_row())

sheet_calculator = SheetCalculator(CsvReader('./data.csv').get_sheet())
    print(sheet_calculator.apply_function_on_column(0, lambda x, y: x +y ))
    print (sheet_calculator.apply_function_on_column(0,lambda x,y: int(y)))

print(l1.get_row(1))
print(l1.count_col(1))
print(l1.get_colum(1))
print(l1.sum_column(0))
print (l1.mul_column(0))
print(l1.mean_column(0))

