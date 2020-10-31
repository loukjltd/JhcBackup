# Assessment 1 Question 8
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

tem_sum = {'Australia': 22.5, 'China': 36.4, 'Malaysia': 38.4, 'New Zealand': 18.2}
total = 0
tem_only = []
high_tem = 0

for i in tem_sum:
    print(i + ': ' + str(tem_sum[i]))
    total += float(tem_sum[i])
    tem_only.append(tem_sum[i])

print('Average temperature: ' + str('%.2f' % (total / len(tem_sum))))
print('Maximum temperature: ' + str('%.2f' % (max(tem_only))))

for j in tem_only:
    if 20 <= j <= 30:
        high_tem += 1

print('Number of temperatures between 20 and 30: ' + str(high_tem))
