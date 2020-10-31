# exercise06-02
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
from tkinter import *
root = Tk()

myLabel = Frame(root)
myLabel = Label(root,text = 'Enter your name:')
myLabel.pack(side = TOP)

topFrame = Frame(root)
topFrame.pack()
entry = Entry(topFrame)
entry.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)
Listbox = Listbox(bottomFrame)
Listbox.insert(0,'Male')
Listbox.insert(END,'Female')
Listbox.pack()

def printName():
    import tkinter.messagebox
    tkinter.messagebox.showinfo('My name',entry.get())

button1 = Button(bottomFrame, text = 'Show name',fg = 'red',command = printName)
button2 = Button(bottomFrame, text = 'Change name',fg = 'green')
button1.pack(side = LEFT)
button2.pack(side = LEFT)

root.mainloop()
