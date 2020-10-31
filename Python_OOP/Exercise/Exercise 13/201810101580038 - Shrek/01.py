#exercise 13-01
'''
studentname:shrek
studentid:201810101580038
class:net182
'''



def countdown(n):

    if n > 10:
        print("Finished!")
    else:
        print(n)
        countdown(n+1)

countdown(1)
