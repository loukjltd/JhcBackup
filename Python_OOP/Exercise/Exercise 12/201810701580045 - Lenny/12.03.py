#
'''
class:net182
name:lenny
ID:201810701580045
'''
class Worker:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

worker = [Worker('Tim',65000),Worker('Jane',52000),Worker('Sam',48000)]

sum_salary = 0
for salary in worker:
    sum_salary += salary.salary
print('Sum of the salaries: ' + str(sum_salary
                                    ))
