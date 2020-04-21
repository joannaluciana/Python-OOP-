import csv
from functools import reduce

class Csvread:

    def __init__(self, fpath):
        self._path=fpath
        with open (fpath) as file:
            read_f=csv.reader(file)
            print(read_f)  #<_csv.reader object at 0x000002A53144DF40>

            self._sheet = list(read_f)[1:] #utworzenie listy


    def get_sheet(self):
        return self._sheet

class Csvcalc:
    def __init__(self, cont):
        self._cont=cont
    def row_count(self):
        return len(self._cont)
    def get_row (self, row_no):
        return self._cont[row_no]
    def col_count (self):
        return len(self._cont[1])
    def get_colum (self,no_col):
        return list (x[no_col] for x in self._cont)
    def sum_col (self,col_no):
        return reduce(lambda x, y: x+y, self.get_colum(col_no))

    def mul_col(self, col_no):
        return sum(lambda x,y: x*y, self.get_colum(col_no))





csv1= Csvread('./data.csv')
print(csv1) #<__main__.Csvread object at 0x000002A5312B4040>




