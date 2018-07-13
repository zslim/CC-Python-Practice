
# Printing functions
from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game, count_grouped_by_genre

# 1.
file_name = input("Enter a filename: ")
print(get_most_played(file_name))

"""def print_get_most_played():
    print(get_most_played(file_name))


print_get_most_played()"""


# 2.
print(sum_sold(file_name))

"""def print_sum_sold():
    print(sum_sold(file_name))


print_sum_sold()"""


# 3.
print(get_selling_avg(file_name))

"""def print_get_selling_avg():
    print(get_selling_avg(file_name))


print_get_selling_avg()"""


# 4.
print(count_longest_title(file_name))

"""def print_count_longest_title():
    print(count_longest_title(file_name))


print_count_longest_title()"""


# 5.
print(get_date_avg(file_name))

"""def print_get_date_avg():
    print(get_date_avg(file_name))


print_get_date_avg()"""

# 6.
title = input("What properties does this game have? (title) ")
print(get_game(file_name, title))

"""def print_get_game():
    print(get_game(file_name, title))


print_get_game()"""

# B1.
#genre = input("How many games are there grouped by genre? ")
print(count_grouped_by_genre(file_name))
