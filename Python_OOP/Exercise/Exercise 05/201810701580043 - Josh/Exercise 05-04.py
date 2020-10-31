#Exercise 05-04
#Josh net182 201810701580043

mark = {'Sam': 90.5,'Jane': 85.4,'Max': 92.3,'Alice': 64.5,'John': 69.4}
sum = 0
for i in mark:
    sum += mark[i]
print('Sum: '+str(sum))
print('Average: '+str(sum/len(mark)))