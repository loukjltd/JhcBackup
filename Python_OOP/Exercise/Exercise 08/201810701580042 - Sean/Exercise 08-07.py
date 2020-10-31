# Exercise 08-07
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Person:

    number_of_people = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.number_of_people += 1
        print('Added 1 person')

    @staticmethod
    def message(self):
        return 'Hello'

    @classmethod
    def count_population(cls):
        print('There are ' + str(Person.number_of_people) + ' people')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            print('Error - name is wrong')
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 100:
            print('Error - age is wrong')
        else:
            self.__age = value


print(Person.message(0))
tim = Person('Tim', 29)
tim.count_population()
alice = Person('Alice', 25)
alice.count_population()

