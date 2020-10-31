'''class;net182
id address;201810701580048
name;  Faker

class Person:

    def __init__(self,name,money):
        self.money=money
        self.name=name


def add_money(person):
    if len(person) == 0:
        return 0
    else:
        return person[0].money + add_money(person[1:])



people = []
people.append(Person("Sam", 23))
people.append(Person("Mary", 142))
people.append(Person("John", 74))

total_money = add_money(people)
print("Total money: {0}".format(total_money))
