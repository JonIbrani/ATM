# The pin is 1234
# User: Jon Ibrani
# Balance: 1500$
# Card Number: 1111

from cardholder import cardholder

def print_menu():
    print("Please choose one of the following options:")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Show Balance")
    print("4.Exit")

def deposit(cardholder):
    try:
        deposit = float(input("How much money would you like to deposit?:\n"))
        cardholder.setbalance(cardholder.get_balance() + deposit)
        print("Thank you for depositing money. Your new balance is:",str(cardholder.get_balance()))
    except:
        print("Invalid input")
def withdraw(cardholder):
    try:
        withdraw = float(input("How much money would you like to withdraw:\n"))
        if(cardholder.get_balance() <withdraw):
            print("Insufficient balance")
        else:
            cardholder.set_balance(cardholder.get_balance() - withdraw)
            print("You are good to go! Thank you")
    except:
        print("Invalid input")

def check_balance(cardholder):
    print("Your current balance is:", cardholder.get_balance())

if __name__ == "__main__":
    current_user = cardholder("","","","","")

    list_of_cardholders = []
    list_of_cardholders.append(cardholder("1111", 1234, "Jon", "Ibrani", 1500))

    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card:")
            debitMatch = [holder for holder in list_of_cardholders if holder.cardNum == debitCardNum]
            if(len(debitMatch)> 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recongnized.Please try again.")
        except:
                print("Card number not recongnized.Please try again.")


    while True:
        try:
            userPin = int(input("Please enter your pin").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN.Please try again.")
        except:
            print("Invalid PIN. Please try again")
    print("Welcome", current_user.get_firstname(), ":)")
    option = 0
    while (option !=4):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")

        if(option ==1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option ==4):
            break
        else:
            option = 0

        print("Thank you have a nice day.")

