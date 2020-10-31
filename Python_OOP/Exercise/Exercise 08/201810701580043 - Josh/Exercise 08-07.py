#Exercise 08-07
#Josh net182 201810701580043

class Person:
    number_of_people = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.number_of_people += 1
        print('Added 1 person')
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
        return self.__age
    @age.setter
    def age(self,value):
        if value < 0 or value > 100:
            print("Error : age is wrong")
        else:
            self.__age = value
    @staticmethod
    def message():
        print('Hello')
    def details(self):
        print('My name is '+self.__name+' and I am '+str(self.__age)+' years old.')
    @classmethod
    def count_population(cls):
        print('There are {0} people'.format(cls.number_of_people))

Person.message()
tim = Person('Tim', 29)
Person.count_population()
alice = Person('Alice', 25)
Person.count_population()