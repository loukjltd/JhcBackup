# Question 7
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
list1 = []
list2 = []
s = 0
l1 = input('Enter the first line of numbers separated by commas: ')
l2 = input('Enter the second line of numbers separated by commas: ')
for i in l1.split(','):
    list1.append(float(i))

for j in l2.split(','):
    list2.append((float(j)))

for m in list1:
    for n in list2:
        if m == n:
            s += 1

print('There are ' + str(s) + ' numbers that are in both lists')
