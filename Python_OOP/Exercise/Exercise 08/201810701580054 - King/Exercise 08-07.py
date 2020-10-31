# Exercise 08-07
'''
name: King
idnumber: 201810701580054
class: net182
'''
class Person:
    number_of_people = 0
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        Person.number_of_people += 1
        print('Added 1 person')
    @staticmethod
    def message(self):
        return 'Hello'
    def details(self):
        print('My name is ' +str(self.__name)+ ' and I am {0} years old.'.format(self.__age))

    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def set_name(self,value):
        if value=='':
            print('Error - wrong name')
        else:
            self.__name=value
    @property
    def get_age(self):
        return self.__age
    @get_age.setter
    def get_age(self,value):
        if value<0 or value>100:
            print('Error - wrong age')
        else:
            self.__age=value

    @classmethod
    def count_population(cls):
        print('There ara ' +str(Person.number_of_people) +' people')
print(Person.message(0))
tim=Person('Tim',29)
tim.count_population()
alice=Person('Alice',25)
alice.count_population()