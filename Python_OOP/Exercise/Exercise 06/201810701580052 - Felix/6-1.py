#exercise 06-01
'''
student name:Felix
class:net182
student id:201810701580052
'''
from tkinter import  *
root = Tk()

topframe = Frame(root)
topframe = Label(root,text='Do not click the Ok button!',fg='red')
topframe.pack(side=TOP)


bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
button1 = Button(bottomframe,text='ok',fg='green')
button2 = Button(bottomframe,text='cancel',fg='blue')
button1.pack(side=LEFT)
button2.pack(side=LEFT)
root.mainloop()

