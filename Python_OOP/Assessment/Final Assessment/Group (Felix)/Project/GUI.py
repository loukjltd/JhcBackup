'''
GUI part
net182
Team:Group4
'''

from tkinter import * #导入tkinter
import tkinter.messagebox as box #导入tkinter中的messagebox并赋值给box
import tkinter.scrolledtext as scrol #导入scrolledtext并赋值给scrol
from Bank import Bank_Account_Tasks #从Bank.py导入Bank_Account_Tasks类型
bank = Bank_Account_Tasks()
bank.read_data()
#window size
root = Tk()
root.title('Bank Account System')
window_width = 550
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
align = '%dx%d+%d+%d' % (window_width, window_height, (screen_width-window_width)/2, (screen_height-window_height)/2)
root.geometry(align)

#functions
account_bool = 0
account_check = 0
account_num = ''
money_bool = 0
money_in_bool = 0
def show_file(file_name):
    text_box.delete(1.0, END)
    list_box1.delete(0, END)
    try:
        f = open('./{0}.txt'.format(file_name), 'r')
        try:
            text_box.insert(END, f.read())
        finally:
            if f:
                f.close()
    except IOError:
        box.showinfo('Error', 'File {0} is not found.'.format(file_name))

def num_in(num):
    entry1.insert(END, num)

def num_clear_last():
    num = entry1.get()
    new_num = num[:-1]
    entry1.delete(0, END)
    entry1.insert(END, new_num)

def insert_list(list_name):
    if len(list_name) == 8:
        text_box.insert(END, 'Name: {0}\n'.format(list_name[0] + list_name[1]))
        text_box.insert(END, 'Birthday: {0}/{1}/{2}\n'.format(list_name[2], list_name[3], list_name[4]))
        text_box.insert(END, 'Account ID: {0}\n'.format(list_name[5]))
        text_box.insert(END, 'Account Type: {0}\n'.format(list_name[6]))
        text_box.insert(END, 'Money: {0}\n'.format(list_name[7]))
    else:
        box.showinfo('Error', 'List {0} is not found.'.format(list_name))

def enter_but():
    num1 = entry1.get()
    text_box.insert(END, num1 + '\n')
    global account_bool
    global account_num
    global account_check
    global money_bool
    global money_in_bool
    if account_bool == 1:
        if bank.check_account(num1) == 0:
            text_box.insert(END, 'Account number {0} cannot be found.\n'.format(num1))
        elif account_check == 1:
            acc_list = bank.show_account(num1).split(' ')
            insert_list(acc_list)
        else:
            text_box.insert(END, 'Enter amount:\n')
        account_bool = 0
        account_check = 0
        account_num = num1
        money_bool = 1
    elif money_bool == 1:
        result = 'Failed'
        if money_in_bool == 1:
            result = bank.put_money_in(account_num, num1)
        else:
            result = bank.get_money_out(account_num, num1)
        text_box.insert(END, result + '\n')
        money_bool = 0
    entry1.delete(0, END)

def money_in():
    global account_bool
    global account_num
    global money_bool
    global money_in_bool
    text_box.delete(1.0, END)
    entry1.delete(0, END)
    text_box.insert(END, 'Put money in …\n')
    text_box.insert(END, 'Enter the account ID:\n')
    account_bool = 1
    account_num = ''
    money_bool = 0
    money_in_bool = 1

def money_out():
    global account_bool
    global account_num
    global money_bool
    global money_in_bool
    text_box.delete(1.0, END)
    entry1.delete(0, END)
    text_box.insert(END, 'Get money out …\n')
    text_box.insert(END, 'Enter the account ID:\n')
    account_bool = 1
    account_num = ''
    money_bool = 0
    money_in_bool = 0

def show_most_m():
    text_box.delete(1.0, END)
    entry1.delete(0, END)
    text_box.insert(END, '----------Bank account with the most money----------\n')
    acc_list = bank.show_biggest_account().split(' ')
    insert_list(acc_list)

def show_most_t():
    text_box.delete(1.0, END)
    entry1.delete(0, END)
    text_box.insert(END, '----------Bank account with the most transactions----------\n')
    acc_list = bank.most_transactions().split(' ')
    insert_list(acc_list)

def show_one_account():
    global account_bool
    global account_num
    global account_check
    text_box.delete(1.0, END)
    entry1.delete(0, END)
    text_box.insert(END, 'Show one account …\n')
    text_box.insert(END, 'Enter the account ID:\n')
    account_bool = 1
    account_check = 1
    account_num = ''

