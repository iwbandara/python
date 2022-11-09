#Author: Indika W Bandara
#Date:  2022-11-09
#Version: 1.0

# In this script age of the user is accepted as the input and checks for the input
# to make sure the value entered is Numeric or not. If age value is numeric, then checks
# whether the value is greater than 18 or not

age=input("Please enter your age : ")

if age.isnumeric():
    if (int(age) >= 18):
        print("You can Vote in the next election.")
    else:
        print("You can not vote in the next election.")
else:
    print("Next time please enter a correct value.")
