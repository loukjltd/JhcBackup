'''
student name:Bruce
ID:201810701580057
class: network 182
'''

from tkinter import *

root = Tk()

def calcC():
    num1 = float(Entry.get(user_text))
    new_temp1 = (num1-32)/1.8
    mylabel.config(text=str(new_temp1))

def calcF():
    num2 = float(Entry.get(user_text))
    new_temp2 = num2*1.8 + 32
    mylabel.config(text=str(new_temp2))

user_text = Entry(root)
user_text.pack(side=TOP)

mylabel = Label(root, text='')
mylabel.pack()

button1 = Button(root, text='Celsius', fg='red',command=calcC)
button2 = Button(root, text='Fahrenheit', fg='green', command=calcF)
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()