#Exercise 04-08
#Josh net182 201810701580043
vowel = ["a","e","i","o","u"]
letter = input("Please enter a word or sentence: ")
num = 0
for i in letter:
    if i in vowel:
        print("X", end = "")
        num += 1
    else:
        print(i, end ="")
print()
print("There are "+str(num)+" vowels in the word or sentence.")