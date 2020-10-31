#exercise 05-04
'''
name:Lenny
class:net182
ID:201810701580045
'''
marks = {}
marks['Sam'] = 90.5
marks['Jane'] = 85.4
marks['Max'] = 92.3
marks['Alice'] = 64.5
marks['John'] = 69.4
sum = 0
for i in marks.values():
    sum = sum + i
print('Sum:' + str(sum))
print('Average:' + str(sum/len(marks)))
