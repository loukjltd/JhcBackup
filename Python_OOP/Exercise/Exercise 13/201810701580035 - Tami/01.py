'''class;net182
id address;201810701580035
name;tami'''

def countdown(n):

    if n >= 10:
        print("Finished!")
    else:
        print(n)
        countdown(n+1)

countdown(1)
