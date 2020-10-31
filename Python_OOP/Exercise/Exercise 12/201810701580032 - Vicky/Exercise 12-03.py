#Exercise 12-03
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

class Worker:
    def __init__(self, name,salary):
        self.name =name
        self.salary=salary


workers=[]
workers.append(Worker('Tim',65000))
workers.append(Worker('Jane',52000))
workers.append(Worker('SAm',48000))

sum_salary=0
for Worker in workers:
    sum_salary=sum_salary+int(Worker.salary)
print('Sum of the salaries:'+str(sum_salary))
