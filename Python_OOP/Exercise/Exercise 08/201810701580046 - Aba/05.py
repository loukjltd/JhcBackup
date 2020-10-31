#exercise 08-05
'''
studentname:Aba
studentid:201810701580046
class:net182
'''
class Person:
    def __init__(self,name,age):
        self.__name =name
        self.__age =age
    def get_name(self):
        return self.__name

    def set_name(self,value):
        if value == '':
            print('Error - wrong age')
        else:
            self.__name = value
    def get_age(self):
        return self.__age
    def set_age(self,value):
        if value < 0 or value > 100:
            print("Error - age is wrong")
        else:
            self.__age = value

    def message(self):
        print('Hello')
    def __details(self):
        print('My name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old')

    name= property(get_name,set_name)
    age = property(get_age, set_age)


sam=Person('Sam',20)
print(sam.name)
sam.set_age(30)
print(sam.get_age())
sam.set_age(130)
print(sam.get_age())