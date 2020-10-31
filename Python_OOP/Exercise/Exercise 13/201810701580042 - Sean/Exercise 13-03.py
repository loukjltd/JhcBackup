# Exercise 13-03
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money


def add_money(people):
    if len(people) == 0:
        return 0
    else:
        return people[0].money + add_money(people[1:len(people)])


people = [Person('Sam', 23), Person('Mary', 142), Person('John', 74)]
total_money = add_money(people)
print('Total money: {0}'.format(total_money))
