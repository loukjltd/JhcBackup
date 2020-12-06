def login(username, password):
    username = str(input('Please enter your username: '))
    password = str(input('Please enter your password: '))
    if password == '123456':
        print('Welcome! ' + username)


enterUser = ''
enterPass = ''
login(enterUser, enterPass)
