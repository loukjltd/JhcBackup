from tkinter import *


root = Tk()

topFrame = Frame(root)
topFrame.pack()

myLabel = Label(topFrame, text="Do not click the OK buton",fg = 'red')
myLabel.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame, text="OK", fg="green")
button2 = Button(bottomFrame, text="Cancel", fg="blue")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
root.mainloop()