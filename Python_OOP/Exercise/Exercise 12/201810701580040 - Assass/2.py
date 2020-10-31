'''
Class:Net182
Name:Assass
ID:201810701580040
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,student_id):
        Person.__init__(self,name,age)
        self.student_id=student_id
class Teacher(Person):
    def __init__(self,name,age,subject):
        Person.__init__(self,name,age)
        self.subject=subject
people=[]
people.append(Person('Alice',23))
people.append(Student('Carl',19,'2017A21'))
people.append(Teacher('Tom',32,'IT'))
sum_ages=0
for i in people:
    sum_ages+=i.age
print('Sum of ages:'+str(sum_ages))

