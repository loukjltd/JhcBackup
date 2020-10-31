# Exercise 12-02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
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
for i in people:
    sum_ages = sum_ages + i.age
print('Sum of ages: ' + str(sum_ages))

largest = 0
for j in people:
    if largest < j.age:
        largest = j.age
print('Largest age: ' + str(largest))

smallest = 100
for k in people:
    if smallest > k.age:
        smallest = k.age
print('Smallest age: ' + str(smallest))

c = 0
for k in people:
    if 20 <= k.age <= 30:
        c += 1
print('Number of ages between 20 and 30: ' + str(c))
