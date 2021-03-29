from user_data import *
import sys
from time import *

data = bank_acc


def goback():
    print("\n")
    print(" " * 15 + "1 : for go back to previous menu")
    print(" " * 15 + "2 : for exit")
    i = int(input("enter the option:"))
    if i == 1:
        transfer()

    elif i == 2:
        sys.exit()
    else:
        print("option not found enter the option")
        goback()


def transfer():
    print("\n")
    print(" " * 20 + "1 is bank details ")
    print(" " * 20 + "2 is transition_history ")
    print(" " * 20 + "3 is payee ")
    j = int(input("enter the details:"))
    if j == 1:
        bank_details()
    elif j == 2:
        trans_history()
    elif j == 3:
        transistion()
    else:
        transfer()

#  bank details function i will print bank details and it will call goback function


def bank_details():
    global data
    for keys, values in data.items():
        print(f"{keys}  : {values}")
    goback()


# if user select the payee option then this function will execuited this function


def transistion():
    global data
    print("\n")
    name = input("enter the name  of user :")
    acc_no = int(input("enter the account number:"))
    while True:
        if acc_no == data['acc_num']:
            break
        else:
            acc_no = int(input("enter the account number:"))
    pay_name = input("enter the name:")
    pay_acc = int(input("enter the payee account number:"))
    amount = float(input("enter the amount to be transfer :"))
    if amount > data['balance']:
        print("insufficient fund :")
        print("account balance amount :", data['balance'])
        transistion()
    else:
        print(f"amount {amount} is transfer to {pay_name} with account  number {pay_acc}")
        trn = "Transfer  Date:{0}   amount:{1}".format(str(datetime.datetime.today()), str(amount))
        data['history'].append(trn)
        data['balance'] = data['balance'] - amount
        goback()


# this function will executed thr function when the trans history function


def trans_history():
    global data

    for i in data['history']:
        print(i)
    print("Balance Amount :", data['balance'])
    goback()


print("*" * 40)
print("\n")
print("Welcome To the  Bank Of India ")
print("\n")
print("*" * 40)
sleep(1)
print(" " * 10 + "Enter 1 for new user: ")
print(" " * 10 + "Enter 2 for exciting user:")
i = int(input("Enter the Option :"))

if i == 1:
    print("Bank details form \n")
    data = enter_data()
    print("\n")
    print("Your account number is :", data['acc_num'])
    print("\n")
    transfer()
else:
    print("*" * 40)
    print("\n")
    print("*" * 10 + "  Enter The Login Details  " + "*" * 10)
    user_name = input("Enter the user name : ")
    password = input("Enter the password :")
    while True:

        if user_name in data['u_name'] and password in data['u_pass']:
            transfer()
            break
        else:
            pass

# goback()
