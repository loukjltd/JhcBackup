# exercise 12-03
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
class Worker:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
workers = [Worker("Tim",65000),Worker("Jane",52000),Worker("Sam",48000)]
sum_salary = 0
for salary in workers:
    sum_salary += salary.salary
print("Sum of the salaries: ",str(sum_salary))
salarys = [65000,52000,48000]
max = max(salarys)
min = min(salarys)
num = 0
for i in salarys:
    if i >= 50000 and i <= 70000:
        num = num + 1
print('Largest age: ',max)
print('Smallest age: ',min)
print('Number of ages between 50000 and 70000: ',num)

