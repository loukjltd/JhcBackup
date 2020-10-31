#Task7
"""
id : 201810701580049
class : Net182
name : vivi
"""
count = 0
list1 = input("Enter the first line of numbers separated by commas: ").split(",")
list2 = input("Enter the second line of numbers separated by commas: ").split(",")
for i in list1:
    for x in list2:
        if i == x:
            count += 1
print("There are {0} numbers that are in both lists".format(count))
