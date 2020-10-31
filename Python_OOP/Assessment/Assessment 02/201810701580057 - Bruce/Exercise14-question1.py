'''
student name :Bruce
ID:201810701580057
class:network 182
'''
class Worker:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def work(self):
        print('I work')

class Teacher(Worker):
    def __init__(self,name,age,number_of_student):
        Worker.__init__(self,name,age)
        self.number_of_student = number_of_student
    def work(self):
        print('I teach ' + str(self.number_of_student) + ' students')

class Programmer(Worker):
    def __init__(self,name,age,language):
        Worker.__init__(self,name,age)
        self.language = language
    def work(self):
        print('I write ' + str(self.language) + ' programs')


worker_list = [Worker("Sam", 23), Teacher("Ted", 33, 27),
               Programmer("Pete", 25, "Python")]


def print_workers(worker_list):
    for i in worker_list:
        print(i.name)
        print(i.age)
        i.work()

print_workers(worker_list)