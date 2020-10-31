'''
class:net182
name:Assass
id:201810710580040
'''
import re as re
f = open("./my_words.txt ", "w")
w='The thing the Time Traveller held in his hand was a glittering metallic\nframework,\nscarcely larger than a small clock,\nand very delicately made.'
f.write(w)
f.close()
f = open("./my_words.txt ", "r")
print(f.read())