# Exercise 12-03
'''
name:Clark
class:net182
I  D:201810701580047
'''
class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


workers = [Worker('Tim', 65000), Worker('Jane', 52000), Worker('Sam', 48000)]
x = 0
for a in workers:
    x += a.salary
print('Sum of the salaries: %d' % x)