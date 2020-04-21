
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance (self,other_point):
        x_diff= self.x - other_point.x
        y_diff=self.y - other_point.y
        dist=(x_diff**2 + y_diff**2)**0.5
        return dist
    def __eq__(self, other_point):
        return(self.x==other_point.x and self.y==other_point.y)
          #porównywanie wielkości - bez tego bedzie porown adresy
    def __add__(self, other_point):
        x_add = self.x+other_point.x
        y_add = self.y + other_point.y
        return Point(x_add, y_add)

    def __str__(self):
        return f"Point {self.x, self.y}"

    def __sub__(self, other_point):
        x_sub = self.x-other_point.x
        y_sub = self.y - other_point.y
        return Point(x_sub, y_sub)
    def __getitem__(self, index_point):
        if index_point == 0:
            return self.x
        elif index_point == 1:
            return self.y
        else:
            raise IndexError("Wektor ma tylko dwa elementy - nr 0 i 1")


# p_1=Point(5,10)
# p_2=Point(5,10)  #other point
# print(p_1.distance(p_2))
# print(p_1==p_2) #metoda magiczna eq
#
#
# print (p_1 + p_2)  #metoda add 0 magiczna
# print (p_1-p_2)    #metoda sub 0 magiczna
# print(p_1[1])     #metoda magiczna getitem

