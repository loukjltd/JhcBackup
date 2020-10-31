# exercise06-01
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
from tkinter import *
root = Tk()
topFrame = Frame(root)
topFrame = Label(root,text = 'Do not click the OK button!',fg = 'red')
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)
button1 = Button(bottomFrame, text = 'OK',fg = 'green')
button2 = Button(bottomFrame, text = 'Cancel',fg = 'blue')
button1.pack(side = LEFT)
button2.pack(side = LEFT)
root.mainloop()
