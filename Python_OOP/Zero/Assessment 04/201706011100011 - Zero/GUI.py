from tkinter import *
from Bank import BankAccountTasks
root = Tk()
root.title("Bank Account System")
root.geometry('700x570')

topFrame = Frame(root, width='70', height='35', pady='20')
topFrame.pack(side=TOP)
frame2 = Frame(root, width='60', height='50', padx='30')
frame2.pack(side=LEFT)
frame3 = Frame(root, width='60', height='50', padx='10')
frame3.pack(side=LEFT)
frame4 = Frame(root, width='60', height='50', padx='30')
frame4.pack(side=LEFT)


myEntry = Text(topFrame, width='70', height='15')

scroll = Scrollbar(topFrame)
scroll.pack(side=RIGHT, fill=Y)
myEntry.configure(yscrollcommand=scroll.set)
myEntry.pack(side=LEFT, fill=BOTH)
scroll['command'] = myEntry.yview()
myEntry.pack()


def c():
    user = e.get()
    number = len(user)
    e.delete(number-1, END)


def enter():
    user = e.get()
    myEntry.insert(END, user)
    e.delete(0, END)
    dd = myEntry.get(index1=1.0, index2=1.30)
    ee = myEntry.get(index1=2.0, index2=2.90)
    ff = myEntry.get(index1=4.0, index2=4.70)

    if dd == 'Sho':
        if bank.check_account(user) == 1:
            i = bank.show_account(user)
            myEntry.insert(END, "\nName: " + i.first_name + " " + i.last_name + '\n')
            myEntry.insert(END, "Birthday: " + i.birth_year + "/" + i.birth_month + "/" + i.birth_day + '\n')
            myEntry.insert(END, "Account ID: " + i.account_id + '\n')
            myEntry.insert(END, "Account Type: " + i.account_type)
            myEntry.insert(END, "Money: " + i.money + '\n')
        else:
            myEntry.insert(END, "\nAccount number " + user + ' cannot be found.')
    elif dd == "Put":
        if ee == "Enter the":
            if bank.check_account(user) == 1:
                myEntry.insert(END, '\nEnter amount:' + '\n')
                #user = e.get()
                #jj = myEntry.get(index1=3.0, index2=3.4)
                #bank.put_money_in(jj, user)
                #myEntry.insert(END, user)
                #myEntry.insert(END, '\nSuccess')
            else:
                myEntry.insert(END, "\nAccount number " + user + ' cannot be found.')
        if ff == "Enter a":
            #print(ff)
            jj = myEntry.get(index1=3.0, index2=3.5)
            #print(jj)
            bank.put_money_in(jj, user)
            myEntry.insert(END, '\nSuccess')
    elif dd == "Get":
        if ee == "Enter the":
            if bank.check_account(user) == 1:
                myEntry.insert(END, '\nEnter amount:' + '\n')
            else:
                myEntry.insert(END, "\nAccount number " + user + ' cannot be found.')
        if ff == "Enter a":
            #print(ff)
            jj = myEntry.get(index1=3.0, index2=3.5)
            #print(jj)
            bank.put_money_in(jj, user)
            myEntry.insert(END, '\nSuccess')


def delete_button_click():
    little = list1.get(list1.curselection())
    bank.delete_account(list1.get(list1.curselection()))
    bank.write_data()
    list1.delete(0, END)
    f = open("files.txt", "r")
    for x in f.readlines():
        split_line = x.split(",")
        list1.insert(END, split_line[5])
    myEntry.delete('0.0', 'end')
    myEntry.insert(END, '账户')
    myEntry.insert(END, little)
    myEntry.insert(END, '删除')
    e.delete(0, END)


def put_money_in():

    myEntry.delete('0.0', 'end')
    myEntry.insert(END, 'Put money in ...' + '\n')
    myEntry.insert(END, 'Enter the account ID:' + '\n')

    """e.delete(0, END)
    jj = myEntry.get(index1=3.0, index2=3.5)
    acct_state = False

    if bank.check_account(jj) == 1:
        myEntry.insert(END, '\nEnter amount:' + '\n')
        amt = int(myEntry.get(index1=5.0, index2=END))
        bank.put_money_in(jj, amt)
        myEntry.insert(END, '\nSuccess')
    else:
        myEntry.insert(END, "\nAccount number " + jj + ' cannot be found.')"""


