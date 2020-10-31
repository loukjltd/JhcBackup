#Net171 tianfeng
class Person:
    def message(self):
        print("Hello")
    def details(self):
        print("My name is {0} and I am {1} years old.".format(self.__name, self.__age))

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            print("error")
        else:
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age > 100:
            print("Error - age is wrong {0}".format(age))
        else:
            self.__age = age

sam = Person("Sam", 20)
print(sam.name)
sam.age = 30
print(sam.age)
sam.age = 144
print(sam.age)
