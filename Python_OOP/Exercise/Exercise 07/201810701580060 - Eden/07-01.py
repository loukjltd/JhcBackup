'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
a = 3
b = 5
c = 9
def max_num(a,b,c):
    if a > b:
        largest = a
    else:
        largest = b

    if c > largest:
        largest = c

    return largest

print(input("Maximun number is  " + str(max_num(a,b,c))))
