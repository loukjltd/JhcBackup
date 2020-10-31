


# exercise 08-05
'''
student name: Luis
ID: 201810701580033
class: network182
'''


class Person:
    name = ""
    age= 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print("Getting the name")
        return self.__name

    def set_name(self, value):
        print("Setting the name")
        if value=="":
            print("Error - name is wrong")
        else:
                self.__age = value

    def get_age(self):
        print("Getting the age")
        return self.__age

    def set_age(self, value):
        print("Setting the age")
        if value < 0 or value > 100:
            print("Error - age is wrong")
        else:
            self.__age = value

    age = property(get_age, set_age)
    name = property(get_name, set_name)
sam=Person("Sam",20)
print(sam.name)
sam.age = 30
print(sam.age)
sam.age = 130
print(sam.age)
