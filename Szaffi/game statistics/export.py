from reports import count_games, decide, count_by_genre, get_line_number_by_title, get_latest, get_genres

# How many games are in the file?
with open("export.txt", "w") as file:
    file.writelines(str(count_games("game_stat.txt")))

# Is there a game from a given year?
    year = int(input("Write the year, you want to search:"))
    file.writelines('\n'+str(decide("game_stat.txt", year)))

# Which was the latest game?
    file.writelines('\n'+str(get_latest("game_stat.txt")))

# How many games do we have by genre?
    genre = str(input("Write the genre, what you looking for:"))
    file.writelines('\n' + str(count_by_genre("game_stat.txt", genre)))


# What is the line number of the given game (by title)?
    title = str(input("Write the title, what you looking for:"))
    file.writelines('\n' + str(get_line_number_by_title("game_stat.txt", title)))

# What are the genres?
    file.writelines('\n' + str(get_genres('game_stat.txt')))