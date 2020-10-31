#Exercise 06-03
#Josh net182 201810701580043

from tkinter import *
import tkinter.messagebox as box
# make up the window
root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
# functions
def calcC():
    try:
        tempC = float(en1.get())
        tempF = 32 + tempC*1.8
        lab1.config(text=str(tempF))
    except:
        box.showinfo('Error','A invalid value.')

def calcF():
    try:
        tempF = float(en1.get())
        tempC = (tempF - 32)/1.8
        lab1.config(text=str(tempC))
    except:
        box.showinfo('Error','A invalid value.')

# main
en1 = Entry(topFrame)
en1.pack()

lab1 = Label(topFrame, text='')
lab1.pack()

butt1 = Button(bottomFrame, text = 'Celsius', command = calcC, fg = 'red')
butt1.pack(side=LEFT)

butt2 = Button(bottomFrame, text = 'Fahrenheit', command = calcF, fg = 'green')
butt2.pack(side=LEFT)
root.mainloop()