'''
student name: Eden
#ID: 201810701580060
#class: net182
'''


class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self,value):
        if value == "":
            print("Error - wrong age")
        else:
            self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0 or value > 100:
            print("Error - wrong age")
        else:
            self.__age = value

p = Person("Sam",30)
print(p.get_name())

p.set_age(30)
print(p.get_age())

p.set_age(130)
print(p.get_age())
