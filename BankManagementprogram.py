class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, user_id, initial_deposit):
        account = Account(user_id, initial_deposit)
        self.accounts.append(account)
        self.total_balance += initial_deposit
        return account

    def get_account_by_id(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled


class Account:
    def __init__(self, user_id, initial_deposit):
        self.account_id = generate_unique_account_id()
        self.user_id = user_id
        self.balance = initial_deposit
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(Transaction(self.account_id, self.account_id, amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(Transaction(self.account_id, self.account_id, -amount))
        else:
            print("Insufficient balance in the account.")

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(Transaction(self.account_id, recipient_account.account_id, -amount))
            recipient_account.transaction_history.append(Transaction(self.account_id, recipient_account.account_id, amount))
        else:
            print("Insufficient balance in the account.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history


class Transaction:
    def __init__(self, sender_account_id, recipient_account_id, amount):
        self.sender_account_id = sender_account_id
        self.recipient_account_id = recipient_account_id
        self.amount = amount
        self.timestamp = get_current_timestamp()


def generate_unique_account_id():
    pass


def get_current_timestamp():
    pass


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, user_id, initial_deposit):
        return self.bank.create_account(user_id, initial_deposit)

    def get_total_balance(self):
        return self.bank.get_total_balance()

    def get_total_loan_amount(self):
        return self.bank.get_total_loan_amount()

    def toggle_loan_feature(self):
        self.bank.toggle_loan_feature()
        if self.bank.loan_feature_enabled:
            print("Loan feature is now enabled.")
        else:
            print("Loan feature is now disabled.")


bank = Bank()
admin = Admin(bank)

user1 = admin.create_account("user1", 1000)
user2 = admin.create_account("user2", 500)

user1.deposit(500)
user1.withdraw(200)

user1.transfer(300, user2)

print(user1.get_balance())
print(user1.get_transaction_history())

print(admin.get_total_balance())
print(admin.get_total_loan_amount())

admin.toggle_loan_feature()
