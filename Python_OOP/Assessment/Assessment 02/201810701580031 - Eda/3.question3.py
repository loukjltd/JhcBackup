# question 3
'''
Student name: Eda xiang
Student ID: 201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

def f(x):
    if x <= 0:
        return 1
    else:
        return int(x % 10) * f(int(x / 10))

num = int(input("Enter a number: "))
print("The product of all of the digits of "+ str(num) + " is "+ str(f(num)))