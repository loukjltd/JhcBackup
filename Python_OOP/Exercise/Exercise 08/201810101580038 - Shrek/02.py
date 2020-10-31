#exercise 08-02
'''
studentname:shrek
studentid:201810101580038
class:net182
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