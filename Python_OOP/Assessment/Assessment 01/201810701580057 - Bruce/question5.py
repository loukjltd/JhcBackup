'''
student name:Bruce
ID:201810701580057
class: network 182
'''

number = int(input('How many sensors are currently collecting data?: '))

list1 = []
list2 = []

for i in range(0,number):
    getnumber = float(input('Enter temperature ' + str(i + 1) + ' : '))
    list1.append(getnumber)

sumlist = sum(list1)
averagerlist = sumlist / int(len(list1))
maxnumber = max(list1)

print('Averager temputer: ' + str('%.2f' % averagerlist))
print('Maximum temperature: ' + str(maxnumber))

for i in list1:
    if 10 <= i and i <= 20 :
        list2.append(i)

print('Number of temperatures between 10 and 20: ' + str(len(list2)))

