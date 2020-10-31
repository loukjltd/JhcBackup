'''
Student Name: leo
ID: 201810701580053
Class: Network 182
'''
sum = {'Australia': 22.5, 'China': 36.4, 'Malaysia': 38.4, 'New Zealand': 18.2}
total = 0
max = []
temp = 0

for i in sum:
    print(i + ': ' + str(sum[i]))
    total += float(sum[i])
    max.append(sum[i])

print('Average temperature: ' + str('%.2f' % (total / len(sum))))
print('Maximum temperature: ' + str('%.2f' % (max(max))))

for j in max:
    if 20 <= j <= 30:
        temp += 1

print('Number of temperatures between 20 and 30: ' + str(temp))