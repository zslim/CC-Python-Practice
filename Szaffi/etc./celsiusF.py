correct_input = False

while not correct_input:
    try:
        T_f = int(input("Write Fahrenheit number, what you want to convert!:"))

        T_c = (5/9) * (T_f - 32)

        print("Here is your Celsius degree!:", T_c )
    except ValueError:
        print("Please enter a valid input!")
    else:
        correct_input = True

