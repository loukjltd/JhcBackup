class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def message(self):
        print('Hello')
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
sam=Person('Sam',20)

james=Person('James',21)
sam.name='Sam'
sam.age=20
print(sam.name)
sam.get_age=30
print(str(sam.get_age))
sam.get_age=130
print(str(sam.get_age))