# 2nd SI week in Python
# Variables and scope, exercise 2
# Limbek Zsófi, 18.06.2018

valid_ans = False

while not valid_ans:
    try:
        Fh = float(input("Enter temperature in Fahrenheit: "))
    except ValueError:
        print("Invalid input")
    else:
        valid_ans = True

Cel = 5/9 * (Fh - 32)

print("Temperature in Celsius: {:.1f}".format(Cel))