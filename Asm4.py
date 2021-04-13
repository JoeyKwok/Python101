class Account:
    count = 0
    def __init__(self, number, name, currency):
        self.currency  = 'HKD'
        self.number = number
        self.name = name
        self.balance = 0
        self.creditlevel = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount
        self.count = 0
        print(f'Depositing...'
              f'\nbalance: {self.currency} {acct1.balance}\n')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'balance: {self.currency} {acct1.balance}')
        else:
            if self.count == 1:
                print(f'Fail to withdrew from {self.currency} account.\n')
            else:
                self.creditlevel -= 1
                self.count = 1
                originalsaving = self.balance
                self.balance = 0
                print(f'Exceeding the balance of your account. All the saving are withdrew from the account.'
                      f'\nWithdrawing = {self.currency} {originalsaving}'
                      f'\ncredit level = {self.creditlevel}. \n')
                if self.creditlevel <= -5:
                    print(f'Credit level hits the minimum.\n'
                          f'{self.currency} saving account of \'{self.name}\' is suspended.\n')

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