"""This script simulates the deposit & withdraw of saving account.
    Simple deposit & withdraw are made by deposit() & withdraw(),
    if withdrawing amount < balance in account, credit level will -1 and can only withdraw the current saving in account.
    This value will accumulate, and the account will be suspended as soon as it hits -5.

    Args:
        Account info is created by = Account('123–456–789', 'Justin', 'HKD')

    Return(Expected Output):
        Depositing...
        balance: HKD 1110

        Exceeding the balance of your account. All the saving are withdrew from the account.
        Withdrawing = HKD 1110
        credit level = -1.

        Depositing...
        balance: HKD 1110

        Exceeding the balance of your account. All the saving are withdrew from the account.
        Withdrawing = HKD 1110
        credit level = -2.

        Fail to withdrew from HKD account.

        Depositing...
        balance: HKD 10

        Exceeding the balance of your account. All the saving are withdrew from the account.
        Withdrawing = HKD 10
        credit level = -3.

        Fail to withdrew from HKD account.

        Depositing...
        balance: HKD 10

        Exceeding the balance of your account. All the saving are withdrew from the account.
        Withdrawing = HKD 10
        credit level = -4.

        Depositing...
        balance: HKD 10

        Exceeding the balance of your account. All the saving are withdrew from the account.
        Withdrawing = HKD 10
        credit level = -5.

        Credit level hits the minimum.
        HKD saving account of 'Justin' is suspended.

"""
class Account:

    def __init__(self, number, name, currency):
        self.currency  = 'HKD'
        self.number = number
        self.name = name
        self.balance = 0
        self.creditlevel = 0

    # Adding the saving to account
    def deposit(self, amount):

    # Withdrawing the corresponding value, or
    # Deducting the credit level if the withdraw > balance & withdraw the current saving in account
    def withdraw(self, amount):


acct1 = Account('123–456–789', 'Justin', 'HKD')
acct1.deposit(1110)
acct1.withdraw(1115)

acct1.deposit(1110)
acct1.withdraw(1115)
acct1.withdraw(10)

acct1.deposit(10)
acct1.withdraw(20)
acct1.withdraw(20)

acct1.deposit(10)
acct1.withdraw(20)

acct1.deposit(10)
acct1.withdraw(20)