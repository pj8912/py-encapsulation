#private 

class Base:
    def __init__(self):
        self.a = "john"
        self.__c = "john"



class Derived(Base):

    def __init__(self):

        Base.__init__(self)
        print(self.__c)



obj1 = Base()
print(obj1.a)
print("\n")
print("This throws error!!")
obj2= Derived()
print(obj2.__c)
