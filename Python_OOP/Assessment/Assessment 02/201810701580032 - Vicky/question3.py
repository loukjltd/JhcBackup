num = int(input("Enter a number:"))
sum = 0
if num >99 and num<1000:
    a1 = num % 10
    num2 =int( num /10)
    a2 = num2 % 10
    num3 = int(num2 / 10)
    a3 = num3 % 10
    sum = a1 *a2 *a3
if num >0 and num<100:
    a1 = num % 10
    num2 = int(num / 10)
    a2 = num2 % 10
    num3 = int(num2 / 10)
    sum = a1 *a2
print("The product of all of the digits of",num,"is",sum)