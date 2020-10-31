'''
Class:Net182
Name:Assass
ID:201810701580040
'''
class Person:
    def __init__(self,name,money):
        self.name=name
        self.money=money
def add_money(x):
    if len(x)<=0:
        return 0
    else:
        z=x[1:]
        return x[0].money + add_money(z)
people = []
people.append(Person("Sam", 23))
people.append(Person("Mary", 142))
people.append(Person("John", 74))

total_money = add_money(people)
print("Total money: {0}".format(total_money))
