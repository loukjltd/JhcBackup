class Person:
    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day

    def show_details(self):
        account_details = self.first_name + "," + self.last_name + "," + self.birth_year + "," + self.birth_month + "," + self.birth_day
        return account_details


class BankAccount(Person):
    transactions = 0

    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day, account_id, money, account_type):
        Person.__init__(self, first_name, last_name, birth_year, birth_month, birth_day)
        self.account_id = account_id
        self.money = money
        self.account_type = account_type

    def show_details(self):
        if self.account_type == 0:
            self.account_type = "Regular"
        elif self.account_type == 1:
            self.account_type = "Premium"
        elif self.account_type == 2:
            self.account_type = "Gold"
        account_details = self.first_name + "," + self.last_name + "," + self.birth_year + "," + self.birth_month + "," + self.birth_day + ',' + self.account_id + "," + self.money + "," + self.account_type
        return account_details

    def money_in(self, money):
        self.money += money
        return True

    def money_out(self, money):
        self.money -= money
        if self.money >= 0:
            return True
        else:
            return False


class BankAccountTasks:
    accounts_list = []
    file_name = "files"

    def read_data(self):
        f = open("files.txt", "r")
        for line in f.readlines():
            split_line = line.split(",")
            object_first_name = split_line[0]
            object_last_name = split_line[1]
            object_birth_year = split_line[2]
            object_birth_month = split_line[3]
            object_birth_day = split_line[4]
            object_account_id = split_line[5]
            object_money = split_line[6]
            object_account_type = split_line[7]
            new_object = BankAccount(object_first_name, object_last_name, object_birth_year, object_birth_month, object_birth_day, object_account_id, object_money, object_account_type)
            self.accounts_list.append(new_object)
        f.close()

    def write_data(self):
        f = open("files.txt", "w")
        for line in self.accounts_list:
            statement = line.first_name + "," + line.last_name + "," + line.birth_year + "," + line.birth_month + "," + line.birth_day + "," + line.account_id + "," + line.money + "," + line.account_type
            f.write(statement)
        f.close()

    def check_account(self, string_account_id):
        for line in self.accounts_list:
            if string_account_id == line.account_id:
                return 1

    def put_money_in(self, string_account_id, amount):
        for line in self.accounts_list:
            if string_account_id == line.account_id:
                if line.money_in(amount):
                    line.transactions += 1
                    return "Success"
                else:
                    return "Failed"

    def show_biggest_account(self):
        max_account = self.accounts_list[0]
        for line in self.accounts_list:
            if max_account.money < line.money:
                max_account = line
        return max_account.show_details()

    def most_transactions(self):
        max_account = self.accounts_list[0]
        for line in self.accounts_list:
            if max_account.transactions < line.transactions:
                max_account = line
        return max_account.show_details()

    def add_transactions(self, a_list):
        if len(a_list) == 0:
            return 0  # stop
        else:
            new_list = a_list[1:len(a_list)]
            return a_list[0].transactions + self.add_transactions(new_list)

    def get_number_of_transactions(self):
        self.add_transactions(self.accounts_list)

    def show_account(self, string_account_id):
        for line in self.accounts_list:
            if string_account_id == line.account_id:
                return line

    def delete_account(self, string_account_id):
        for line1 in self.accounts_list:
            if string_account_id == line1.account_id:
                self.accounts_list.remove(line1)
