# Author: Indika W Bandara
# Date: 2022-11-09
# Version: 1.0

# Use of inbuilt functions

# Use of len() function => calculate the length of the string

str1="Welcome to Sri Lanka." # declaring the string
length=len(str1)
print("The length of the string is : "+str(length))

# ===============================================================

# Use of split() function => splits a list into small sections

str2="Sri Lanka is an island in Indian ocean."

print(str2.split(' '))

# ===============================================================

# Checking input is only CAPITAL letters

name=input("Enter your name : ")

if name.isupper():
    print("Your name is in CAPITAL letters. Thank you.")
else:
    print("Your name is not in CAPITAL letters. Try again next time.")

# ===============================================================

# Checking input is only SIMPLE letters

name=input("Enter your name : ")

if name.islower():
    print("Your name is in SIMPLE letters. Thank you.")
else:
    print("Your name is not in SIMPLE letters. Try again next time.")
