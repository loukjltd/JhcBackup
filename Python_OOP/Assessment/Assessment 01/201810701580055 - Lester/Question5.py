a = int(input("How many sensors are currently collecting data?"))
list1 = []
list2 = []

for i in range(0,a):
    b = int(input("Enter temperature" + str(i + 1) + ":"))
    list1.append(b)

sum = sum(list1)
average = sum / int(len(list1))
max = mas(list1)

print("Average temperature:" + str(average))
print("Maximum temperature:" + str(max))

for i in list1:
    if 10 <= i <= 20:
        list2.append(i)

print("Number of temperatures between 10 and 20:" + str(len(list2)))
