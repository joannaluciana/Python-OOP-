class Point:
    # statyczne
    _counter = 0

    def __init__(self, x, y):
        Point._counter += 1
        self.x = x
        self.y = y

    def __str__(self):
        return f" Punkt: {self.x}, {self.y} z {self._counter}"

    def __del__(self):
        Point._counter -= 1

    @staticmethod
    def description():
        print("This is 2d point, future work to be done")
    @staticmethod
    def increase_count():
        Point._counter+=1

f_point = Point(10, 20)
s_point = Point(10, 30)
t_point = Point(20, 40)
print(f_point)
print(Point._counter)
print(f_point._counter)

del (f_point)
print(Point._counter)  # -- nie usunelo obiektu
Point.description()
s_point.description()

Point.increase_count()
print()