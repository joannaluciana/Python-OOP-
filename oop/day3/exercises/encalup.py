class MyClass:
    _protected_class_attribute = "PortClassAttr"
    normal_attribute = "NormalAttribute"


    def __init__(self):
        self.normal_attribute = None
        self._protected_attribute = None #atrybut chroniony prze podłoge

    def normal_method(self):
        self._protected_method()
        print(f"invoked normal method111{self._protected_attribute}")

    def _protected_method(self):
        print("Invoked Protected Method")

    def get_protected_attribute(self):
        return self._protected_attribute
    def set_protected_attribute(self, new_value):
        self._protected_attribute=new_value





    def public_method(self):
        print("wywołałeś metodę publiczną")
    #
    # def _protected_method(self):
    #     print("wywołałeś metodę chronioną")



    # def private_method ()



x = MyClass()
print(x.normal_attribute)
print(MyClass.normal_attribute)
x.normal_method()
x._protected_method()

x.get_protected_attribute()

x.set_protected_attribute(5) #najpierw metoda set
print(x.get_protected_attribute()) #potem metoda get zwracajaca
x.public_method()

# print(x._protected_attribute) violate OOP encapsulation principle