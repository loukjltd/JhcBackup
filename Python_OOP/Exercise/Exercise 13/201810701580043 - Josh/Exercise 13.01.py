#Exercise 13-01
#Josh net182 201810701580043

def countdown(n):

    if n >= 10:
        print(n)
        print("Finished!")
    else:
        print(n)
        countdown(n+1)

countdown(1)
