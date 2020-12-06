import random as rdm
import matplotlib.pyplot as mp_plt
import matplotlib.image as mp_img

print('This is a lovely frog, why not give it a name?')
frogName = str(input('Please type your frog\'s name here: '))
print('Sure, your frog\'s name is ' + frogName + '.' + '\n')

imgTower = mp_img.imread('image/入道崎灯塔.jpeg')
imgLetter = mp_img.imread('image/写信.jpeg')
imgWood = mp_img.imread('image/削木头.jpeg')
imgDoze = mp_img.imread('image/发呆.jpeg')
imgNoodle = mp_img.imread('image/吃拉面.jpeg')
imgHamburger = mp_img.imread('image/吃汉堡.jpeg')
imgCity = mp_img.imread('image/名古屋城.jpeg')
imgTemple = mp_img.imread('image/善光寺.jpeg')
imgBridge = mp_img.imread('image/天桥立.jpeg')
imgBook = mp_img.imread('image/看书.jpeg')
imgSleep = mp_img.imread('image/睡觉.jpeg')
imgWater = mp_img.imread('image/草津温泉.jpeg')

homePoint = rdm.randint(101, 102)
home = {101: 'is at home', 102: 'isn\'t at home'}

actionPoint = rdm.randint(1, 8)

action = {1: 'eating', 2: 'sleeping', 3: 'dozing', 4: 'cutting the wood', 5: 'writing letter',
          6: 'reading book', 7: 'travelling', 8: 'sending postcard'}
food = {11: 'noodles', 12: 'hamburgers'}
people = {51: 'butterfly', 52: 'snail', 53: 'crab'}
book = {61: 'A Dream in Red Mansions', 62: 'Jane Eyre', 63: 'A Brief History of Time',
        64: 'No Longer Human'}
view = {71: 'Nagoya Castle', 72: 'Miyazu Amano Hashidate', 73: 'Kusatsu Onsen',
        74: 'Nyudozaki Tower', 75: 'Zenko-ji Temple'}

if homePoint == 101:
    print('Your frog, ' + frogName + ' ' + home[homePoint] + '!')

    print('It is ' + action[actionPoint] + ' now!')

    if actionPoint == 1:
        foodPoint = rdm.randint(11, 12)
        print('It is eating ' + food[foodPoint] + '.')
        if foodPoint == 11:
            mp_plt.imshow(imgNoodle)
            mp_plt.axis('off')
            mp_plt.show()
        elif foodPoint == 12:
            mp_plt.imshow(imgHamburger)
            mp_plt.axis('off')
            mp_plt.show()

    elif actionPoint == 2:
        mp_plt.imshow(imgSleep)
        mp_plt.axis('off')
        mp_plt.show()

    elif actionPoint == 3:
        mp_plt.imshow(imgDoze)
        mp_plt.axis('off')
        mp_plt.show()

    elif actionPoint == 4:
        mp_plt.imshow(imgWood)
        mp_plt.axis('off')
        mp_plt.show()

    elif actionPoint == 5:
        peoplePoint = rdm.randint(51, 53)
        print('It is writing letter to ' + people[peoplePoint] + '.')
        mp_plt.imshow(imgLetter)
        mp_plt.axis('off')
        mp_plt.show()

    elif actionPoint == 6:
        bookPoint = rdm.randint(61, 64)
        print('It is reading a book called ' + book[bookPoint] + '.')
        mp_plt.imshow(imgBook)
        mp_plt.axis('off')
        mp_plt.show()

    elif actionPoint == 8:
        mp_plt.imshow(imgLetter)
        mp_plt.axis('off')
        mp_plt.show()

elif homePoint == 102:
    print('Your frog, ' + frogName + ' ' + home[homePoint] + '!')
    viewPoint = rdm.randint(71, 75)
    print('It is travelling to ' + view[viewPoint] + '.')
    if viewPoint == 71:
        mp_plt.imshow(imgCity)
        mp_plt.axis('off')
        mp_plt.show()

    elif viewPoint == 72:
        mp_plt.imshow(imgBridge)
        mp_plt.axis('off')
        mp_plt.show()

    elif viewPoint == 73:
        mp_plt.imshow(imgWater)
        mp_plt.axis('off')
        mp_plt.show()

    elif viewPoint == 74:
        mp_plt.imshow(imgTower)
        mp_plt.axis('off')
        mp_plt.show()

    elif viewPoint == 75:
        mp_plt.imshow(imgTemple)
        mp_plt.axis('off')
        mp_plt.show()
