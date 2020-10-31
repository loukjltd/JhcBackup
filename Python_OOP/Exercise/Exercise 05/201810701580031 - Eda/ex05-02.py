# exercise 05-02
'''
student name: Eda
ID: 201810701580031
class: network182
'''

n = int(input("Enter the number of values to insert:"))
my_list = []

for a in range(0,n):
    get_num = int(input("Enter a number to insert:"))
    my_list.append(get_num)
sum = sum(my_list)
average =sum / n
print('Sum is: '+ str(sum))
print('Average is: ' + str(average))