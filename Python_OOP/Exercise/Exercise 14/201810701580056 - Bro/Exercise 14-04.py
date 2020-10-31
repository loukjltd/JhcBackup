# exercise 14 04
'''
Bro
201810701580056
network 182
'''
f=open('.\my_words','w')
f.write('The thing the Time Traveller held in his hand \nwas a glittering metallic\nframework, \nscarcely larger than a small clock, \nand very delicately made.')
f.close()

f=open('.\my_words','r')
print(f.read())