'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
student_marks = []
student_marks.append(75)
student_marks.append(87)
student_marks.append(55)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)

for mark in student_marks:
    print(mark)

sum_marks = sum([75,87,55,63,87,71])
print("Sum: "+ str(sum_marks))

sun = sum_marks/len(student_marks)
print("Average: " + str(sun))
