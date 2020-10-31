#Exercise 13-01
'''
class:net182
name:vivi
id:201810701580049
'''
def countdown(n):

    if n >= 10:
        print(n)
        print("Finished!")
    else:
        print(n)
        countdown(n+1)

countdown(1)
