# Exercise 04-08
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
word = str(input('please enter a word or sentence:'))
count = 0
for m in word:
    if m=='a' or m=='e' or m=='i' or m=='o' or m=='u':
        m = 'X'
        count +=1
    print(m,end='')
print('')
print('There are '+ str(count) + ' vowels in the word or sentence.')