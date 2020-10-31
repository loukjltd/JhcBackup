#Exercise 06-01
'''
class net182
id 2018100701580049
name vivi
'''
from tkinter import * # get everything in tkinter module
root = Tk() # make an empty window object
myLabel = Label(root, text="Do not click the OK button!") #
# make some text, put it in the window
myLabel.pack() # put the text in the window
# make the top frame
topFrame = Frame(root)
topFrame.pack()
# make the bottom frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) # put it at the bottom


# make 4 buttons. The first 3 are in the top frame
# and button 4 is in the bottom frame
button1 = Button(topFrame, text="OK", fg="green")
button2 = Button(topFrame, text="Cancel", fg="blue")

# make the buttons show
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()
