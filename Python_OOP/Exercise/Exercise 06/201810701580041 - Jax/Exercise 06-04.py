#Exercise 06-04
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

from tkinter import *
cac = Tk()
cac.title('Calculator')
cac.geometry('450x450')
cac.resizable(0, 0)
progress = []

myFrame1 = Frame(cac)
myFrame1.pack()
myFrame2 = Frame(cac)
myFrame2.pack()
myFrame3 = Frame(cac)
myFrame3.pack()
myFrame4 = Frame(cac)
myFrame4.pack()
myFrame5 = Frame(cac)
myFrame5.pack()
myFrame6 = Frame(cac)
myFrame6.pack()

myText = Entry(myFrame1, width=25, font=("Arial", 16))
myText.pack()
myText.insert(0, 'Please enter')

myLabel = Label(myFrame2, text='', font=("Arial", 16))
myLabel.pack()

def button1():
    myText.delete(0, END)
    myText.insert(0, '1')
    progress.append(1)

def button2():
    myText.delete(0, END)
    myText.insert(0, '2')
    progress.append(2)

def button3():
    myText.delete(0, END)
    myText.insert(0, '3')
    progress.append(3)

def button4():
    myText.delete(0, END)
    myText.insert(0, '4')
    progress.append(4)

def button5():
    myText.delete(0, END)
    myText.insert(0, '5')
    progress.append(5)

def button6():
    myText.delete(0, END)
    myText.insert(0, '6')
    progress.append(6)

def button7():
    myText.delete(0, END)
    myText.insert(0, '7')
    progress.append(7)

def button8():
    myText.delete(0, END)
    myText.insert(0, '8')
    progress.append(8)

def button9():
    myText.delete(0, END)
    myText.insert(0, '9')
    progress.append(9)

def button0():
    myText.delete(0, END)
    myText.insert(0, '0')
    progress.append(0)

def buttonAdd():
    progress.append('+')

def buttonSubtract():
    progress.append('-')

def buttonMultiply():
    progress.append('*')

def buttonDivide():
    progress.append('/')

def buttonSqr():
    result = str((progress[0]) ** 0.5)
    myText.delete(0, END)
    myText.insert(0, result)

def buttonEqual():
    if progress[1] == '+':
        result = str(progress[0] + progress[2])
        myText.delete(0, END)
        myText.insert(0, result)
    elif progress[1] == '-':
        result = str(progress[0] - progress[2])
        myText.delete(0, END)
        myText.insert(0, result)
    elif progress[1] == '*':
        result = str(progress[0] * progress[2])
        myText.delete(0, END)
        myText.insert(0, result)
    elif progress[1] == '/':
        result = str(progress[0] / progress[2])
        myText.delete(0, END)
        myText.insert(0, result)

myButton1 = Button(myFrame3, text='1', width=5, height=2, font=("Arial", 16), command=button1)
myButton1.pack(side=LEFT)
myButton2 = Button(myFrame3, text='2', width=5, height=2, font=("Arial", 16), command=button2)
myButton2.pack(side=LEFT)
myButton3 = Button(myFrame3, text='3', width=5, height=2, font=("Arial", 16), command=button3)
myButton3.pack(side=LEFT)
myButtonAdd = Button(myFrame3, text='+', width=5, height=2, font=("Arial", 16), command=buttonAdd)
myButtonAdd.pack(side=LEFT)

myButton4 = Button(myFrame4, text='4', width=5, height=2, font=("Arial", 16), command=button4)
myButton4.pack(side=LEFT)
myButton5 = Button(myFrame4, text='5', width=5, height=2, font=("Arial", 16), command=button5)
myButton5.pack(side=LEFT)
myButton6 = Button(myFrame4, text='6', width=5, height=2, font=("Arial", 16), command=button6)
myButton6.pack(side=LEFT)
myButtonSubtract = Button(myFrame4, text='-', width=5, height=2, font=("Arial", 16), command=buttonSubtract)
myButtonSubtract.pack(side=LEFT)

myButton7 = Button(myFrame5, text='7', width=5, height=2, font=("Arial", 16), command=button7)
myButton7.pack(side=LEFT)
myButton8 = Button(myFrame5, text='8', width=5, height=2, font=("Arial", 16), command=button8)
myButton8.pack(side=LEFT)
myButton9 = Button(myFrame5, text='9', width=5, height=2, font=("Arial", 16), command=button9)
myButton9.pack(side=LEFT)
myButtonMultiply = Button(myFrame5, text='*', width=5, height=2, font=("Arial", 16), command=buttonMultiply)
myButtonMultiply.pack(side=LEFT)

myButtonEqual = Button(myFrame6, text='=', width=5, height=2, font=("Arial", 16), command=buttonEqual)
myButtonEqual.pack(side=LEFT)
myButton0 = Button(myFrame6, text='0', width=5, height=2, font=("Arial", 16), command=button0)
myButton0.pack(side=LEFT)
myButtonSqr = Button(myFrame6, text='√', width=5, height=2, font=("Arial", 16), command=buttonSqr)
myButtonSqr.pack(side=LEFT)
myButtonDivide = Button(myFrame6, text='/', width=5, height=2, font=("Arial", 16), command=buttonDivide)
myButtonDivide.pack(side=LEFT)

cac.mainloop()