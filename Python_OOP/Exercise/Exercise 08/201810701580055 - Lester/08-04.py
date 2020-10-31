class Person:

     def __init__(self,name,age):
         self._name = name
         self._age = age

     def message(self):
         print("Hello")

     def detalis(self):
         print("My name is {""}".format(self.name) + " I am {0} years old".format(self.age))


sam = Person("Sam",20)
james = Person("James",21)

print(sam._name)
