#question7
'''
student name:Eda xiang
student ID:201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
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