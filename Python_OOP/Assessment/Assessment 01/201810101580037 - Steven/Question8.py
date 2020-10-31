# Question 8
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
t = {'Malaysia': 38.4, 'China': 36.4, 'Australia': 22.5, 'New Zealand': 18.2}
t_sum = 0
t_only = []
t_high = 0

for i in t:
    print(i + ': ' + str(t[i]))
    t_sum += float(t[i])
    t_only.append(t[i])

print('Average temperature: ' + str('%.2f' % (t_sum/len(t))))
print('Maximum temperature: ' + str('%.2f' % max(t_only)))

for j in t_only:
    if 20 <= j <= 30:
        t_high += 1

print('Number of temperatures between 20 and 30: ' + str(t_high))
