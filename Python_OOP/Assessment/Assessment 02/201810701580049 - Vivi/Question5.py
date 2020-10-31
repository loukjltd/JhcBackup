#Question 5
"""
class:net182
name:vivi
id:201810701580049
"""

user_input = input('Enter a list of numbers separated by commas:')
f = open('some_numbers.txt', 'w')
f.write(user_input)
f.close()
try:
    f = open('some_numbers.txt', 'r')
    line_of_numbers = f.readline()
    num_list = line_of_numbers.split(',')
    num_list1 = []
    for i in num_list:
        print(i)
        num_list1.append(int(i))
    print('Sum: {0}'.format(sum(num_list1)))
    print('Maximum: {0}'.format(max(num_list1)))
    f.close()
except IOError:
    print('Not found')
finally:
    if f:
        f.close()
