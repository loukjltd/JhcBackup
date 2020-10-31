'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
class Animal:
    def __init__(self,type):
        self.type = type
    def sound(self):
        print("No sound")
    def display_info(self):
        print("Type: {0}".format(self.type))
class Dog(Animal):
    def __init__(self,weight):
        Animal.__init__(self,weight)
    def sound(self):
        print("Woof")
class Cat(Animal):
    def __init__(self,color):
        Animal.__init__(self,color)
    def sound(self):
        print("Meow")

my_dog = Dog("Labrador")
my_dog.sound()
my_dog.display_info()
my_cat = Cat("Siamese")
my_cat.sound()
my_cat.display_info()

