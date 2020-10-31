# exercise 10-02
'''
student name: Luis
ID: 201810701580033
class: network182
'''

class Animal:

    def __init__(self,type):
        self.type = type

    def sound(self):
        return 2

    def sound(self):
        print("no sound")

    def display_info(self) :
        print( "Type:" + self.type)


class Dog(Animal):

    def __init__ (self,type,weight):
     Animal.type=type
     Animal.weight=weight

     def sound(self):
         print("Woof")

class Cat(Animal):

    def __init__ (self,type,color):
     Animal.type=type
     Animal.color=color

     def sound(self):
         print("Meow")

my_dog=Dog("Labrador",22)
my_dog.sound()
my_dog.display_info()
