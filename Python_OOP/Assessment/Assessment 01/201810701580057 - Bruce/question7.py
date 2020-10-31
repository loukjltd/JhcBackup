'''
student name:Bruce
ID:201810701580057
class: network 182
'''

num1 = input('Enter the first line of numbers separated by commas: ')
num2 = input('Enter the second line of numbers separated by commas: ')

list1 = []
list2 = []
sum = 0

for i in num1.split(','):
    list1.append(float(i))

for j in num2.split(','):
    list2.append(float(j))

for k in list1:
    for l in list2:
        if k == l:
            sum += 1

print('There are ' + str(sum) + ' numbers that are in both lists')
