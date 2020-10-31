class Person:
     name = ""
     age = 0

     def message(self):
         print("Hello")

     def detalis(self):
         print("My name is {""}".format(self.name) + " I am {0} years old".format(self.age))

sam = Person()
sam.name = "Sam"
sam.age = 20
sam.message()
sam.detalis()

james = Person()
james.name = "James"
james.age = 21
james.message()
james.detalis()
