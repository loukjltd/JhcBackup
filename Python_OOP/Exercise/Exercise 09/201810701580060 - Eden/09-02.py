'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
class Computer:

    def __init__(self, company):
        self.__company = company

    def __private_say_company(self):
        print("The company is called {}".format(self.__company))
    def public_say_company(self):
        self.__private_say_company()
class Phone :
    def __init__(self,phonenumber):
        self.__phone_number = phonenumber

    def get_phone_number(self):
        return self.__phone_number

class Smartphone(Computer,Phone):

    def __init__(self,company,phonenumber,name):
        Computer.__init__(self,company)
        Phone.__init__(self,phonenumber)
        self.__name = name
    def get_name(self):
        return self.__name

sp1 = Smartphone("Apple","15257918341","iPhone X")
sp1.public_say_company()
print(sp1.get_phone_number())
print(sp1.get_name())