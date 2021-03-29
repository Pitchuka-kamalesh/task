import datetime
bank_acc = {}


def gen_acc():
    i = 1
    while True:
        yield i
        i += 1


def user_data(**kwargs):
    global bank_acc
    bank_acc = kwargs

    return bank_acc


def enter_data():
    accont = gen_acc()

    acc_num = next(accont)

    name = input("enter the full name : ")

    phone = int(input("enter the phone number : "))

    addr = input("enter the address: ")

    pan = input("enter the pan number")

    card = input("enter the debit or credit card:")

    u_name = input("enter the user name we have: ")

    u_pass = input("enter the password:")

    aadhaar = int(input("enter the 12 digit  addhar number:"))

    balance = float(input("Enter the min balance 5000"))

    acc_date = datetime.datetime.today()

    while True:
        if len(str(aadhaar)) != 12:
            aadhaar = int(input("enter the 12 digit addhar number:"))
        if not(pan[0:5].isalpha() and pan[5:-1].isnumeric() and pan[-1].isalpha()):
            pan = input("enter the  correct pan number:")
        if balance < 5000.00:
            balance = float(input("enter the minimum balance"))
        if True:
            pass
        else:
            break
    hist = "deposit  " + str(acc_date) + "  amount: " + str(balance)
    history = [hist]
    accounts = user_data(acc_num = acc_num,name = name,phone = phone,addr = addr,pan=pan,card = card,u_name = u_name,u_pass=u_pass,aadhaar = aadhaar,balance = balance,history=history)
    return accounts
# amount deposity  varible  only integer


#
#bank data must store in dictnoary

# then check the username and password in data

# if present then trasistion details

