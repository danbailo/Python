start = True
account = []
# deposit = []

account_balance = {}

def create_account():
    global account,start,account_balance

    print('Please, input a number of account: ')    
    account_number = str(input())
    # print(len(account_number))

    while len(account_number) != 6 or account_number in account_balance:
        if len(account_number) != 6:
            print('Account must have 6 numbers: ')
        elif account_number in account_balance:
            print('This account has exist in bank, input a different number: ')
        account_number = str(input())
        
    deposit = float(input('Input a value of deposit: '))
    account_balance[account_number] = deposit 
    # account.append(account_number)

def show_accounts():
    global account_balance
    for item in account_balance.items():
        print('Account {}, Balance: {}'.format(item[0],item[1]))
    # global account #, funciona sem
    # for i in enumerate(account):
    #     print(i)

def intro():
    global start
    while start:
        print('Create account or Close the program? "c" for create, "q" for quit')
        option = str(input()).lower()
        if option == 'c':
            create_account()
        elif option == 'q':
            start = False
        else:
            print('Please, input only "c" or "q"!')

intro()
show_accounts()