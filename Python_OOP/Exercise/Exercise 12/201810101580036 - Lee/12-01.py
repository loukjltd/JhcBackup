my_marks = []
my_marks.append(75)
my_marks.append(87)
my_marks.append(74)
my_marks.append(63)
my_marks.append(87)
my_marks.append(71)

for mark in my_marks:
    print(mark)

sum_marks = 0
for sum in my_marks:
    sum_marks += sum
print('Sum: ' + str(sum_marks))
print('Average: ' + str(sum_marks/len(my_marks)))
