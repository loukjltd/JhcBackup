# exercise04-08
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
word = str(input("Enter a word or sentence:"))
num=["a","e","i","o","u"]
count = 0
for i in word :
    if i in num:
        print ("X",end ="")
        count += 1
    else :
        print(i,end ="")
print()
print('There are ' + str(count) + ' vowels in the word or sentence.')
