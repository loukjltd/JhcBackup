#Question 1
"""
class:net182
name:vivi
id:201810701580049
"""
class Worker:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def work(self):
        return ("I work")

class Teacher(Worker):
    def __init__(self,name,age,number_of_students):
        Worker.__init__(self,name,age)
        self.number_of_students = number_of_students
    def work(self):
        return ("I teach {} student".format(self.number_of_students))

class Programmer(Worker):
    def __init__(self,name, age, language):
        Worker.__init__(self, name, age)
        self.language = language
    def work(self):
        return ("I write {} programs".format(self.language))



worker_list = [Worker("Sam", 23), Teacher("Ted", 33, 27),
               Programmer("Pete", 25, "Python")]


def print_workers(workers):

    for info in workers:

        print(info.name)
        print(info.age)
        print(info.work())


print_workers(worker_list)
exit(0)



















