# exercise 08-02
'''
student name: Eda
ID: 201810701580031
class: network182
'''


class Person:
    name = ""
    age = 0
    def message(self):
        print("Hello")
    def details(self):
        print("My name is {} " .format(self.name),"and I am {} ".format(self.age),"years old")

sam = Person()
sam.message()
sam.name = "Sam"
sam.age = 20
sam.details()

james = Person()
james.message()
james.name = "James"
james.age = 21
james.details()
