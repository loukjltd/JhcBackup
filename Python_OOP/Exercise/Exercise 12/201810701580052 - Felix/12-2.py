# Exercise 12-02
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class  Student(Person):
     def __init__(self,name,age,student_id):
         Person.__init__(self,name,age)
         self.student_id = student_id

class  Teacher(Person):
    def __init__(self,name,age,subject):
        Person.__init__(self,name,age)
        self.subject = subject
people = [Person('Alice',23),Student('Carl',19,'2017A121'),Teacher('Tom',32,'IT')]

sum_ages = 0
for i in people:
    sum_ages = sum_ages + i.age


print('Sum of ages: ',sum_ages)
