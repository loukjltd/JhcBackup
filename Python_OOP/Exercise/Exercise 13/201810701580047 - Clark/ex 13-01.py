def countup(n):
    if n > 10:
        print('Finished!')
    else:
        print(n)
        countup(n+1)

countup(1)
