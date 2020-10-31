# Exercise 12-02
'''
name:Clark
class:net182
I  D:201810701580047
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self.student_id = student_id


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject


people = [Person('Alice', 23), Student('Carl', 19, '2017A121'), Teacher('Tom', 32, 'IT')]
sum_ages = 0
max_ages = 0
min_ages = 0
middle_ages = 0
for a in people:
    sum_ages += a.age
print('Sum of ages: %d' % sum_ages)
for b in people:
    if max_ages < b.age:
        max_ages = b.age
print('Largest age: %d' % max_ages)
for c in people:
    min_ages = c.age
    if min_ages > c.age:
        min_ages = c.age
print('Smallest age: %d' % min_ages)
for e in people:
    if 30 >= e.age >= 20:
        middle_ages += 1
print('Number of ages between 20 and 30: %d' % middle_ages)