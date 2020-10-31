# Exercise 12-03
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


workers = [Worker("Tim", 65000), Worker("Jane", 52000), Worker("Sam", 48000)]

sum_salary = 0
for i in workers:
    sum_salary = sum_salary + i.salary
print('Sum of the salaries: ' + str(sum_salary))

largest = 0
for j in workers:
    if largest < j.salary:
        largest = j.salary
print('Largest age: ' + str(largest))

smallest = 100000
for k in workers:
    if smallest > k.salary:
        smallest = k.salary
print('Smallest age: ' + str(smallest))

c = 0
for l in workers:
    if 20 <= l.salary <= 30:
        c += 1
print('Number of salaries between 50000 and 70000: ' + str(c))
