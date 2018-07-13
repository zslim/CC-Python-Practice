import reports

file_name = "game_stat.txt"

print(reports.count_games(file_name))
year = input("year: ")
print(reports.decide(file_name, year))
print(reports.get_latest(file_name))
genre = input("genre: ")
print(reports.count_by_genre(file_name, genre))
title = input("title: ")
print(reports.get_line_number_by_title(file_name, title))
