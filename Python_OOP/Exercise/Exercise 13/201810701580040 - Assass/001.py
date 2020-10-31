'''
Class:Net182
Name:Assass
ID:201810701580040
'''
def countdown(x):
    if x >10:
        print('Finished!')
    else:
        print(x)
        countdown(x+1)
countdown(1)