#Exercise 08-06
#Josh net182 201810701580043

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == '':
            print("Error : name not found")
        else:
            self.__name = value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value < 0 or value > 100:
            print("Error : age is wrong")
        else:
            self.__age = value
    def message(self):
        print('Hello')
    def details(self):
        print('My name is '+self.__name+' and I am '+str(self.__age)+' years old.')

sam = Person('Sam', 20)

james = Person('James', 21)

print(sam.name)
sam.age = 30
print(sam.age)
sam.age = 130
print(sam.age)