# Exercise 06-03
'''
name:Clark
class:net182
I  D:201810701580047
'''
from tkinter import *
root = Tk()
root.title('ex 06-03')
# 框架
insertF = Frame(root)
insertF.pack()
lF = Frame(root)
lF.pack()
bF = Frame(root)
bF.pack()
#函数


def celsius():
    temperature = 5/9*(float(Entry.get(insert))-32)
    label.config(text=str(temperature))


def fahrenheit():
    temperature = 9/5*(float(Entry.get(insert))+32)
    label.config(text=str(temperature))


# 控件
text = Text(insertF)
text.pack()
insert = Entry(text)
insert.pack()
label = Label(lF)
label.pack()
celsius = Button(bF, text='Celsius', fg='red', command=celsius)
celsius.pack()
fahrenheit = Button(bF, text='Fahrenheit', fg='green', command=fahrenheit)
fahrenheit.pack()
root.mainloop()
