from withdraw import balance_check, withdraw_cash, fast_cash, ministatement
from login import login_output


if login_output == True:

    def show_menu():
        choice = 0

        while choice != 5:
            print("1. Check Balance")
            print("2. Withdraw Cash")
            print("3. Fast Cash")
            print("4. Mini Statement")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                balance_check()

            elif choice == 2:
                withdraw_cash()

            elif choice == 3:
                fast_cash()

            elif choice == 4:
                ministatement()

            elif choice == 5:
                print("Thank you for using ATM")

            else:
                print("Invalid Option")

    show_menu()
    
