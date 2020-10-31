'''
Class:Net182
Name:Assass
ID:201810701580040
'''
d = {'Australia': 22.5, 'China': 36.4, 'Malaysia': 38.4, 'New Zealand': 18.2}
sum = 0
l = []
q = 0
for i in d:
    print(i + ': ' + str(d[i]))
    sum += float(d[i])
    l.append(d[i])
for i in l:
    if 20 <= i <= 30:
        q += 1
print()
print('Average temperature: ' + str('%.2f' % (sum / len(d))))
print('Maximum temperature: ' + str('%.2f' % (max(l))))
print('Number of temperatures between 20 and 30: ' + str(q))