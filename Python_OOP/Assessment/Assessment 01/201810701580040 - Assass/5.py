'''
Class:Net182
Name:Assass
ID:201810701580040
'''
n = int(input('How many sensors are currently collecting data?: '))
l = []
q=0
for i in range(0, n):
    get_num = int(input('Enter temperature ' + str(i + 1) + ': '))
    l.append(get_num)
average = sum(l) / int(len(l))
max = float(max(l))
print('Average temperature: ' + str(average))
print('Maximum temperature: ' + str(max))
for i in l:
    if 10 <= i <= 20:
        q+=1
print('Number of temperatures between 10 and 20: ' + str(q))