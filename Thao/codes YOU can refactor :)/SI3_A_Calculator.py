# Write a calculator script, that waits for the user to enter a number, then a sign (plus, minus, multiplication and division), then a number again.
# After the 2nd number input, the script should calculate the addition or subtraction and print it out.

# Then the program should run again with asking for the first number.

# The script should exit when the user enters a letter instead of a number.

while 1:  # the loop goes on and on and on, forever
    x = int(input('Enter a number: '))
    sign = input('Enter an operation: ')
    y = int(input('Enter another number: '))

    if sign == '+':
        result = x + y
        print(result)
    elif sign == '-':
        result = x - y
        print(result)
    elif sign == '*':
        result = x * y
        print(result)
    elif sign == '/':
        result = x / y
        print(result)
    else:
        pass


#  result = 
#  print(result)