# Exercise 08-04
'''
name:Clark
class:net182
I  D:201810701580047
'''


class Person:

    def __init__(self, name):
        self.__name = name

    def details(self):
        print(self.__name)


Sam = Person('Sam')
print(Sam._Person__name)



