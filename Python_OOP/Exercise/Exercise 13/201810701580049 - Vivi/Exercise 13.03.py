#Exercise 13-03
'''
class:net182
name:vivi
id:201810701580049
'''

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

def add_money(list1):
        le = len(list1)
        if le > 1:
            return list1[0].money + add_money(list1[1:le])
        else:
            return list1[0].money

people = []
people.append(Person("Sam", 23))
people.append(Person("Mary", 142))
people.append(Person("John", 74))

total_money = add_money(people)
print("Total money: {0}".format(total_money))
