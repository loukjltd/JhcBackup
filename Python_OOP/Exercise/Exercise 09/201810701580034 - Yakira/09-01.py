# exercise 09-01
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
class Person:

    def __init__(self, name):
        self.name = name
    def say_name(self):
        print("Hi, my name is {}".format(self.name))


class Student(Person):

    def __init__(self, name, id):
        Person.__init__(self, name)
        self.id = id

class Worker(Person):
    def __init__(self,name,salary):
        Person.__init__(self,name)
        self.salary = salary


student1 = Student("James", "2016A1234")
print(student1.name)
print(student1.id)
student1.say_name()

worker1 = Worker("Max","3000")
print(worker1.name)
print(worker1.salary)
worker1.say_name()