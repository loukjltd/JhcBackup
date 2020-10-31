# Exercise 05-03
'''
Student Name: Charlie
ID: 201810101580044
Class: Network 182
'''
student = {}
student['course'] = "it"
student['id'] = "2016A001"
student['age'] = 21
student['name'] = "james"
print(student)
print(student['name']+":"+student['id'])
del student['course']
for d in student :
    print(student[d])