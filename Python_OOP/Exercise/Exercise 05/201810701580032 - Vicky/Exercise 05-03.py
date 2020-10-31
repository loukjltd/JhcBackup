#Exercise 05-03
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

student = {'Course':'IT','ID': '2016A001', 'Age': 21, 'Name': 'James'}
print(student)
del student['Course']
print('James'+':'+'2016A001')
for key in student:
    print(student[key])