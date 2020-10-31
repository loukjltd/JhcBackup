#Exercise 08-06
'''
class net182
id 2018100701580049
name vivi
'''
class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if value == '':
            print("Error : name not found")
        else:
            self.__name = value

    @property
    def age(self):
        print("Geting the age")
        return self.__age
    @age.setter
    def age(self, value):
        print("Setting the age")
        if value < 0 or value > 100:
            print("Error - age is wrong")
        else:
            self.__age = value

    def message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I am {1} years old".format(self.__name,self.__age))


sam = Person("Sam",20)
james = Person("James",21)

# sam.age = 144

sam.age =144
print(sam.age)

