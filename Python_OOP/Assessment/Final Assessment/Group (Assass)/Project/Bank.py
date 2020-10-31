class Person:
    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day

    def show_details(self):
        print('Name: %s %s' % (self.first_name, self.last_name))
        print('Birthday: %s/%s/%s' % (self.birth_year, self.birth_month, self.birth_day))


class Bank_Account(Person):
    transaction = 0

    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day, account_id, money, account_type):
        Person.__init__(self, first_name, last_name, birth_year, birth_month, birth_day)
        self.account_id = account_id
        self.money = float(money)
        self.account_type = account_type

    def show_details(self):
        a = 0
        x = 'Name: %s %s\n' % (self.first_name, self.last_name)
        y = 'Birthday: %s/%s/%s\n' % (self.birth_year, self.birth_month, self.birth_day)
        z = 'Account ID: %s\n' % self.account_id
        if self.account_type == '0':
            a = 'Account Type: Regular\n'
        elif self.account_type == '1':
            a = 'Account Type: Premium\n'
        elif self.account_type == '2':
            a = 'Account Type: Gold\n'
        b = 'Money: %s\n' % self.money
        x = x+y+z+a+b
        return x

    def money_in(self, money):
        self.money += money
        Bank_Account.transaction += 1
        return True

    def money_out(self, money):
        if self.money - money >= 0:
            self.money -= money
            Bank_Account.transaction += 1
            return True
        else:
            return False


class Bank_Account_Tasks:
    accounts_list = []
    file_name = 'data.txt'

    def read_data(self):
        f = open('data.txt', 'r')
        for a in f.readlines():
            i = a.replace('\n', '').split(',')
            Bank_Account(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            Bank_Account_Tasks.accounts_list.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        f.close()

    def write_data(self):
        f = open(Bank_Account_Tasks.file_name, 'w')
        for i in Bank_Account_Tasks.accounts_list:
            f.writelines('%s,%s,%s,%s,%s,%s,%.1f,%s,%s\n' % (i[0], i[1], i[2], i[3], i[4], i[5], float(i[6]), i[7], i[8]))

    def check_account(self, string_account_id):
        for a in Bank_Account_Tasks.accounts_list:
            if str(string_account_id) == a[5]:
                return 1

    def put_money_in(self, string_account_id, amount):
        x = 0
        for a in Bank_Account_Tasks.accounts_list:
            x += 1
            if Bank_Account_Tasks().check_account(string_account_id) == 1:
                if Bank_Account(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]).money_in(amount):
                    del(Bank_Account_Tasks.accounts_list[x-1])
                    a[6] = float(a[6])+amount
                    a[8] = int(a[8])+1
                    y = [a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]]
                    Bank_Account_Tasks.accounts_list.insert(x-1, y)
                    Bank_Account_Tasks().write_data()
                    return 'Success'
                else:
                    return 'Failed'

    def get_money_out(self, string_account_id, amount):
        x = 0
        for a in Bank_Account_Tasks.accounts_list:
            x += 1
            if Bank_Account_Tasks().check_account(string_account_id) == 1:
                if Bank_Account(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]).money_out(amount):
                    if Bank_Account(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]).money_in(amount):
                        del (Bank_Account_Tasks.accounts_list[x - 1])
                        a[6] = float(a[6]) - amount
                        a[8] += 1
                        y = [a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]]
                        Bank_Account_Tasks.accounts_list.insert(x - 1, y)
                        Bank_Account_Tasks().write_data()
                    return 'Success'
                else:
                    return 'Failed'

    def show_biggest_account(self):
        amount = 0
        for a in Bank_Account_Tasks.accounts_list:
            if float(a[6]) >= float(amount):
                amount = a[6]
        for b in Bank_Account_Tasks.accounts_list:
            if amount == b[6]:
                return Bank_Account(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7]).show_details()

    def most_transactions(self):
        n = 0
        for a in Bank_Account_Tasks.accounts_list:
            for b in Bank_Account_Tasks.accounts_list:
                if int(b[8]) > n:
                    n = int(b[8])
            if n == int(a[8]) and n > 0:
                return Bank_Account(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]).show_details()
            else:
                return 'don\'t have transaction'

    def get_number_of_transactions(self):
        x = Bank_Account.transaction
        return x

    def show_account(self, string_account_id):
        for a in Bank_Account_Tasks.accounts_list:
            if str(string_account_id) == a[5]:
                return Bank_Account(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]).show_details()

    def delete_account(self, string_account_id):
        x = 0
        for a in Bank_Account_Tasks.accounts_list:
            x += 1
            if str(string_account_id) == a[5]:
                del(Bank_Account_Tasks.accounts_list[x-1])
                Bank_Account_Tasks().write_data()

    def all_account(self):
        z = ''
        for a in Bank_Account_Tasks.accounts_list:
            x = Bank_Account(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]).show_details()
            y = '---------\n'
            z += x + y
        return z

    def clear(self):
        f = open(Bank_Account_Tasks.file_name, 'w')
        f.seek(0)                                  # 移动文件指针到文件的开头
        f.truncate()                               # 清空data.txt内容
        for i in Bank_Account_Tasks.accounts_list:
            f.writelines('%s,%s,%s,%s,%s,%s,%.1f,%s,%d\n' % (i[0], i[1], i[2], i[3], i[4], i[5], float(i[6]), i[7], 0))
