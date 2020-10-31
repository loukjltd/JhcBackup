#Exercise 06-01
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

from tkinter import *
root=Tk()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

botton1=Button(topFrame,text="Do not click the OK buttom!",fg="red")
botton2=Button(bottomFrame,text="OK",fg="green")
botton3=Button(bottomFrame,text="Cancel",fg="blue")

botton1.pack(side=LEFT)
botton2.pack(side=LEFT)
botton3.pack()
root.mainloop()
