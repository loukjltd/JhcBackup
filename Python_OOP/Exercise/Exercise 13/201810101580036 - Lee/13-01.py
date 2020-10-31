'''
name:Lee
class:net182
ID:201810101580036
'''
def countdown(n):
    if n > 10:
        print('Finished!')
    else:
        print(n)
        countdown(n + 1)
countdown(1)