def show_all_account():
    text_box.delete(1.0, END)
    entry1.delete(0, END)
    text_box.insert(END, 'Showing all accounts …\n')
    for acc in bank.accounts_list:
        acc_list = bank.show_account(acc.account_id).split(' ')
        insert_list(acc_list)
        text_box.insert(END, '---------\n')

def show_total():
    text_box.delete(1.0, END)
    entry1.delete(0, END)
    text_box.insert(END, 'Total transactions:\n')
    noft = bank.get_number_of_transactions()
    text_box.insert(END, '{0}\n'.format(noft))

def delete_account():
    acc = list_box1.get(ACTIVE)
    list_box1.delete(acc)
    text_box.delete(1.0, END)
    entry1.delete(0, END)
    bank.delete_account(acc)
    text_box.insert(END, 'Account {0} deleted.\n'.format(acc))

def exit_file():
    bank.write_data()
    exit(0)
#top part
top_frame = Frame(root)
top_frame.pack(side=TOP)
lab_title = Label(top_frame, text='Bank Account System')
lab_title.pack()

#main part
text_box = scrol.ScrolledText(root)
text_box.place(x=20, y=20, width=520, height=200)

#left button
but_menu = Button(root, text='Menu', command=lambda: show_file('Menu'))
but_menu.place(x=20, y=250, width=220, height=30)
but_money_in = Button(root, text='Put money in', command=money_in)
but_money_in.place(x=20, y=280, width=220, height=30)
but_money_out = Button(root, text='Get money out', command=money_out)
but_money_out.place(x=20, y=310, width=220, height=30)
but_show_most_m = Button(root, text='Show account with most money', command=show_most_m)
but_show_most_m.place(x=20, y=340, width=220, height=30)
but_show_most_t = Button(root, text='Show account with most transactions', command=show_most_t)
but_show_most_t.place(x=20, y=370, width=220, height=30)
but_show_one = Button(root, text='Show one account', command=show_one_account)
but_show_one.place(x=20, y=400, width=220, height=30)
but_show_all = Button(root, text='Show all accounts', command=show_all_account)
but_show_all.place(x=20, y=430, width=220, height=30)
but_show_total = Button(root, text='Show total number of transactions', command=show_total)
but_show_total.place(x=20, y=460, width=220, height=30)
but_exit = Button(root, text='Exit', command=exit_file)
but_exit.place(x=20, y=490, width=220, height=30)

#number and entry
entry1 = Entry(root)
entry1.place(x=250, y=250, width=150, height=20)
but_num1 = Button(root, text='1', command=lambda: num_in('1'))
but_num1.place(x=250, y=300, width=50, height=50)
but_num2 = Button(root, text='2', command=lambda: num_in('2'))
but_num2.place(x=300, y=300, width=50, height=50)
but_num3 = Button(root, text='3', command=lambda: num_in('3'))
but_num3.place(x=350, y=300, width=50, height=50)
but_num4 = Button(root, text='4', command=lambda: num_in('4'))
but_num4.place(x=250, y=350, width=50, height=50)
but_num5 = Button(root, text='5', command=lambda: num_in('5'))
but_num5.place(x=300, y=350, width=50, height=50)
but_num6 = Button(root, text='6', command=lambda: num_in('6'))
but_num6.place(x=350, y=350, width=50, height=50)
but_num7 = Button(root, text='7', command=lambda: num_in('7'))
but_num7.place(x=250, y=400, width=50, height=50)
but_num8 = Button(root, text='8', command=lambda: num_in('8'))
but_num8.place(x=300, y=400, width=50, height=50)
but_num9 = Button(root, text='9', command=lambda: num_in('9'))
but_num9.place(x=350, y=400, width=50, height=50)
but_c = Button(root, text='c', command=num_clear_last)
but_c.place(x=250, y=450, width=50, height=50)
but_num0 = Button(root, text='0', command=lambda: num_in('0'))
but_num0.place(x=300, y=450, width=50, height=50)
but_enter = Button(root, text='ENTER', command=enter_but)
but_enter.place(x=350, y=450, width=50, height=50)



#account list and delete
lab1 = Label(root, text='Accounts:')
lab1.place(x=430, y=250, width=80, height=20)
list_box1 = Listbox(root)
list_box1.place(x=410, y=270, width=120, height=200)
scroll = Scrollbar(root)
scroll.place(x=530, y=270, width=20, height=200)
but_delete = Button(root, text='Delete',command=delete_account)
but_delete.place(x=430, y=480, width=80, height=30)
list_box1.config(yscrollcommand=scroll.set)
scroll.config(command=list_box1.yview)
for i in bank.accounts_list:
    list_box1.insert(END, i.account_id)
#keep window
root.mainloop()