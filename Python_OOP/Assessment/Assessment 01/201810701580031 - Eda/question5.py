#question5
'''
student name:Eda xiang
student ID:201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''


a = int(input("How many sensors are currently collecting data?: "))
my_list = []
for i in range(1,a+1):
    b = float(input("Enter temperature" + str(i) + " : "))
    my_list.append(b)
average = sum(my_list)/a
maximum = max(my_list)
print("Average temperature: " + str("%.2f"% average))
print("Maximum temperature: " + str("%.2f"% maximum))
c = 0
for j in my_list:
    if j >= 10 and j <= 20:
        c += 1
print("Number of temperatures between 10 and 20: " + str(c))

