'''
Class:Net182
Name:Assass
ID:201810701580040
'''
student_marks=[75,87,74,63,87,71]
sum_marks=0
for i in student_marks:
    print(str(i))
    sum_marks+=i
print('Sum:' + str(sum_marks))
print('Average:' + str('%.1f' %(sum_marks/len(student_marks))))