def displayMenu():
    print("MENU".center(20,'*'))
    print("1.Withdraw")
    print("2.Deposite")
    print("3.Check Balance")
    print("4.Change Pin")
    print("5.Exit")
    
# Withdraw
def withdraw():
    global pin1, balance
    while True:
        print()
        user_pin= input("enter the pin :")
        if user_pin== pin1:
            while True:
                amount= int(input("Enter Amount to withdraw"))
                if amount > balance:
                    print("Insufficient Balance !Balance:",balance)
                else:
                    balance-=amount
                    print("Withdraw Sucessfull ! Balance:",balance)
                    break
            break
        else:
            print("Invalid Pin !")   
            
# Deposite
def deposite():
    global balance
    while True:
        user_pin= input("enter the pin :")
        if user_pin== pin1:
            amount= int(input("Enter Amount to Deposite"))
            balance+=amount
            print("Deposite Sucessfull ! Balance :",balance)
            break
        else:
            print("Invalid Pin !")
            
# Check Balance
def checkbalance():
    while True:
        user_pin= input("enter the pin :")
        if user_pin== pin1:
            print("Name :",name)
            print("Balance :",balance)
            break           
        else:
            print("Invalid Pin !")
            
# Pin Change
def changepin():
    global pin1, balance
    while True:
        user_pin= input("enter the pin :")
        if user_pin== pin1:
            while True:
                pin1=input("Enter New Pin :")
                pin2=input("Confirm Pin :")
                if pin1==pin2:
                    print("Pin Updated Sucessfull")
                    break
                else:
                    print("Password not Matching")
            break
        else:
            print("Invalid Pin")
            
# Main function to call other functions
def main():
    while True:
        displayMenu()
        ch=int(input("Enter Choice :"))
        if ch == 1:
            withdraw()
        elif ch == 2:
            deposite()
        elif ch == 3:
            checkbalance()
        elif ch == 4:
            changepin()
        elif ch == 5:
            break
        else:
            print("Wrong Input")
    print("Thank You !")
    
# Main Code
# Taking inputs
name=input("Enter Name :")
balance=int(input("Set the Balance :"))
while True:
    pin1=input("Enter Pin :")
    pin2=input("Confirm Pin :")
    if pin1==pin2:
        print("Pin Set Sucessfull")
        break
    else:
        print("Password Not Matching")
            
# Calling the main function
main()
    