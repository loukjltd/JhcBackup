# exercise 06-03
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''


from tkinter import *
import tkinter.messagebox as ms

window = Tk()
window.title('')
window.geometry('200x100')

tx=Entry(window)
tx.pack()
tx.insert(0,'')

myLabel = Label(window, text="")
myLabel.pack()

def calcC():
    c=float(Entry.get(tx))
    f=c*9/5+32
    myLabel.config(text=str(f))
def calcF():
    f = float(Entry.get(tx))
    c = (f-32)*5/9
    myLabel.config(text=str(c))
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

bt1 = Button(window,text = 'Celsius',fg = 'red',command=calcC)
bt1.pack()
bt2 = Button(window,text = 'Fahrenheit',fg = 'green',command=calcF)
bt2.pack()
bt1.pack(side=LEFT)
bt2.pack(side=LEFT)

window.mainloop()
