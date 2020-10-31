#Exercise 08-02
'''
class net182
id 2018100701580049
name vivi
'''
class Person:
    name = ""
    age = 0

    def message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I am {1} years old".format(self.name,self.age))

sam = Person()

sam.age = 20
sam.name = "Sam"
sam.message()
sam.details()


james = Person()

james.age = 21
james.name = "James"
james.message()
james.details()