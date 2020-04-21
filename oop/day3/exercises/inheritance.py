# class BaseClass:
#     pass
# class DeriveredClass(BaseClass):
#     pass
class Base:
    def __init__(self):
        self.name = "Base"
        print('I am base class')
    def fun(self):
        print(f"Base class fun {self.name}")
b=Base()
b.fun()
print('000000000000000000000000000000000000000')

class Derived1(Base):
    def __init__(self):
        super().__init__() #Constructor invocation of base class
        self.name="Derived"
        print("I'm derived class one")
    def not__so__funny (self):
        print('Name d is not funny')

class Derived2(Base):
    def __init__(self):
        super().__init__()
        print("I am derived class Two")

    def fun(self):
        print(f"Overriden method")


d = Derived1()
d.fun()
d.not__so__funny()


derrived2 = Derived2()
derrived2.fun()
