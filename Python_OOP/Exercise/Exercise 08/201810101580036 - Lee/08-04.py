'''
name:Lee
class:net182
ID:201810101580036
'''
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


sam = Person('Sam', 20)
sam._Pet__name = 'Sam'
print(sam._Person__name)
print(sam.name)