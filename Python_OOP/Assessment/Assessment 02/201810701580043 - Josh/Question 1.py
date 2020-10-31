#Question 1
#Josh net182 201810701580043

class Worker:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def work(self):
        print('I work')

class Teacher(Worker):
    def __init__(self, name, age, number_of_students):
        Worker.__init__(self, name, age)
        self.number_of_students = number_of_students
    def work(self):
        print('I teach {0} students'.format(self.number_of_students))

class Programmer(Worker):
    def __init__(self, name, age, language):
        Worker.__init__(self, name, age)
        self.language = language
    def work(self):
        print('I write {0} programs'.format(self.language))

worker_list = [Worker("Sam", 23), Teacher("Ted", 33, 27), Programmer("Pete", 25, "Python")]

def print_workers(workers):
    for i in workers:
        print(i.name)
        print(i.age)
        i.work()

print_workers(worker_list)
