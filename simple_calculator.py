print("Welcome to Simple Calculator.")
print("1. Addition")
print("2. Subtraction")        
print("3. Multiplication")
print("4. Division")
print("5. Exit")

print("Select the Calculation type : ")
txtInput=int(input())

def acceptValues():
    global num1
    num1=int(input("Enter the First number : "))
    global num2
    num2=int(input("Enter the Second number : "))
    return num1, num2

#print(txtInput)

if(txtInput==1):
    print("======ADDITION======")
    #num1=int(input("Enter the First number : "))
    #num2=int(input("Enter the Second number : "))
    acceptValues()
    result=num1+num2
    print("--+--+--+--+--+--+--+--+--+--+--+--+")
    print("The ADDITION of "+str(num1)+" and "+str(num2)+" is : "+str(result))
    print("--+--+--+--+--+--+--+--+--+--+--+--+")
elif(txtInput==2):
    print("======SUBTRACTION======")
    #num1=int(input("Enter the First number : "))
    #num2=int(input("Enter the Second number : "))
    acceptValues()
    result=num1-num2
    print("--+--+--+--+--+--+--+--+--+--+--+--+")
    print("The SUBTRACTION of "+str(num1)+" and "+str(num2)+" is : "+str(result))
    print("--+--+--+--+--+--+--+--+--+--+--+--+")
else:
    print("Wrong choice.")
