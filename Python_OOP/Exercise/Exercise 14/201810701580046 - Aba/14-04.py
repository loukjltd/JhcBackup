'''
class:net182
name:Aba
ID:201810701580046
'''
f = open('D:\yourname\my_words.txt','w')
f.write('The thing the Time Traveller held in his hand was a glittering metallic\nframework,\nscarcely larger than a small clock,\nand very delicately made.')
f.close()
f = open('D:\yourname\my_words.txt','r')
print(f.read())