# exercise 08-04
'''
student name: Yakira
ID: 201810701580031
class: network182
'''
class Person:
    def __init__(self,name):
        self.__name = name


    def get_name(self):
        return self.__name




sam = Person("Sam")
sam.name = "Sam"
print(sam.get_name())


James = Person("James")
James.name = "James"
print(James.get_name())