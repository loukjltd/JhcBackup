# exercise05-03
'''
student name: Steven
ID: 201810101580037
class: network 182
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
