import reports

input_file = "game_stat.txt"

with open("export.txt", 'w') as f:
    f.write(str(reports.count_games(input_file)) + '\n')
    year = input("year: ")
    f.write(str(reports.decide(input_file, year)) + '\n')
    f.write(str(reports.get_latest(input_file)) + '\n')
    genre = input("genre: ")
    f.write(str(reports.count_by_genre(input_file, genre)) + '\n')
    title = input("title: ")
    f.write(str(reports.get_line_number_by_title(input_file, title)) + '\n')
