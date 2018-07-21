
import reports

read_file = input("Please enter the name of the data file: ")
year = int(input("Is there a game from year: "))
genre = input("Please enter a game genre: ")
title = input("Enter a title to see it's line number: ")


count = reports.count_games(read_file)
decide = reports.decide(read_file, year)
latest = reports.get_latest(read_file)
count_by_genre = reports.count_by_genre(read_file, genre)
line_number_by_title = reports.get_line_number_by_title(read_file, title)

with open("output.txt", "w") as ex:
    ex.write(str(count) + "\n")
    ex.write(str(decide) + "\n")
    ex.write(str(latest) + "\n")
    ex.write(str(count_by_genre) + "\n")
    ex.write(str(line_number_by_title) + "\n")