'''
Student Name: Eden
ID: 201810701580060
Class: Network 182
'''
word = str(input('Please enter the sentence: '))
letter = ('a', 'e', 'i', 'o', 'u')
count = 0
t = ''
for i in word:
    if i in letter:
        count += 1
        t += 'X'
    else:
        t += str(i)
print(str(t))
print('There are ' + str(count) + ' vowels in the word or sentence.')