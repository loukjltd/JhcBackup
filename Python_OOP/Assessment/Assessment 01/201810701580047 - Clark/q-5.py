# Question 5
'''
name:Clark
class:net182
I  D:201810701580047
'''
sensors = int(input('How many sensors are currently collecting data?: '))
li = []
x = 0
y = 0
for a in range(1, sensors+1):
    tem = input('Enter temperature ' + str(a) + ': ')
    li.append(tem)
    if 10 < float(tem) < 20:
        y += 1
    x += float(tem)

print('Average temperature:', x / sensors)
print('Maximum temperature:', max(li))
print('Number of temperatures between 10 and 20', y)
