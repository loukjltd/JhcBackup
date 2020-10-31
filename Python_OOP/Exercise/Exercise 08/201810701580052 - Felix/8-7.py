# Exercise 08-07
'''
student name: felix
#ID: 201810701580052
#class: net182
'''


class person:
    number_of_people = 0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        person.number_of_people += 1
        print('Added 1 person')

    @staticmethod
    def message(self):
        return 'hello'

    @classmethod
    def count_population(cls):
        print('There are ' + str(person.number_of_people) + ' people')


    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value < 0 or value > 100:
            print("Error - age is wrong")
        else :
            self.__age = value




print(person.message(0))
tim = person('Tim', 29)
tim.count_population()
alice = person('Alice', 25)
alice.count_population()


