# exercise07-01
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
a = 3
b = 5
c = 9
def max_num(num1, num2, num3):
    if num1 > num2:
        largest = num1
    else:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

print('Maximum number is ' + str(max_num(a, b, c)))
