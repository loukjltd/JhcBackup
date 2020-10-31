#exercise 12-01
'''
studentname:faker
studentid:201810701580048
class:net182
'''




student_marks =[]
student_marks.append(75)
student_marks.append(87)
student_marks.append(55)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)

for marks in  student_marks:
    print(marks)

sum_marks =0
for sum in student_marks:
    sum_marks+=sum
print( 'Sum: '+str(sum_marks))
print(str('Average: '+ str(sum_marks/len(student_marks))))

