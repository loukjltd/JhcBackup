# exercise 04 09
'''
Bro
201810701580056
network 182
'''
message = str(input('please enter a word or sentence:'))
for i in message:
    if i == 'x':
        print('This has the letter \'x\' in it')
        break
else:
    print('This dose not has the letter \'x\' in it')
