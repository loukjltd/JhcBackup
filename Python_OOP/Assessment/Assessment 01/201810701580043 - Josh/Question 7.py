#Question 7
#Josh net182 201810701580043

numlis1 = input('Enter the first line of numbers separated by commas: ').split(',')
numlis2 = input('Enter the second line of numbers separated by commas: ').split(',')
newlist = []
ct = 0

for i in numlis1:
    newlist.append(float(i))

for i in newlist:
    for j in numlis2:
        if i == float(j):
            ct += 1

print('There are '+str(ct) + ' numbers that are in both lists')
