'''
Student Name: Leo
ID: 201810701580053
Class: Network 182
'''
class Person:
    name=''
    age = 0
    def message(self):
        print('Hello')
    def details(self):
        print('My name is ' +str(self.name)+ ' and I am {0} years old.'.format(self.age))
sam=Person()
sam.name='Sam'
sam.age=20
sam.message()
sam.details()
james=Person()
james.name='James'
james.age=21
james.message()
james.details()
