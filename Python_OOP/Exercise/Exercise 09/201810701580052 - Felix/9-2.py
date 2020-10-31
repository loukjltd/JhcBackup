class Computer:
 def __init__(self, company):
     self.__company = company
 def __private_say_company(self):
     print("The company is called ",self.__company)
 def public_say_company(slef):
     slef.__private_say_company()

class Phone:
    def __init__(self,phone_number):
        self.__phone_number = phone_number
    def get_phone_number(self):
        return self.__phone_number

class Smartphone(Computer,Phone):
    def __init__(self, company, phone_number, name):
        Computer.__init__(self, company)
        Phone.__init__(self, phone_number)
        self.__name = name
    def get_name(self):
        return self.__name

spl = Smartphone('Apple',15257918341,'iphone X')
spl.public_say_company()
print(spl.get_phone_number())
print(spl.get_name())


