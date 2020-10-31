'''
exercise:06-03
name:jone
class:net182
student id:201810701580059
'''

from tkinter import *
def calcC():
    Celsius = Entry.get(myLabel1)
    new_temp = (int(Celsius) - 32)/1.8
    myLabel2.config(text=str('%.1f'%new_temp))
def calcF():
    Fahrenheit = Entry.get(myLabel1)
    new_temp = int(Fahrenheit) * 1.8 + 32
    myLabel2.config(text = str('%.1f'%new_temp))
root = Tk()
topFrame = Frame(root)
topFrame = Label()
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)
myLabel1 = Label(root,text = 'enter your number:')
myLabel1 = Entry(root)
myLabel1.pack(side = TOP)
myLabel2 = Frame(root)
myLabel2 = Label(root)
myLabel2.pack()
button1 = Button(bottomFrame, text = 'Celsius',fg = 'red',command = calcC)
button2 = Button(bottomFrame, text = 'Fahrenheit',fg = 'green',command = calcF)
button1.pack(side = LEFT)
button2.pack(side = LEFT)
root.mainloop()