def get_money_out():
    myEntry.delete('0.0', 'end')
    myEntry.insert(END, 'Get money out ...' + '\n')
    myEntry.insert(END, 'Enter the account ID:' + '\n')
    e.delete(0, END)
    zyt = 2


def show_menu():
    myEntry.delete('0.0', 'end')
    myEntry.insert(1.0, '*************************************************\n')
    myEntry.insert(END, '*               Bank Account Menu               *\n')
    myEntry.insert(END, '*************************************************\n')
    myEntry.insert(END, '1.Menu\n')
    myEntry.insert(END, '2.Put money in\n')
    myEntry.insert(END, '3.Get money out\n')
    myEntry.insert(END, '4.Show account with most money\n')
    myEntry.insert(END, '5.Show account with most transactions\n')
    myEntry.insert(END, '6.Show one account\n')
    myEntry.insert(END, '7.Show all accounts\n')
    myEntry.insert(END, '8.Show total number of transactions\n')
    myEntry.insert(END, '9.Exit\n')
    f = open("./files.txt", "r")
    for x in f.readlines():
        split_line = x.split(",")
        list1.insert(END, split_line[5])


def show_account_with_most_money():
    myEntry.delete('0.0', 'end')
    myEntry.insert(END, '----------Bank account with the most money----------' + '\n')
    e.delete(0, END)
    i = bank.show_biggest_account()
    split_line = i.split(",")
    myEntry.insert(END, "Name: " + split_line[0] + " " + split_line[1] + '\n')
    myEntry.insert(END, "Birthday: " + split_line[2] + "/" + split_line[3] + "/" + split_line[4] + '\n')
    myEntry.insert(END, "Account ID: " + split_line[5] + '\n')
    myEntry.insert(END, "Account Type: " + split_line[7])
    myEntry.insert(END, "Money: " + split_line[6] + '\n')


def show_account_with_most_transactions():
    myEntry.delete('0.0', 'end')
    myEntry.insert(END, '----------Bank account with the most transactions----------' + '\n')
    e.delete(0, END)
    i = bank.most_transactions()
    split_line = i.split(",")
    myEntry.insert(END, "Name: " + split_line[0] + " " + split_line[1] + '\n')
    myEntry.insert(END, "Birthday: " + split_line[2] + "/" + split_line[3] + "/" + split_line[4] + '\n')
    myEntry.insert(END, "Account ID: " + split_line[5] + '\n')
    myEntry.insert(END, "Account Type: " + split_line[7])
    myEntry.insert(END, "Money: " + split_line[6] + '\n')


def show_one_account():
    myEntry.delete('0.0', 'end')
    myEntry.insert(END, 'Show one account ...' + '\n')
    myEntry.insert(END, 'Enter the account ID： ' + '\n')
    e.delete(0, END)
    zyt = 0
    """if bank.check_account(user) != 0:
            bank.show_account(END, user)
    else:
        myEntry.insert(END, "\nAccount number " + user + ' cannot be found.')"""


def show_all_accounts():
    myEntry.delete('0.0', 'end')
    myEntry.insert(END, 'Showing all accounts ...' + '\n')
    e.delete(0, END)
    for i in bank.accounts_list:
        myEntry.insert(END, "Name: " + i.first_name + " " + i.last_name + '\n')
        myEntry.insert(END, "Birthday: " + i.birth_year + "/" + i.birth_month + "/" + i.birth_day + '\n')
        myEntry.insert(END, "Account ID: " + i.account_id + '\n')
        #i.show_details()
        myEntry.insert(END, "Account Type: " + i.account_type)
        myEntry.insert(END, "Money: " + i.money + '\n')
        myEntry.insert(END, "---------" '\n')


def show_total_transactions():
    myEntry.delete('0.0', 'end')
    myEntry.insert(END, 'Total transactions：' + '\n')
    e.delete(0, END)
    myEntry.insert(END, bank.add_transactions(bank.accounts_list))


def exit():
    root.destroy()


