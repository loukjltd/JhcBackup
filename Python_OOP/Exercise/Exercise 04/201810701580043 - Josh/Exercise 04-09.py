#Exercise 04-09
#Josh net182 201810701580043

s = input("Please enter a word or sentence:")
for i in s:
    if i == "x":
        print('This has the letter \'x\' in it')
        break
else:
    print('This does not have the letter \'x\' in it')