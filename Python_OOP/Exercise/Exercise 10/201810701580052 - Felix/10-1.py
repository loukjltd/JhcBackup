class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        prints('Hello')

    def display_info(self):
        print('Name: ',self.name)


class Customer(Person):

    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age = age

    def greeting(self):
        print('Dear customers, I am ',self.age, 'years old')


cus = Customer('John Smith',20)
cus.greeting()
cus.display_info()
