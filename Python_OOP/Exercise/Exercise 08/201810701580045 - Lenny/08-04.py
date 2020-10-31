#
'''
class:net182
name:lenny
ID:201810701580045
'''


class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age


Sam = person('Sam',20)
print(Sam._person__name)
print(Sam.__name)


