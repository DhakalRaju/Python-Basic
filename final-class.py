class Bank:
    __bank_name = 'Bro Bank Pvt Ltd'
    __interest_rate = 10

    def __init__(self, f_name, l_name, user_age, balance=0):
        self.first_name = f_name
        self.last_name = l_name
        self.age = user_age
        # self.district = user_district
        self.balance = balance

    def check_current_balance(self):
        print(f'The current balance is {self.balance}')

    def add_balance(self, deposit_balance):
        if deposit_balance > 0:
            self.balance = self.balance + deposit_balance
            print('Your amount has been deposited successfully!')
            self.get_current_balance()
        else:
            print('Enter a valid amount!')
    
    def withdraw_balance(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
    

    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name

    @classmethod
    def get_interest_rate(cls):
        print(f'The current interest rate is {cls.__interest_rate}')

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.__interest_rate = new_rate
        Bank.get_interest_rate()
    
    @classmethod
    def get_bank_name(cls):
        return Bank.__bank_name
    
    @classmethod
    def get_interest_rate(cls):
        # print('The current interest rate is ' + str(cls.interest_rate))
        print(f'The current interest rate is {cls.__interest_rate}')

    @staticmethod
    def get_holiday_list():
        print('Yaay!!! 😁')
        print('Teej ma sab kt haru lai matra bida cha')
        print('Dashain holiday last from Ghatasthapana to Purnima')
        print('Tihar ma Laxmi Puja dekhi Bhai tika ko bholi palta samma bida')

while True :
    print(f'Welcome to {Bank.get_bank_name}')
    user_choice = input('Enter 1 to open bank account. \nEnter 2 to check current balance. \nEnter 3 to add deposit balance. \nEnter 4 to withdraw balance. \nEnter 5 to check current interest rate. \nEnter 6 to change the interest rate. \nEnter 7 to check holiday.: ')

    if user_choice == '1':
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        user_age = int(input('Enter age: '))
        user_account = Bank(first_name.upper(), last_name.upper(), user_age)
        
        print('Congratulations! Account Opened!')
        print('*' * 15)

    elif user_choice == '2':
        user_account.get_current_balance()

    elif user_choice == '3':
        balance = int(input('Enter deposit amount: '))
        user_account.add_balance(balance)

    elif user_choice == '4':
        amount = int(input('Enter withdraw amount: '))
        user_account.withdraw_balance(amount)

    elif user_choice == '5':
        Bank.get_interest_rate()

    elif user_choice == '6':
        print('WARNING')
        print('Only change the interest rate with the permission of the manager and the decision from the Bro Advisory Board!')
        new_rate = int(input('Enter the new interest rate:'))
        Bank.set_interest_rate(new_rate)

    elif user_choice == '7':
        Bank.get_holiday_list()

    else:
        Bank.get_holiday_list()