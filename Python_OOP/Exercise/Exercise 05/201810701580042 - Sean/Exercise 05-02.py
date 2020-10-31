# Exercise 05-02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

n = int(input('Enter the number of values to insert: '))
myList = []

for i in range(0, n):
    get_num = int(input('Enter a number to insert: '))
    myList.append(get_num)

sum_new = sum(myList)
average_new = sum_new / int(len(myList))
print('Sum is ' + str(sum_new))
print('Average is ' + str(average_new))
