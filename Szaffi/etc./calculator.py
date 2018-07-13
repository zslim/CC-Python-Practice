#Write a calculator script, that waits for the user to enter a number,
# then a sign (plus, minus, multiplication and division), then a number again.
#After the 2nd number input, the script should calculate the addition or subtraction and print it out.
#Then the program should run again with asking for the first number.

#The script should exit when the user enters a letter instead of a number.
print("Calculator program")

while 1:
    print("First choose an operation: +; -; *; / or q to exit")
    op = str(input("Please enter the operation: "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == "q":
        break

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "/":
        result = num1 / num2

    elif op == "*":
        result = num1 * num2

    else:
        print("Bad choice!")
    print(result)
   
    pass