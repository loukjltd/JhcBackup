# Exercise 014-04
'''
name: King
idnumber: 201810701580054
class: net182
'''
f=open('f:\python\my_words','w')
f.write('The thing the Time Traveller held in his hand \nwas a glittering metallic\nframework, \nscarcely larger than a small clock, \nand very delicately made.')
f.close()

f=open('f:\python\my_words','r')
print(f.read())