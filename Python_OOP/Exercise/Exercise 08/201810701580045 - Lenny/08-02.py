#
'''
class:net182
name:lenny
ID:201810701580045
'''
class person:
    name = ''
    age = 0
    def message(self):
        print('Hello')

    def details(self):
        print('My name is {0}'.format(self.name) + ' and I am {0}'.format(self.age)  + ' years old')

Sam = person()
Sam.name = 'Sam'
Sam.age = 20
Sam.message()
Sam.details()

James = person()
James.name = 'James'
James.age = 21
James.message()
James.details()


