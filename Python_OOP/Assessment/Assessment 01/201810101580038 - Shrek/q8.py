#exercise 08
'''
studentname:shrek
student id:201810101580038
class:net182
'''
tem_sum = {'Australia': 22.5, 'China': 36.4, 'Malaysia': 38.4, 'New Zealand': 18.2}
total = 0
tem = []
tem_high = 0

for i in tem_sum:
    print(i + ': ' + str(tem_sum[i]))
    total += float(tem_sum[i])
    tem.append(tem_sum[i])

print('Average temperature: ' + str('%.2f' % (total / len(tem_sum))))
print('Maximum temperature: ' + str('%.2f' % (max(tem))))

for j in tem:
    if 20 <= j <= 30:
        tem_high += 1

print('Number of temperatures between 20 and 30: ' + str(tem_high))