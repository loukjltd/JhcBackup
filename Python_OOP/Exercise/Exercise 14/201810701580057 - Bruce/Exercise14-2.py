'''
student name :Bruce
ID:201810701580057
class:network 182
'''
f = open("D:\my_text2.txt", "r")
my_numbers = []

for x in f.readlines():
    my_numbers.append(int(x))


print('Sum: ',sum(my_numbers))
