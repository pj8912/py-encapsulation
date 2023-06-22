#Encapsulation in python

#protected

class Base:
    def __init__(self):
        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self._a=3



obj1 = Derived()
obj2 = Base()


print("Accessing protected member of obj1: ", obj1._a)
print("*"*30)
print("Accessing protected member of obj2: ", obj2._a)

