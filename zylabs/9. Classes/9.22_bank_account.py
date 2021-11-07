# FIXME UNFINISHED
class BankAccount:
    def __init__(self, name, savings, checking):
        self.name = name
        self.savings = savings
        self.checking = checking

    def deposit_checking(self, more):
        if more > 0:
            self.checking = self.checking + more

    def deposit_savings(self, more):
        if more > 0:
            self.savings = self.savings + more

    def withdraw_checking(self, less):
        if less > 0:
            self.checking = self.checking - less

    def withdraw_savings(self, less):
        if less > 0:
            self.savings = self.savings - less

    def transfer_to_savings(self, change):
        if change > 0:
            self.checking = self.checking - change
            self.savings = self.savings + change


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