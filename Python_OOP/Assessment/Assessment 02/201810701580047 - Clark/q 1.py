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
        print('I teach %s student' % self.number_of_students)


class Programmer(Worker):
    def __init__(self, name, age, language):
        Worker.__init__(self, name, age)
        self.language = language

    def work(self):
        print('I write %s programs' % self.language)


worker_list = [Worker("Sam", 23), Teacher("Ted", 33, 27),
               Programmer("Pete", 25, "Python")]


def print_workers(workers):
    for a in workers:
        print(a.name)
        print(a.age)
        a.work()


print_workers(worker_list)
