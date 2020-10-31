#Exercise 12-03
#Josh net182 201810701580043

class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

worker = []
worker.append(Worker('Tim', 65000))
worker.append(Worker('Jane', 52000))
worker.append(Worker('Sam', 48000))

sum_salary = 0
max_sa = 0
min_sa = 0
mdcount = 0
for i in worker:
    isa = i.salary
    sum_salary += isa
    if isa > max_sa or max_sa == 0:
        max_sa = isa
    if isa < min_sa or min_sa == 0:
        min_sa = isa
    if isa >= 50000 and isa <= 70000:
        mdcount += 1
print('Sum of the salaries:', sum_salary)
print('Largest salary:', max_sa)
print('Smallest salary:', min_sa)
print('Number of salaries between 50000 and 70000:', mdcount)