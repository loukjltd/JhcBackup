# Exercise 09-02
'''
name:Clark
class:net182
I  D:201810701580047
'''
class Computer:

    def __init__(self, company):
        self.__company = company

    def __priveate_say_company(self):
        print('The company is', self.__company)

    def public_say_company(self):
        self.__priveate_say_company()


class Phone:
    def __init__(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        print(self.__phone_number)


class SmartPhone(Computer, Phone):
    def __init__(self, name, company, phone_number):
        Computer.__init__(self, company)
        Phone.__init__(self, phone_number)
        self.__name = name

    def gat_name(self):
        print(self.__name)


phone = SmartPhone('iPhone X', 'Apple', '15257918341')
phone.public_say_company()
phone.get_phone_number()
phone.gat_name()