#Question 7
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

a = str(input("Enter the first line of numbers separated by commas: ")).split(",")
b = str(input("Enter the second line of numbers separated by commas: ")).split(",")

s = 0
for i in a:
    for j in b:
        while i == j:
            s += 1
            break
print("There are " + str(s) + " numbers that are in both lists")
