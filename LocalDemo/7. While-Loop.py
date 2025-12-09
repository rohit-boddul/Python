from loguru import logger
import time

labours = ["Mithilesh", "Ayush", "Geeta", "Deepak"]

# itr = 0
# while (itr < len(labours)):
#     # logger.info(f"labour name is {labours[itr]}")
#     # giving sleep time, once 3 seconds are done, next will be printed.value must be in SECONDS
#     time.sleep(3) 
#     itr = itr + 1


# --------------------------------------- Calculator using WHILE loop -----------------------------------------#

# Calculator using while loop
user_input = float(input("Enter the number: "))
operation = input("Choose the operation (+, -, *, /): ")

result = user_input 

while (operation != "="):
    user_input1 = float(input("Enter the other number: "))

    if operation == "+":
        result = result + user_input1
    elif operation == "-":
        result = result - user_input1
    elif operation == "*":
        result = result * user_input1
    elif operation == "/":
        if user_input1 == 0:
            logger.info(f"Error! - Division won't happen with 0")
            exit()
        else:
            result = result / user_input1
    else:
        logger.info(f"Intermediate = {result}")
    operation = input("Choose the operation (+, -, *, /): or Enter '=' to view the result: ")

logger.info(f"Final Results = {result}")



print("1.Addition\n2.subtraction\n 3.Multiplication\n 4.Division")
while(True):
    p=int(input("Please entered your choice :"))
    if(p==1):
        x=int(input("Enter the first number"))
        y=int(input("Enter the second Number"))
        z=(x+y)
        print(z)

    if(p==2):
        x=int(input("Enter the first number"))
        y=int(input("Enter the second Number"))
        z=(x-y)
        print(z)

    if(p==3):
        x=int(input("Enter the first number"))
        y=int(input("Enter the second Number"))
        z=(x*y)
        print(z)

    if(p==4):
        x=int(input("Enter the first number"))
        y=int(input("Enter the second Number"))
        if(y!=0):
          z1=(x/y)
          print(z1)
        else:
            print("Division not possible")
