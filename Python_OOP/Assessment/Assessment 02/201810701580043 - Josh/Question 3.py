#Question 3
#Josh net182 201810701580043

def cal_num(num1):
    if num1 == 0:
        return 1
    else:
        return cal_num(int(num1/10)) * (num1 % 10)

numi = int(input('Enter a number: '))
print('The product of all of the digits of {0} is {1}'.format(numi, cal_num(numi)))
