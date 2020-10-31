# exercise 09-02
'''
student name: Eda
ID: 201810701580031
class: network182
'''

class Computer:
     def __init__(self, company):
        self.__company = company
     def private_say_company(self):
         print("The company is called " + self.__company)
     def public_say_company(self):
         self.private_say_company()

class Phone:
    def __init__(self,phone_number):
        self.__phone_number = phone_number
    def get_phone_number(self):
        return self.__phone_number

class Smartphone(Computer,Phone):
    def __init__(self,company,phone_number,name):
        Computer.__init__(self,company)
        Phone.__init__(self,phone_number)
        self.name = name
    def get_name(self):
        return self.name

sp1 = Smartphone("Apple",15257918341,"iphone X")
sp1.public_say_company()
print(sp1.get_phone_number())
print(sp1.get_name())

