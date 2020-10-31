# exercise 08 02
'''
Bro
201810701580056
network 182
'''
class person:
    name=''
    age=0

    def message(self):
        print('Hello')
    def details(self):
        print('My name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old')

sam =person()
sam.name='Sam'
sam.age=20
sam.message()
sam.details()

james =person()
james.name='James'
james.age=21
james.message()
james.details()