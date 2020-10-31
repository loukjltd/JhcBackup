# exercise 14-02
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
f = open("D:\drive\my_text2.txt", "r")
my_numbers = []

for x in f.readlines():
    my_numbers.append(int(x))


print("sum:",sum(my_numbers))
