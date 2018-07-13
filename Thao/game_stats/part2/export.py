
# Export functions
from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game

file_name = input("Enter a filename: ")
title = input("What properties does this game have? (title) ")

with open("judy.txt", "w") as file:
    file.writelines(str(get_most_played(file_name)))
    file.writelines("\n" + str(sum_sold(file_name)))
    file.writelines("\n" + str(get_selling_avg(file_name)))
    file.writelines("\n" + str(count_longest_title(file_name)))
    file.writelines("\n" + str(get_date_avg(file_name)))
    file.writelines("\n" + str(get_game(file_name, title)))

file = open("judy.txt", "r")
print(file.read())
file.close()
