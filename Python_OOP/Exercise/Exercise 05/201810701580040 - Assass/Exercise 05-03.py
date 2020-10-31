#Exercise 05-03
'''
name: Assass
idnumber: 201810701580040
class: network 182
'''
student={}
student['Name']='James'
student['Age']= 21
student['Course']='IT'
student['ID']='2016A001'
print(student)
print(student['Name']+':'+student['ID'])
del student['Course']
for i in student:
    print(i+':'+str(student[i]))