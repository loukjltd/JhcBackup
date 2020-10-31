# Exercise 12-03
'''
student name: jone
#ID: 201810701580059
#class: net182
'''
class  Worker:
    def __init__(self,name,salary):
         self.name = name
         self.salary = salary

workers = []
workers = [Worker('Tim',65000),Worker('Jane',52000),Worker('Sam',48000)]

sum_salary = 0

for i in workers:
    sum_salary = sum_salary + i.salary

print('Sum of the salaries: ',sum_salary)
