def sum_num(number):
    sum = 1
    for a in range(len(number)):
        if '0' <= number[a] <= '9':
            sum = sum * int(number[a])
    return sum


num = input("Enter a number: ")
print('The product of all of the digits of 235 is %s' % sum_num(num))