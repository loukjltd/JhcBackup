'''
Bank part
net182
Team:
Leader: Josh 201810701580043
Others: Vivi, Steven, Carlie, Jone, Eden
'''

import tkinter.messagebox as box
class Person:

    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day

    def show_details(self):
        return self.first_name + ' ' \
               + self.last_name + ' ' \
               + self.birth_year + ' ' \
               + self.birth_month + ' ' \
               + self.birth_day

class Bank_Account(Person):
    transactions = 0

    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day, account_id, money, account_type):
        Person.__init__(self, first_name, last_name, birth_year, birth_month, birth_day)
        self.account_id = account_id
        self.money = money
        self.account_type = account_type

    def show_details(self):
        str1 = Person.show_details(self)
        str2 = ' ' + self.account_id
        if self.account_type == '0':
            str2 += ' Regular'
        elif self.account_type == '1':
            str2 += ' Premium'
        elif self.account_type == '2':
            str2 += ' Gold'
        return str1 + str2 + ' ' + self.money

    def money_in(self, money):
        self.money = str(float(self.money) + float(money))
        return True

    def money_out(self, money):
        if float(self.money) >= float(money):
            self.money = str(float(self.money) - float(money))
            return True
        else:
            return False

class Bank_Account_Tasks:
    accounts_list = []
    file_name = './Account.txt'

    def read_data(self):
        try:
            f = open(self.file_name, 'r')
            try:
                for i in f.read().splitlines():
                    line_list = i.split(',')
                    self.accounts_list.append(Bank_Account(line_list[0],
                                                           line_list[1],
                                                           line_list[2],
                                                           line_list[3],
                                                           line_list[4],
                                                           line_list[5],
                                                           line_list[6],
                                                           line_list[7]))
            finally:
                if f:
                    f.close()
        except IOError:
            box.showinfo('Error', 'File {0} is not found.'.format(self.file_name))

    def write_data(self):
        try:
            f = open(self.file_name, 'w')
            try:
                line_list = []
                for i in self.accounts_list:
                    lines = i.first_name + ',' \
                            + i.last_name + ',' \
                            + i.birth_year + ',' \
                            + i.birth_month + ',' \
                            + i.birth_day + ',' \
                            + i.account_id + ',' \
                            + i.money + ',' \
                            + i.account_type
                    line_list.append(lines)
                for i in line_list:
                    f.write(i + '\n')
            finally:
                if f:
                    f.close()
        except IOError:
            box.showinfo('Error', 'File {0} is not found.'.format(self.file_name))

    def check_account(self, string_account_id):
        for i in self.accounts_list:
            account = i
            if account.account_id == string_account_id:
                return account
        else:
            return 0

    def put_money_in(self, string_account_id, amount):
        i = self.check_account(string_account_id)
        if i != 0:
            if i.money_in(amount):
                i.transactions += 1
                return "Success"
            else:
                return "Fail"
        else:
            box.showinfo('Error', 'Account {0} is not found.'.format(string_account_id)) #未找到账号时抛出错误

    def get_money_out(self, string_account_id, amount):
        i = self.check_account(string_account_id)
        if i != 0:
            if i.money_out(amount):
                i.transactions += 1
                return "Success"
            else:
                return "Fail"
        else:
            box.showinfo('Error', 'Account {0} is not found.'.format(string_account_id))

    def show_biggest_account(self):
        num = 0
        maxnum = self.accounts_list[0]
        for i in self.accounts_list:
            if float(i.money) > num:
                num = float(i.money)
                maxnum = i
        return maxnum.show_details()

    def most_transactions(self):
        num = 0
        maxnum = self.accounts_list[0]
        for i in self.accounts_list:
            if i.transactions > num:
                num = i.transactions
                maxnum = i
        return maxnum.show_details()

    def get_number_of_transactions(self):
        return self.add_transactions(self.accounts_list)

    def add_transactions(self, a_list):
        if len(a_list) == 0:
            return 0
        else:
            return self.add_transactions(a_list[1:]) + a_list[0].transactions

    def show_account(self, string_account_id):
        i = self.check_account(string_account_id)
        if i != 0:
            return i.show_details()
        else:
            box.showinfo('Error', 'Account {0} is not found.'.format(string_account_id))

    def delete_account(self, string_account_id):
        i = self.check_account(string_account_id)
        if i != 0:
            self.accounts_list.remove(i)
        else:
            box.showinfo('Error', 'Account {0} is not found.'.format(string_account_id))