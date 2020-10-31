

# exercise 08-04
'''
student name: Luis
ID: 201810701580033
class: network182
'''


class Person:
    name = ""
    age= 0

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

sam=Person("Sam")
print(sam.get_name())
jams=Person("Jams")
print(jams.get_name())