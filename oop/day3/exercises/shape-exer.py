import math


class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
    def circumference(self):
        raise NotImplementedError
# Stworzyć klase Shape z metodami kostruktor, area, circumference )
# utworzyc klasy pochodne
# rectange, square, circle
# i odpowiednio je zaimplmentować
class Rectangle(Shape):
    def __init__(self, a, b):
        super ().__init__()
        self.a=a
        self.b=b
    def area (self):
        # super().area()
        return self.a * self.b
    def circumference(self):
        # super().circumference()
        return 2*(self.a + self.b)

class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)

class Circle (Shape):
    pi = math.pi
    def __init__(self, r):
        super ().__init__()
        self.r=r
    def area (self):
        return ((self.r)**2 )*self.pi
    def circumference(self):
        return 2*self.pi*self.r


rec = Rectangle(10,20)
circle=Circle(4)
square=Square(4)
print(rec.circumference())
print(rec.area())
print(square.circumference())

shapes = [Square(4), Rectangle(4,5),Circle(3)]
for shape in shapes:
    print(shape.area(), shape.circumference())