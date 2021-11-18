class BankAccount:
    def __init__(self, name, checking, savings):
        self.name = name
        self.savings_balance = savings
        self.checking_balance = checking

    def deposit_checking(self, more):
        if more > 0:
            self.checking_balance = self.checking_balance + more

    def deposit_savings(self, more):
        if more > 0:
            self.savings_balance = self.savings_balance + more

    def withdraw_checking(self, less):
        if less > 0:
            self.checking_balance = self.checking_balance - less

    def withdraw_savings(self, less):
        if less > 0:
            self.savings_balance = self.savings_balance - less

    def transfer_to_savings(self, change):
        if change > 0:
            self.checking_balance = self.checking_balance - change
            self.savings_balance = self.savings_balance + change


if __name__ == "__main__":
    account = BankAccount("Mickey", 500.00, 1000.00)
    account.checking_balance = 500
    account.savings_balance = 500
    account.withdraw_savings(100)
    account.withdraw_checking(100)
    account.transfer_to_savings(300)

    print(account.name)
    print('${:.2f}'.format(account.checking_balance))
    print('${:.2f}'.format(account.savings_balance))
