#  net171 ZhaoYinTing

class Person:
    def __init__(self, name):
        self.name = name

    #< Make a method called greeting() that prints "Hello" >
    def greeting(self):
        print("Hello")

    #< Make a method called display_info() that prints out "Name: ... + the name variable>
    def display_info(self):
        print("Name:",self.name)


class Customer(Person):

    #< Make the __init__ method with name and age >
    def __init__(self, name, age):
        #< Call the Person __init__ method >
        Person.__init__(self, name)
        #< Set the age object variable >
        self.age = age

    #< Make a method called greeting() that prints "Dear customers, I am ?? years old" with the age variable >
    def greeting(self):
        print("Dear customers, I am %s years old"  %(self.age))


#< Make a customer object with the name "John Smith" and the age 20 >
customer1=Customer("John Smith",20)
# < Call the greeting() method >
customer1.greeting()
# < Call the display_info() method >
customer1.display_info()