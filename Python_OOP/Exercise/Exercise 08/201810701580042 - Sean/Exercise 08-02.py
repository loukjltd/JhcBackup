# Exercise 08-02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Person:
    name = ''
    age = 0

    def message(self):
        print('Hello')

    def details(self):
        print('My name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old.')


sam = Person()
sam.name = 'Sam'
sam.age = 20
sam.message()
sam.details()

james = Person()
james.name = 'James'
james.age = 21
james.message()
james.details()
