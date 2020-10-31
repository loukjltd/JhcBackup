#Net171 ZERO
class Person:

    def message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I am {1} years old.".format(self.__name, self.__age))

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == "":
            print("error")
        else:
            self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0 or age > 100:
            print("Error - age is wrong {0}".format(age))
        else:
            self.__age = age

    name = property(get_name, set_name)
    age = property(get_age, set_age)


sam = Person("Sam", 20)
print(sam.name)
sam.age = 30
print(sam.age)
sam.age = 144
print(sam.age)

