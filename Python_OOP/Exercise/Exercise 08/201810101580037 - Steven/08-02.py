# exercise08-02
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
class Person:
    name = ""
    age = 0
    def message(self):
        print("Hello")
    def details(self):
        print("My name is",self.name,"and I am",self.age,"years old.")

sam = Person()
sam.name = "Sam"
sam.age = 20
sam.message()
sam.details()

james = Person()
james.name = "James"
james.age = 21
james.message()
james.details()
