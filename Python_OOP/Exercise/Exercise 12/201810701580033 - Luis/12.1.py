

# exercise 12-01
'''
student name: Luis
ID: 201810701580033
class: network182
'''


student_marks=[]

student_marks.append(75)
student_marks.append(87)
student_marks.append(74)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)

del student_marks[2]
student_marks.insert(2,55)
for i in student_marks:
      print(i)
sum_marks=0
for j in student_marks:
    sum_marks=sum_marks+j
print("Sum:"+str(sum_marks))
print("Average:"+str(float(sum_marks/5)))
