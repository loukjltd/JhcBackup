#Exercise 04-10
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

user = int(input("Enter the number for the times table: "))
user = user + 1
for i in range(1,user):
    for j in range(1,user):
        print("%2d" % (i*j),end = "\t")
    print()