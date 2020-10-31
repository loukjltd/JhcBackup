# exercise 12-03
'''
student name: Eda
ID: 201810701580031
class: network182
'''

class Worker:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
worker = []
worker.append(Worker("Tim",65000))
worker.append(Worker("Jane",52000))
worker.append(Worker("Sam",48000))
sum_salary = 0
for Worker in worker:
    sum_salary += Worker.salary
print("Sum of the salaries: " + str(sum_salary))