#
'''
class:net182
name:lenny
ID:201810701580045
'''
def countdown(n):

    if n >= 11:
        print('Finished!')
    else:
        print(n)
        countdown(n+1)

countdown(1)