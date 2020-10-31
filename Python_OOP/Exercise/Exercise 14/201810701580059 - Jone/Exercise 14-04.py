# Exercise 014-04
'''
Student Name: jone
ID: 201810701580059
Class: Network 182
'''
f=open('my_words','w')
f.write('The thing the Time Traveller held in his hand \nwas a glittering metallic\nframework, \nscarcely larger than a small clock, \nand very delicately made.')
f.close()

f=open('my_words','r')
print(f.read())