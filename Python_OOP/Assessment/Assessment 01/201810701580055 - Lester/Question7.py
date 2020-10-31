list1 = []
list2 = []
same = 0
a = input("Enter the first line of numbers separated by commas:")
b = input("Enter the secoond line of numbers separated by commas:")

for i in a.split(","):
    list1.append(float(i))
for j in b.split(","):
    list2.append(float(j))

for c in list1:
    for d in list2:
        if c == d:
            same += 1

print("There are" + str(same) + "numbers that are in both lists")


