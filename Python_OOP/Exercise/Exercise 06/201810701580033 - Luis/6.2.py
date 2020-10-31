

# Exercise 06-02
''''
student name:Luis
ID:201810701580033
class:network 182
'''

from tkinter import *
import tkinter.messagebox as ms
root=Tk()
tx1=Entry(root)
tx1.pack()
MyLable=Label(root,text='Enter your name')
MyLable.pack()
tx1.insert(0,'')

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
def showname():
    name=Entry.get(tx1)
    ms.showinfo('My name', name)

def changename():
    tx1.delete(0, END)
    ms.showinfo('My name', 'My name is Sam.')

listbox = Listbox(root)
listbox.insert(END,'Male')
listbox.insert(END,'Female')
listbox.pack()

button1 = Button(bottomFrame, text='show name', fg='red',command=showname)
button2 = Button(bottomFrame, text='change name', fg='green',command=changename)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
root.mainloop()
