# for sauna users, it’s 1500 HUF altogether
# for the ones who don’t intend to use the sauna, the following applies: (unless they are students):
# women: 500 HUF
# men: 750 HUF
# for students it’s 300 HUF (unless they use the sauna)
# below the age of 14, usage of the gym is forbidden

# Jim Carrey should ask yes/no questions.
# All Jim's questions should be elements of list - script should display them based on stage.
# After asking enough questions he should tell you the price.
# Jim should be foolproof (able to handle stupid users).

# If your script works, you can add some features:
# Jim should tell some random jokes after each answer.
# Use ASCII art for tickets and add both questions and answers should be colorful.

questions = [
    ["Are you younger than 14 yrs old? ", "Not allowed."],
    ["Do you want to use the sauna? ", "1500 HUF"],
    ["Are you a student? ", "300 HUF"],
    ["Are you a female? ", "500 HUF"]
]


def gymCarrey():
    for question in questions:
        answer = input(question[0])
        if answer == "yes":
            print(question[1])
            break
    print("750 HUF")


gymCarrey()




"""def gymCarrey():
    student = input("Are you a student? ")
    if student == "yes":
        younger14 = input("Are you younger than 14 yrs old? ")
        if younger14 == "yes":
            print("\nThe usage of the gym for you is forbidden. ")
        elif younger14 == "no":
            print("\nIt'll be 300 HUF pls. ")
    elif student == "no":
        sauna = input("Do you want to use the sauna? ")
        if sauna == "yes":
            print("\nIt'll be 1500 HUF pls. ")
        elif sauna == "no":
            gender = input("Are you a female? ")
            if gender == "yes":
                print("\nIt'll be 500 HUF pls. ")
            elif gender == "no":
                print("\nIt'll be 750 HUF pls. ")


gymCarrey()"""
