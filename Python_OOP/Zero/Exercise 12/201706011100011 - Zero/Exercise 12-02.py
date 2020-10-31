# net171-ZhaoYinTing

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



people = []
people.append(Person("Alice ", 23))
people.append(Student("Carl", 19, "2017A121"))
people.append(Student("Tom ", 32, "IT"))

sum_ages = 0
for i in people:
    sum_ages = sum_ages + i.age
print("Sum of ages:", sum_ages)

Largest = 0
for i in people:
    if Largest < i.age:
        Largest = i.age
print("Largest age:", Largest)

Smallest = 1000000000
for i in people:
    if Smallest > i.age:
        Smallest = i.age
print("Smallest age:", Smallest)

a = 0
for i in people:
    if i.age >= 20 and i.age <= 30:
        a += 1
print("Number of ages between 20 and 30:", a)
