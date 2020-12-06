num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))
symbol = input('Please enter your symbol: ')

if symbol == '+':
    print('The answer is ' + str(num1 + num2))
elif symbol == '-':
    print('The answer is ' + str(num1 - num2))
elif symbol == '*':
    print('The answer is ' + str(num1 * num2))
elif symbol == '/':
    print('The answer is ' + str(num1 / num2))
