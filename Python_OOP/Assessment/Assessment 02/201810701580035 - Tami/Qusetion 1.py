# Qusetion 1
'''
Student Name: Tami
ID: 201810701580035
Class: Network 182
'''
class Worker:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print('I work')

class Teacher(Worker):
    def __init__(self,name,age,number_of_students):
        Worker.__init__(self,name,age)
        self.number_of_students=number_of_students
    def work(self):
        print('I teach {0} students'.format(self.number_of_students))

class Programmer(Worker):
    def __init__(self,name,age,language):
        Worker.__init__(self,name,age)
        self.language=language
    def work(self):
        print('I write {0} programs'.format(self.language))

worker_list = [Worker("Sam", 23), Teacher("Ted", 33, 27),
               Programmer("Pete", 25, "Python")]


def print_workers(worker_list):
    for i in worker_list:
        print(i.name)
        print(i.age)
        i.work()

print_workers(worker_list)