button1 = Button(frame2, text="Menu", width='30', height='1', command=show_menu)
button2 = Button(frame2, text="Put money in", width='30', height='1', command=put_money_in)
button3 = Button(frame2, text="Get money out", width='30', height='1', command=get_money_out)
button4 = Button(frame2, text="Show account with most money", width='30', height='1', command=show_account_with_most_money)
button5 = Button(frame2, text="Show account with most transactions", width='30', height='1', command=show_account_with_most_transactions)
button6 = Button(frame2, text="Show one account", width='30', height='1', command=show_one_account)
button7 = Button(frame2, text="Show all accounts", width='30', height='1', command=show_all_accounts)
button8 = Button(frame2, text="Show total number of transactions", width='30', height='1',command=show_total_transactions)
button9 = Button(frame2, text="Exit", width='30', height='1', command=exit)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()


display = StringVar()
e = Entry(frame3, width=31, textvariable=display)
e.grid(row=0, column=0, columnspan=30, rowspan=2)
Button(frame3, text='1', width=9, height=3, command=lambda: e.insert(INSERT, '1')).grid(row=2, column=0, columnspan=3)
Button(frame3, text='2', width=9, height=3, command=lambda: e.insert(INSERT, '2')).grid(row=2, column=4, columnspan=3)
Button(frame3, text='3', width=9, height=3, command=lambda: e.insert(INSERT, '3')).grid(row=2, column=8, columnspan=3)
Button(frame3, text='4', width=9, height=3, command=lambda: e.insert(INSERT, '4')).grid(row=3, column=0, columnspan=3)
Button(frame3, text='5', width=9, height=3, command=lambda: e.insert(INSERT, '5')).grid(row=3, column=4, columnspan=3)
Button(frame3, text='6', width=9, height=3, command=lambda: e.insert(INSERT, '6')).grid(row=3, column=8, columnspan=3)
Button(frame3, text='7', width=9, height=3, command=lambda: e.insert(INSERT, '7')).grid(row=4, column=0, columnspan=3)
Button(frame3, text='8', width=9, height=3, command=lambda: e.insert(INSERT, '8')).grid(row=4, column=4, columnspan=3)
Button(frame3, text='9', width=9, height=3, command=lambda: e.insert(INSERT, '9')).grid(row=4, column=8, columnspan=3)
Button(frame3, text='C', width=9, height=3, command=c).grid(row=5, column=0, columnspan=3)
Button(frame3, text='0', width=9, height=3, command=lambda: e.insert(INSERT, '0')).grid(row=5, column=4, columnspan=3)
Button(frame3, text='ENTER', width=9, height=3, command=enter).grid(row=5, column=8, columnspan=3)

Label_1 = Label(frame4, text="Accounts")
Label_1.pack()
list1 = Listbox(frame4, width='16', height="8")
scroll=Scrollbar(frame4)
scroll.pack(side=RIGHT,fill=Y)
list1.configure(yscrollcommand=scroll.set)
scroll['command']=list1.yview()
list1.pack(side=LEFT,fill=BOTH)
Button_1 = Button(root, text='Delete', command=delete_button_click)
Button_1.place(x=574,y=516,anchor=W,width=60,height=50)

#Label_1 = Label(frame4, text="Accounts")
#Label_1.grid(row=0, column=0)
#list1 = Listbox(frame4, width='15', height="8")
#scroll=Scrollbar(frame4)
#scroll.grid(row=1,column=1)
#list1.configure(yscrollcommand=scroll.set)
#scroll['command']=list1.yview()
#list1.grid(row=1, column=0)
#Button_1 = Button(frame4, text='Delete', width=9, height=2, command=delete_button_click)
#Button_1.grid(row=3, column=0)

f = open("./files.txt", "r")
for x in f.readlines():
    split_line = x.split(",")
    list1.insert(END, split_line[5])
myEntry.insert(1.0, '*************************************************\n')
myEntry.insert(END, '*               Bank Account Menu               *\n')
myEntry.insert(END, '*************************************************\n')
myEntry.insert(END, '1.Menu\n')
myEntry.insert(END, '2.Put money in\n')
myEntry.insert(END, '3.Get money out\n')
myEntry.insert(END, '4.Show account with most money\n')
myEntry.insert(END, '5.Show account with most transactions\n')
myEntry.insert(END, '6.Show one account\n')
myEntry.insert(END, '7.Show all accounts\n')
myEntry.insert(END, '8.Show total number of transactions\n')
myEntry.insert(END, '9.Exit\n')

bank = BankAccountTasks()
bank.read_data()
"""for i in bank.accounts_list:
    i.show_details()"""

root.mainloop()
