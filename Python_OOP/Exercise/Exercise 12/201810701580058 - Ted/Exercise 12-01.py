# Exercise 12-01
'''
Student Name: Ted
ID: 201810701580058
Class: Network 182
'''

student_marks=[]

student_marks.append(75)
student_marks.append(87)
student_marks.append(74)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)

student_marks[2]=55

for i in student_marks:
    print(i)

sum_marks=0
a=0

for i in student_marks:
    sum_marks+=i
    a+=1

print('Sum: '+str(sum_marks))
print('Average: '+str(sum_marks/a))