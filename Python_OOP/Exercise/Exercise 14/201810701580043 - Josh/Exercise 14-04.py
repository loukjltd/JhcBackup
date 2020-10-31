#Exercise 14-04
#Josh net182 201810701580043

try:
    f = open('./my_words.txt', 'w')
    f.write('The thing the Time Traveller held in his hand was a glittering metallic \nframework, \nscarcely larger than a small clock, \nand very delicately made.')
    f.close()
    fr = open('./my_words.txt', 'r')
    print(fr.read())
except IOError as my_error:
    print('Not found. ', my_error)
    exit(0)
finally:
    if f:
        f.close()
    if fr:
        fr.close()