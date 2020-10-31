#Exercise 09-01
"""
class:Net182
name:vivi
id:201810701580049
"""
class Person:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("Hi, my name is {0}".format(self.name))


class Student(Person):

    def __init__(self, name, id):
        Person.__init__(self, name)
        self.id = id

class Worker(Person):

    def __init__(self,name,salary):
        Person.__init__(self, name)
        self.name = name
        self.salary = salary



student1 = Student("James", "2016A1234")
print(student1.name)
print(student1.id)
student1.say_name()
Worker1 = Worker("Max",'30000')
print(Worker1.name)
print(Worker1.salary)
Worker1.say_name()
