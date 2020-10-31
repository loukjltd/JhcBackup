#Exercise 06-01
'''
Name:Assass
Class:Net182
ID:201810701580040
'''
from tkinter import *
root = Tk()
f1=Frame(root)
f1.pack(side=TOP)
f2=Frame(root)
f2.pack(side=BOTTOM)
label = Label(f1, text="Do not click the OK button!", fg="red")
label.pack()
button1 = Button(f2, text="OK", fg="green")
button1.pack(side=LEFT)
button2 = Button(f2, text="Cancel", fg="blue")
button2.pack(side=LEFT)
root.mainloop()