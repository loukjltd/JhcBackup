#Exercise 14-04
"""
class:net182
name:vivi
id:201810701580049
"""
text = '''The thing the Time Traveller held in his hand was a glittering metallic
framework,
scarcely larger than a small clock,
and very delicately made.'''
f1 = open("my_words.txt", "w")
try:
    f1.write(text)
    f1.close()
except IOError as e:
    print("The file cannot be found")
    if f1:
        f1.close()



f2 = open("my_words.txt", "r")
try:
    print(f2.read())
    f2.close()
except IOError as my_err:
    print("The file cannot be found")
    if f2:
        f2.close()
exit(0)

