
# Printing functions
from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title, when_was_top_sold_fps

file_name = input("Enter a filename: ")

print("1. How many games are in the file?\n"
"2. Is there a game from a given year?\n"
"3. Which was the latest game?\n"
"4. How many games do we have by genre?\n"
"5. What is the line number of the given game (by title)?\n")

# 1.

print(count_games(file_name))

"""def print_count_games():
    print(count_games(file_name))


print_count_games()"""


# 2.
year = int(input("Is there a game from year: "))
print(decide(file_name, year))

"""def print_decide():
    print(decide(file_name, year))


print_decide()"""


# 3.
print(get_latest(file_name))

"""def print_get_latest():
    print(get_latest(file_name))


print_get_latest()"""


# 4.
genre = input("How many games are there by this genre: ")
print(count_by_genre(file_name, genre))

"""def print_count_by_genre():
    print(count_by_genre(file_name, genre))


print_count_by_genre()"""


# 5.
title = input("What is the line number of the given game (title): ")
print(get_line_number_by_title(file_name, title))

"""def print_get_line_number_by_title():
    print(get_line_number_by_title(file_name, title))


print_get_line_number_by_title()"""


# B3.
print(when_was_top_sold_fps(file_name))

"""def print_when_was_top_sold_fps():
    print(when_was_top_sold_fps(file_name))


print_when_was_top_sold_fps()"""
