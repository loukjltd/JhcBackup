#Exercise4-10
'''
student name:Bruce
ID:201810701580057
class: network 182
'''

number = int(input('Please enter a number: '))
for i in range(1,number+1):
    for j in range(1,number + 1):
        result = i * j
        print(result, end = "\t")
    print('')