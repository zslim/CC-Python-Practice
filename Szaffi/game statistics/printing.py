from reports import count_games, decide, count_by_genre, get_line_number_by_title, get_latest, get_genres

#How many games are in the file?
print(count_games("game_stat.txt"))

#Is there a game from a given year?

try:
    year = int(input("Write the year, you want to search:"))
    print(decide("game_stat.txt", year))
except ValueError:
    print("It needs number!")

#Which was the latest game?
print(get_latest('game_stat.txt'))

#How many games do we have by genre?
genre = str(input("Write the genre, what you looking for:"))
print(count_by_genre("game_stat.txt", genre))

#What is the line number of the given game (by title)?
title = str(input("Write the title, what you looking for:"))
print(get_line_number_by_title("game_stat.txt", title))

'''#What is the alphabetical ordered list of the titles?
print(sort_abc("game_stat.txt"))'''

#What are the genres?
print(get_genres('game_stat.txt'))