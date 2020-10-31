# exercise 06-03
'''
student name:Felix
class:net182
student id:201810701580052
'''
from tkinter import *
root = Tk()

temperature = Entry(root)
temperature.pack()

lab = Label(root,text='')
lab.pack()

def calcC():
    c = float(Entry.get(temperature))
    new_temp = (c - 32) / 1.8
    lab.config(text=str(new_temp))
def calcF():
    f = float(Entry.get(temperature))
    new_temp = f*1.8+32
    lab.config(text=str(new_temp))

cbutton = Button(root,text = 'Celsius',fg = 'red' ,command = calcC )
fbutton = Button(root,text = 'Fahrenheit',fg = 'green' ,command = calcF )
cbutton.pack(side=LEFT)
fbutton.pack(side=LEFT)


root.mainloop()





root.mainloop()