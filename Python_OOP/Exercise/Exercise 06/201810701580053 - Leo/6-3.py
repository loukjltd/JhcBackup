from tkinter import * # get everything in tkinter module
import tkinter.messagebox # import the messagebox class

root = Tk() # make an empty window object

mylabel = Label(root, text="")
mylabel.pack()
entry1 = Entry(root)
entry1.pack()

def calcC():
    entry2 = Entry.get(entry1)
    new_temp = int(entry2)-32/1.8
    mylabel.config(text=str(new_temp))

def calcF():
    entry2 = Entry.get(entry1)
    new_temp = int(entry2)*1.8+32
    mylabel.config(text=str(new_temp))

button1 = Button(root, text="Celsius ", fg="red",command = calcC)
button2 = Button(root, text="Fahrenheit", fg="green",command = calcF)
button1.pack()
button2.pack()


root.mainloop()
