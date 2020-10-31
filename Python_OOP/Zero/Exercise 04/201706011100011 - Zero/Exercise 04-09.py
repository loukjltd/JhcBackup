#net171 Zero

word=input("Please enter a word or sentence:")
a=0
b=len(word)
for i in word:
    if i=="x":
        print("This has the letter 'x' in it")
        break
    else:
        a=a+1
if a==b:
    print("This does not have the letter 'x' in it")