# Author: Indika W Bandara
# Date: 2022-11-16
# Version: 1.0
# Script to accept a number from user and guess it

print()
print("Welcome to Number Guessing Game.")

givenNo=44

while True:
    print("===========================================")
    print("Please type the number of your preference :")
    #print("===========================================")
    txtInput=int(input())

    if(txtInput==givenNo):
        print("+---+---+---+---+---+---+---+---+---+---+---+---+")
        print("Congratulations !!! Your guess is correct.")
        print("+---+---+---+---+---+---+---+---+---+---+---+---+")
        break
    else:
        print("+---+---+---+---+---+---+---+---+---+---+---+---+")
        print("Sorry. Your guess is incorrect")
        print("+---+---+---+---+---+---+---+---+---+---+---+---+")
        if(txtInput >= givenNo):
            print("Please type a lower number.")
        else:
            print("Please type a higher number.")
