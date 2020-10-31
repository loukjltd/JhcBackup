# exercise 13 01
'''
Bro
201810701580056
network 182
'''
def countdown(n):

    if n > 10:
        print("Finished!")
    else:
        print(n)
        countdown(n+1)

countdown(1)
