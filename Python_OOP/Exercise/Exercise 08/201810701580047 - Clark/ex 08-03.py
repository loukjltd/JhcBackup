# Exercise 08-03
'''
name:Clark
class:net182
I  D:201810701580047
'''
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print('my name is', self.name, 'and i am', self.age, 'year old')


people = Person('Sam', 20)
people2 = Person('James', 21)
people.details()
people2.details()
