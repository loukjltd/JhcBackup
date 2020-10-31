# exercise 12-02
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name,age,student_id):
        Person.__init__(self,name,age)
        self.student_id = student_id
class Teacher(Person):
    def __init__(self,name,age,subject):
        Person.__init__(self,name,age)
        self.subject = subject
people = [Person("Alice",23),Student("Carl",19,"2017A121"),
          Teacher("Tom",32,"IT")]

sum_ages = 0
for age in people:
    sum_ages += age.age
ages = [23,19,32]

max = max(ages)
min = min(ages)
num = 0
for i in ages:
    if i >= 20 and i <= 30:
        num = num + 1
print("Sum of ages: ",str(sum_ages))
print('Largest age: ',max)
print('Smallest age: ',min)
print('Number of ages between 20 and 30: ',num)


