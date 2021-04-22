import datetime
import random
import validation
import database
from getpass import getpass

now = datetime.datetime.now()

def init():
    print("Welcome!")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)
        else:
            print('Invalid account or password')
            login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")
    balance = 0

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password, balance)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")


        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]) + 'you logged in:' + ' ' +now.strftime('%Y-%m-%d %H:%M:%S'))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation():
    current_balance = get_current_balance(0)
    print("Your Current Balance is #%s" % current_balance)
    withdrawal = int(input('How much would you like to withdraw? \n'))
    if withdrawal <= current_balance:
        print('Take your cash')
        new_balance = current_balance - withdrawal
        return "Your Current Balance is #%s" % new_balance
    else:
        print('Insuffucient Balance, Try again')
    
    withdrawal_operation()


def deposit_operation():
    current_balance = get_current_balance(0)
    print("Your Current Balance is #%s" % current_balance)
    deposit = int(input('How much would you like to deposit? \n'))
    new_balance = current_balance + deposit
    print('Your Current Balance is #%s' % new_balance)


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(new_balance):
    return new_balance

    


def get_current_balance(balance):
    return balance


def logout():
    login()


init()