# 3th SI week, starting with Python
# Set A assignment 2.

from colorama import Fore, Style

def pres(res):
    print("Result: " + Style.BRIGHT + Fore.BLUE + str(res), "\n" + Style.RESET_ALL)

while True:
    n1 = input("Enter a number (or a letter to " + Style.BRIGHT + "exit" + Style.RESET_ALL + "): ")
    try:
        n1 = float(n1)
    except:
        exit()

    op = input("Enter an operation: ")

    n2 = input("Enter another number: ")
    try:
        n2 = float(n2)
    except:
        print(Fore.RED + "This is not a number \n" + Style.RESET_ALL)
        continue

    if op == "+":
        pres(n1 + n2)
    elif op == "-":
        pres(n1 - n2)
    elif op == "*":
        pres(n1 * n2)
    elif op == "/":
        pres(n1 / n2)
    else:
        print(Fore.RED + "Unknown operation", "\n" + Style.RESET_ALL)

