# Exercise 08-07
'''
name:Clark
class:net182
I  D:201810701580047
'''


class Person:
    number_of_people = 0

    def __init__(self, name, age):
        if name != '':
            if 100 > age > 0:
                Person.number_of_people += 1
        print('Added 1 person')

    @staticmethod
    def message():
        print('Hello')

    @classmethod
    def count_population(cls):
        print('There are', Person.number_of_people, 'people')


Person('Sam', 29).count_population()
Person('Alice', 25).count_population()

