#net171 Zero

word=input("write a word or sentence:")
n=0
for i in word:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        i="X"
        n=n+1
        print(i,end="")
    else:
        print(i,end="")
print()
print("There are",n,"vowels in the word or sentence. ")