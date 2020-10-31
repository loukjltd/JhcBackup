'''
Class:Net182
Name:Assass
ID:201810701580040
'''
same = 0
l1 = input('Enter the first line of numbers separated by commas: ').split(',')
l2 = input('Enter the second line of numbers separated by commas: ').split(',')
for m in l1:
    for n in l2:
        if m == n:
            same += 1
print('There are ' + str(same) + ' numbers that are in both lists')