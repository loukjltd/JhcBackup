# exercise14-04
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
f=open('my_words','w')
f.write('The thing the Time Traveller held in his hand \nwas a glittering metallic\nframework, \nscarcely larger than a small clock, \nand very delicately made.')
f.close()

f=open('my_words','r')
print(f.read())
