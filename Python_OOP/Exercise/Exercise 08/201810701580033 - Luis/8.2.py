

# exercise 08-02
'''
student name: Luis
ID: 201810701580033
class: network182
'''


class Person:
    name = ""
    age= 0

    def message(self):
        print("Hello")

    def details(self):
        print("My name is {}".format(self.name)," and I am {0}".format(self.age) , "years old.")

person = Person()
person.message()
person.name="Sam"
person.age =20
person.details()

my_person1=Person()
my_person1.name="Jams"
my_person1.age =21
my_person1.message()
my_person1.details()

