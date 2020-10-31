#Task5
"""
id : 201810701580049
class : Net182
name : vivi
"""
count = 0
sensors = []
sensors_sum = int(input("How many sensors are currently collecting data?: "))

for i in range(1,sensors_sum+1):
    id = float(input("Enter temperature " + str(i) +" : "))
    sensors.append(id)

Sum = 0
for i in sensors:
    Sum += float(i)
    if float(i) >= 10 and float(i) <=20:
        count += 1

average = Sum / len(sensors)
print("Average temperature: " + "{0:.2f}".format(average))
print("Maximum temperature: " + "{0:.2f}".format(max(sensors)))
print("Number of temperatures between 10 and 20:" + str(count))