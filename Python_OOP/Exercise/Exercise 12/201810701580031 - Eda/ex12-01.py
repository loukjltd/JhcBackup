# exercise 12-01
'''
student name: Eda
ID: 201810701580031
class: network182
'''

student_marks = []
student_marks.append(75)
student_marks.append(87)
student_marks.append(74)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)
student_marks[2] = 55
for i in student_marks:
    print(i)
sum_marks = 0
for j in student_marks:
   sum_marks += j
   a = sum_marks/len(student_marks)
print("sum " + str(sum_marks))
print("average " + str(a))