# Qusetion 5
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
num = input('Enter a list of numbers separated by commas: ')
list = []
f = open('./some_number.txt','w')
f.write(num)
f.close()
f = open('./some_number.txt','r')
line_of_numbers = f.readline()
max = 0
sum = 0
for i in line_of_numbers.split(','):
    list.append(i)
for i in list:
    print(i)
    sum += int(i)
    if int(i) > int(max):
        max = i
print('Sum: ' + str(sum))
print('Maximum: '+max)

