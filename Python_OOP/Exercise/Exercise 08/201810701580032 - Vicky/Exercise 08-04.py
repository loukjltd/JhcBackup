#Exercise 08-04
'''
student name :Vicky
ID:201810701580032
class:Net182
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
