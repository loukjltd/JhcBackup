'''
student name: Yakira
ID: 201810701580034
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

sensors = int(input("How many sensors are currently collecting data?: "))
t = []
num = 0
for i in range(0,sensors) :
    temperature = float(input('Enter temperature ' + str(i + 1) + ':'))
    t.append(temperature)
    if temperature >= 10 and temperature <= 20:
        num = num+1
Sum = sum(t)
average = Sum / int(sensors)


print("Average temperature: " , average)
print("Maximum temperature: " , max(t))
print("Number of temperatures between 10 and 20: " , num)