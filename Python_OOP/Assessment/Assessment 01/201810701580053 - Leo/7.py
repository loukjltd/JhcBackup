'''
Student Name: leo
ID: 201810701580053
Class: Network 182
'''
list1 = []
list2 = []
same = 0
insert1 = input('Enter the first line of numbers separated by commas: ')
insert2 = input('Enter the second line of numbers separated by commas: ')
for i in insert1.split(','):
    list1.append(float(i))

for n in insert2.split(','):
    list2.append((float(n)))

for a in list1:
    for j in list2:
        if j == a:
            same += 1

print('There are ' + str(same) + ' numbers that are in both lists')