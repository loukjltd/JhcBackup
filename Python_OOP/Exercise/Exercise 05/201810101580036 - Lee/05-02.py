'''
class:net182
name:Lee
ID:201810101580036
'''
n = int(input('Enter the number of values to insert: '))

mylist = []

for i in range(0,n):
    get_num = int(input('Enter a number to insert: '))
    mylist.append(get_num)

print('Sum is : ',sum(mylist))
print('Average is : ',(sum(mylist)/n))