

from reports import count_games, decide, get_latest, count_by_genre,  get_line_number_by_title


def print_latest(file_name):
    print("The latest game in the statistics: ")
    print(get_latest(file_name))


def menu():
    menu_return = True
    while menu_return == True:
        print("""
        1.: How many games are in the file?
        2.: Is there a game from a given year?
        3.: Which was the latest game?
        4.: How many games do we have by genre?
        5.: What is the line number of the given game (by title)?

        0.: Exit program 
        """)
        file_name = input("Please enter the file name: ")
        question = int(input("Please enter the number of the choosen question from these: "))
        if question == 1:
            print("The answer for the 1. question is: ")
            print(count_games(file_name))
            
        elif question == 2:
            year = int(input("\nIs there a game from year: "))
            print("The answer for the 2. question is: ")
            print(decide(file_name, year))
        elif question == 3:
            print("The answer for the 3. question is: ")
            print_latest(file_name)
        elif question == 4:
            genre = input("Please enter a game genre: ")
            print("The answer for the 4. question is: ")
            print(count_by_genre(file_name, genre))
        elif question == 5:
            
            title = input("Enter a title to see it's line number: ")
            print("The answer for the 5. question is: ")
            print(get_line_number_by_title(file_name, title))
        elif question == 0:
            menu_return = False
            print("You are exiting the program")


def main():
    menu()



if __name__ == '__main__':
    main()