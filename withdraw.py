usercash_inbank = 50000
transections = []


def balance_check():
    print("Your current balance is", usercash_inbank)


def cash_process(amount):
    global transections
    global usercash_inbank

    if amount <= usercash_inbank:
        usercash_inbank -= amount
        transections.append(f"Withdraw: {amount}")
        return True
    else:
        return False


def withdraw_cash():
    amount = int(input("Enter your amount: "))

    if cash_process(amount):
        if recipt():
            print("Withdraw Successful")
            print("Your Remaining Balance is", usercash_inbank)
        else:
            print("Please Collect Your Cash\nWithdraw Successful")
    else:
        print("Insufficient Balance")


def fast_cash():

    fastcash_options = ["1.10000","2.8000","3.6000","4.4000",
                        "5.2000","6.1000","7.500","8.other"]

    fastcash_amount = [10000,8000,6000,4000,2000,1000,500]

    count = 0
    for item in fastcash_options:
        print(item.ljust(12), end="")
        count += 1
        if count % 3 == 0:
            print()

    fastcash_userinput = int(input("\nEnter your option (1-8): "))

    if 1 <= fastcash_userinput <= 7:
        amount = fastcash_amount[fastcash_userinput - 1]

        if cash_process(amount):
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif fastcash_userinput == 8:
        amount = int(input("Enter your amount: "))

        if cash_process(amount):
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    else:
        print("Invalid Option")


def recipt():
    print("Do You Want Receipt? (yes/no)")
    recipt_option = input("Enter your choice: ")

    if recipt_option.lower() == "yes":
        return True
    else:
        return False


def ministatement():
    if len(transections) == 0:
        print("No Transaction Yet")
    else:
        for item in transections[-5:]:
            print(item)
    

            









       






