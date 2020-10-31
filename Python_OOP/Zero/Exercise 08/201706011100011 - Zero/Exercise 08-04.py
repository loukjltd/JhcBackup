#Net171 ZERO
class Person:

    def message(self):
        print("Hello")
    def details(self):
        print("My name is {0} and I am {1} years old.".format(self.__name,self.__age))

    def __init__(self,name,age):
        self.__name = name
        self.__age=age

sam=Person("Sam",20 )
James=Person("James",20 )

#print(sam.name)

print(sam._Person__name)