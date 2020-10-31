'''
student name:Bruce
ID:201810701580057
class: network 182
'''

class Computer:
    def __init__(self,company):
        self.__company = company
    def public_say_company(self):
        print('The company is called ' + str(self.__company))
class Phone:
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
sp1 = Smartphone('Apple','15257918341','iphone X')
sp1.public_say_company()
print(sp1.get_phone_number())
print(sp1.get_name())