# exercise06-03
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack(side = TOP)
text1 = Entry(topFrame)
text1.pack()
Label = Label(topFrame)
Label.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

def calcC():
    Celsius = Entry.get(text1)
    new_temp = (int(Celsius) - 32)/1.8
    Label.config(text = str('%.1f'%new_temp))
def calcF():
    Fahrenheit = Entry.get(text1)
    new_temp = int(Fahrenheit) * 1.8 + 32
    Label.config(text = str('%.1f'%new_temp))

button1 = Button(bottomFrame, text = 'Celsius',fg = 'red',command = calcC)
button2 = Button(bottomFrame, text = 'Fahrenheit',fg = 'green',command = calcF)
button1.pack(side = LEFT)
button2.pack(side = LEFT)

root.mainloop()
