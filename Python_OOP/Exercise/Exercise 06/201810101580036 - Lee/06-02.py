'''
exercise:06-02
name:Lee
class:net182
'''

from tkinter import *
root = Tk()
myLabel = Frame(root)
myLabel = Label(root,text = 'Enter your name:')
myLabel.pack(side = TOP)
topFrame = Frame(root)
topFrame = Label(root,text = 'Enter your name:')
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)
entry = Entry(topFrame)
entry.pack()
Listbox = Listbox(root)
Listbox.insert(0,'Male')
Listbox.pack()
Listbox.insert(END,'Female')
Listbox.pack()
button1 = Button(bottomFrame, text = 'Show name',fg = 'red')
button2 = Button(bottomFrame, text = 'Change name',fg = 'green')
button1.pack(side = LEFT)
button2.pack(side = LEFT)
root.mainloop()