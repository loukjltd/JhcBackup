'''
student name :Bruce
ID:201810701580057
class:network 182
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
Person_list = [Person('Alice',23),Student('Carl',19,'2017A121'),Teacher('Tom',32,'IT')]

sum_ages = 0
for age in Person_list:
    sum_ages += age.age
print('Sum of ages: ' + str(sum_ages))
