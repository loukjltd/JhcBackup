'''
name:leo
id:201810701580053
class:net182
'''
from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame = Label(root,text= "Do not click the ok button " )
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame, text="OK", fg="red")
button2 = Button(bottomFrame, text="Cancel", fg="blue")



button1.pack(side=LEFT)
button2.pack(side=LEFT)


root.mainloop()
