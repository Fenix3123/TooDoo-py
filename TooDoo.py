from User import User
from sqlmethods import *

while True:
    print("Welcome to TooDoo-py")
    print("What would you like to do:")
    print("1. Create account")
    print("2. Login")
    print("3. exit")
    choice = input("Enter a number: ")
    if choice == "3":
        exit()
    elif choice == "1":
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        Account = User(username, password)
        InsertUser(Account)
    elif choice == "2":
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        Account = User(username, password)
        if CheckUser(Account)== True:
            while True:
                print("Welcome {}".format(Account.username))
                print("Your TooDoo list is:")
                print()
                print("------------------------------------")
                #gets the user object to get id to retrieve toodoo items
                tuple = GetUser(Account)
                gettoodoo(tuple)
                #end of prints
                print("------------------------------------")
                print()
                print("What would you like to do now?")
                print("1. add toodoo list item")
                print("2. logout")
                choice = input("Enter your choice: ")
                if choice == "1":
                    item = input("The Description of the activity: ")
                    Inserttoodoo(item,tuple)
                elif choice == "2":
                    exit()
        else:
            print("Doesnt exist")
    