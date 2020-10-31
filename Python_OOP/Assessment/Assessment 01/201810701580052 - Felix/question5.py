s = int(input('How many sensors are currently collecting data?: '))
list1 = []
list2 = []
for i in range(1,s+1):
    t = float(input('Enter temperature ' + str(i) + ': '))
    list1.append(t)
Sum = sum(list1)
Average = sum(list1)/len(list1)
Maximum = max(list1)

for a in list1:
    if 10 <= a <= 20:
        list2.append(a)
print('Average temperature: ',Average)
print('Maximum temperature: ',Maximum)
print('Number of temperatures between 10 and 20: ',len(list2))


