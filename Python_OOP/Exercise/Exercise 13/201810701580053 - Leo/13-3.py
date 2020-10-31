,,,
Net182
Leo
201810701580053
,,,

class Person:
 def __init__(self, name,number_of_money):
        self.number_of_money = number_of_money
        self.name = name


def add_money(Person):
    if len(Person) == 0:
        return 0
    else:
        return Person[0].number_of_money + add_money(Person[1:])


people = []
people.append(Person("Sam", 23))
people.append(Person("Mary", 142))
people.append(Person("John", 74))

total_money = add_money(people)
print("Total money: {0}".format(total_money))
