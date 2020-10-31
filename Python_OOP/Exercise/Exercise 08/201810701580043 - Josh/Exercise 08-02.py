#Exercise 08-02
#Josh net182 201810701580043

class Person:
    name = ''
    age = 0
    def message(self):
        print('Hello')
    def details(self):
        print('My name is '+self.name+' and I am '+str(self.age)+' years old.')

sam = Person()
sam.name = 'Sam'
sam.age = 20

james = Person()
james.name = 'James'
james.age = 21

sam.message()
sam.details()
james.message()
james.details()