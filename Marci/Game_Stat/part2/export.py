
import reports

read_file = input("Please enter the name of the data file: ")
title = (input("Please enter the title of the game you want to get the details of: "))


most_played = reports.get_most_played(read_file)
sum_sold = reports.sum_sold(read_file)
avg = reports.get_selling_avg(read_file)
count_longest_title = reports.count_longest_title(read_file)
date_avg = reports.get_date_avg(read_file)
get_game = reports.get_game(read_file, title)

with open("output_part.txt", "w") as ex:
    ex.write(str(most_played) + "\n")
    ex.write(str(sum_sold) + "\n")
    ex.write(str(avg) + "\n")
    ex.write(str(count_longest_title) + "\n")
    ex.write(str(date_avg) + "\n")
    ex.write(str(get_game) + "\n")

#The output file goes in the main "game_statistics_reports" folder (not in the part2 folder)