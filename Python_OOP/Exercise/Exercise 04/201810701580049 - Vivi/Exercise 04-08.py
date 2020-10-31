#Exercise 04-08
'''
class:net182
name:vivi
id:201810701580049
'''
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
