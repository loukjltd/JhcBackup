# Exercise 08-02
'''
student name: felix
#ID: 201810701580052
#class: net182
'''


class person:
 name = ''
 age = 0
 def message(self):
     print('Hello')
 def details(self):
     print('My name is {0} and I am {1} years old'.format(self.name,self.age))

sam = person()
sam.name = 'sam'
sam.age = 20
sam.message()
sam.details()

james = person()
james.name = 'james'
james.age = 21
james.message()
james.details()


