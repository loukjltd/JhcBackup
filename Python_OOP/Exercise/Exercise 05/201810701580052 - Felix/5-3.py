# Exercise 05-03
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
student={}
student['name']='james'
student['age']='21'
student['course']='it'
student['ID']='2016A001'
print(student)
print(student['name'],':',student['ID'])

del student['course']
for i in student:
    print(student[i])