# exercise 08-02
'''
student name: Yakira
ID: 201810701580031
class: network182
'''
class Person:
    name = ""
    number_of_age = 0

    def message(self):
        print("Hello")
    def details(self):
        print("My name is {} " .format(self.name), "and I am {0}".format(self.number_of_age), "years old.")

person1 = Person()
person1.message()
person1.name = "Sam"
person1.number_of_age = 20
person1.details()

person2 = Person()
person2.message()
person2.name = "James"
person2.number_of_age = 21
person2.details()
