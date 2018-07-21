from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title,  get_date_avg, get_game




def menu():
    menu_return = True
    while menu_return == True:
        print("""
1.: What is the title of the most played game (i.e. sold the most copies)?
2.: How many copies have been sold total?
3.: What is the average selling?
4.: How many characters long is the longest title?
5.: What is the average of the release dates?
6.: What properties has a game?
""")
        question = int(input("Please enter the number of the choosen question from these: "))
        file_name = input("Please enter the file name: ")
        if question == 1:
            print("The most played game is: ")
            print(get_most_played(file_name))
            #export(get_most_played(file_name))
        elif question == 2:
            print("The total number of sold copies is: ")
            print(float(sum_sold(file_name)))
            #export(float(sum_sold(file_name)))
        elif question == 3:
            print("The average selling number is: ")
            print(get_selling_avg(file_name))
        elif question == 4:
            print("The number of characters in the longest title is: ")
            print(count_longest_title(file_name))
        elif question == 5:
            print("The average of the release dates is: ")
            print(get_date_avg(file_name))
        elif question == 6:
            title = input("Please enter the title of the game: ")
            print("The details of " + title + " are the following: ")
            print(*get_game(file_name, title))
        elif question == 0:
            menu_return = False
            print("You are exiting the program")


def main():
    menu()




if __name__ == '__main__':
    main()