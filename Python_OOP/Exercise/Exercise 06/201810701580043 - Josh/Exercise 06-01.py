#Exercise 06-01
#Josh net182 201810701580043
from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame, text="OK", fg="green")
button2 = Button(bottomFrame, text="Cancel", fg="blue")
lab1 = Label(topFrame, text="Do not click the OK button!", fg='red')
button1.pack(side=LEFT)
button2.pack(side=LEFT)
lab1.pack()

root.mainloop()
