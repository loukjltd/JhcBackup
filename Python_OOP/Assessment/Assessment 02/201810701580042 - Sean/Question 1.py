# Assessment 2 Question 1
"""
Student Name: Sean
ID: 201810701580042
Class: Network 182
"""


class Worker:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print('I work')


class Teacher(Worker):

    def __init__(self, name, age, number_of_students):
        Worker.__init__(self, name, age)
        self.number_of_students = number_of_students

    def work(self):
        print('I teach ' + str(self.number_of_students) + ' students')


class Programmer(Worker):

    def __init__(self, name, age, language):
        Worker.__init__(self, name, age)
        self.language = language

    def work(self):
        print('I write ' + str(self.language) + ' programs')


worker_list = [Worker("Sam", 23), Teacher("Ted", 33, 27), Programmer("Pete", 25, "Python")]


def print_workers(workers):

    for i in workers:
        print(i.name)
        print(i.age)
        i.work()


print_workers(worker_list)
