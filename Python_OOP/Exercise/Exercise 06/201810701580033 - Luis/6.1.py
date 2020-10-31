

# Exercise 06-01
''''
student name:Luis
ID:201810701580033
class:network 182
'''


from tkinter import *

root=tk()
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Do not click OK button', fg='red')
button2 = Button(bottonFrame, text='OK', fg='green')
button3 = Button(bottonFrame, text='Cancle', fg='blue')

button1.pack()
button2.pack()
button3.pack(side=LEFT)

root.mainloop()
