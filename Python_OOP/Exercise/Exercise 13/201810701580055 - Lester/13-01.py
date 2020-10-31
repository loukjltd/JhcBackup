def countdown(n):
    if n == 10:
        print(n)
        return ("Finished!")

    elif n != 10:
        print(n)
        countdown(n+1)

countdown(1)
