f = open('my_word.txt', 'w')
f.write('The thing the Time Traveller held in his hand\nwas a glittering metallic '
        '\nframework,\nscarcely larger than a small clock, \nand very delicately made.')
f.close()
x = open('my_word.txt', 'r')
print(x.read())
