print("Welcom to our ATM")
print("Please insert your card")
input("Press Enter to continue:")
def login_ATM():
    userpin_inbank=1234
    count=0
    while count<3:
        userpin=int(input("Enter your pin Number:\n"))
        if userpin==userpin_inbank:
            return True
        else:
            print("Tncorrect password\n Try again")
            count+=1
    print("Your Account has been blocked")
    return False
login_output=login_ATM()    



    
