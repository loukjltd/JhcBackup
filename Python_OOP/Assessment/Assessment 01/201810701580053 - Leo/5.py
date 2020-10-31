'''
Student Name: leo
ID: 201810701580053
Class: Network 182
'''
num = int(input('How many sensors are currently collecting data?:'))

list1 = []
list2 = []

for i in range(0, num):
    temp= int(input('Enter temperature ' + str(i + 1) + ': '))
    list1.append(temp)

sum = sum(list1)
average= sum / int(len(list1))
max = max(list1)

print('Average temperature: ' + str(average))
print('Max mum temperature: ' + str(max))

for i in list1:
    if 10 <= i <= 20:
        list2.append(i)

print('Number of temperatures between 10 and 20: ' + str(len(list2)))