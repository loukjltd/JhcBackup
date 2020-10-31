class Person:

    def __init__ (self, name, money):
        self.name = name
        self.money = money

        
def add_money(people):
    return people[0].money + people[1].money + people[2].money

        
people = []
people.append(Person("Sam", 23))
people.append(Person("Mary", 142))
people.append(Person("John", 74))

total_money = add_money(people)
print("Total money: {0}".format(total_money))
