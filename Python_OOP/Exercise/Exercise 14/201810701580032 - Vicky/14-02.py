#Exercise 14-02
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

f = open("./my_text2.txt", "r")

my_numbers = []

for x in f.readlines():
    my_numbers.append(int(x))


print("sum:",sum(my_numbers))
