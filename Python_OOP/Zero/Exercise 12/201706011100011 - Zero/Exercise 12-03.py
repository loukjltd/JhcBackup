# net171-ZhaoYinTing


class Worker:
    def __init__(self,  name, salary):
        self.name = name
        self.salary = salary


workers = []
workers.append(Worker("Tim", 65000))
workers.append(Worker("Jane", 52000))
workers.append(Worker("Sam", 48000))

sum_salary = 0
for i in workers:
    sum_salary = sum_salary + i.salary
print("Sum of the salaries:", sum_salary)

Largest = 0
for i in workers:
    if Largest < i.salary:
        Largest = i.salary
print("Largest age:", Largest)

Smallest = 100000000000
for i in workers:
    if Smallest > i.salary:
        Smallest = i.salary
print("Smallest age:", Smallest)

a = 0
for i in workers:
    if i.salary >= 20 and i.salary <= 30:
        a += 1
print("Number of salaries between 50000 and 70000:", a)
