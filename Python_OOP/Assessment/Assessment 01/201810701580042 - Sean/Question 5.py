# Assessment 1 Question 5
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

n = int(input('How many sensors are currently collecting data?: '))
myList = []
betweenList = []

for i in range(0, n):
    get_num = int(input('Enter temperature ' + str(i + 1) + ': '))
    myList.append(get_num)

sum_new = sum(myList)
average_new = sum_new / int(len(myList))
max_num = max(myList)

print('Average temperature: ' + str(average_new))
print('Maximum temperature: ' + str(max_num))

for i in myList:
    if 10 <= i <= 20:
        betweenList.append(i)

print('Number of temperatures between 10 and 20: ' + str(len(betweenList)))
