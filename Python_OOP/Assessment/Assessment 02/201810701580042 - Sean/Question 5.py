# Assessment 2 Question 5
"""
Student Name: Sean
ID: 201810701580042
Class: Network 182
"""


list1 = input('Enter a list of numbers separated by commas:')
f1 = open('some_numbers.txt', 'w')
f1.write(list1)
f1.close()
total = 0
maximum = 0
f2 = open('./some_numbers.txt', 'r')
line_of_numbers = f2.readline()
split_line = line_of_numbers.split(',')
for i in split_line:
    print(i)
    total = total + int(i)
    if maximum < int(i):
        maximum = int(i)
print('Sum: ' + str(total))
print('Maximum: ' + str(maximum))
