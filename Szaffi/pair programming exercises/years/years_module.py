import datetime


def years(age):
    return 2018-age+100


def main():
    name = input("Please enter your name: ")
    print("Hello "+ name + "!")
    age = int(input("Please enter your age: "))
    num = int(input("How many times do you want to see the result? "))
    print("You will turn 100 in {}\n".format(years(age)) * num)
    return


if __name__ == '__main__':
    main()
