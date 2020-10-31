'''
student name:Bruce
ID:201810701580057
class: network 182
'''


class Person:
    def __init__(self,name):
        self.__name = name
    def message(self):
        print('Hello')
    def details(self):
        print('My name is ' + str(self.__name))

sam = Person('Sam')

#print(sam.name)
print(sam._Person__name)


