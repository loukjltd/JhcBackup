'''
Class:Net182
Name:Assass
Id:201810701580040
'''
class Person:
    number_of_people=0
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        print('Added 1 person')
        Person.number_of_people +=1
    def details(self):
        print('My name is ' + self.__name  + ' and I am ' + str(self.__age) +  ' years old.')
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value=='':
            print('Error - wrong name')
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 0>value or 100<value:
            print('Error - wrong age')
        else:
            self.__age=value
def message():
    print('Hello')
def count_population():
    print('There are ' + str(Person.number_of_people) + ' people')
message()
Person('Tim',29)
count_population()
Person('Akice',25)
count_population()