# exercise05-02
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
n=int(input("Enter the number of values to insert: "))
my_list=[]
for i in range(n) :
    get_num = int(input("Enter a number to insert: "))
    my_list.append(get_num)
sum = sum(my_list)
average = sum/len(my_list)
print("sum is:"+ str(sum))
print("Average is:"+ str(average))
