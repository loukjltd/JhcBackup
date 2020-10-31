# Assessment 2 Question 3
"""
Student Name: Sean
ID: 201810701580042
Class: Network 182
"""


def sum_digits(num):
    if num < 10:
        return num
    else:
        number_to_add = num % 10
        cut_number = int(num / 10)
        return number_to_add * sum_digits(cut_number)


number = int(input('Enter a number:'))
print('The product of all of the digits of ' + str(number) + ' is ' + str(sum_digits(number)))
