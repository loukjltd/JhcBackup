#exercise 14-04
'''
class: net182
studentid:201810101580038
studentname:shrek
'''
f=open('C:\yourname\myword','w')
f.write('The thing the Time Traveller held in his hand \nwas a glittering metallic\nframework, \nscarcely larger than a small clock, \nand very delicately made.')
f.close()

f=open('C:\yourname\myword','r')
print(f.read())