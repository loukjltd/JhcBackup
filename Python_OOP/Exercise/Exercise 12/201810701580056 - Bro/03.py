# exercise 12 03
'''
Bro
201810701580056
network 182
'''
class Worker:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
workers=[Worker('Tim',65000),Worker('Jane',52000),Worker('Sam',48000)]
sum_salary=0
for sum in workers:
    sum_salary+=sum.salary
print('Sum of the salaries; '+ str(sum_salary))
