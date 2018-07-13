from reports import get_most_played, sum_sold, get_selling_avg,count_longest_title, get_date_avg, get_game

#What is the title of the most played game (i.e. sold the most copies)?
print(get_most_played("game_stat.txt"))
#How many copies have been sold total?
print(sum_sold("game_stat.txt"))
#What is the average selling?
print(get_selling_avg("game_stat.txt"))
#How many characters long is the longest title?
print(count_longest_title("game_stat.txt"))
#What is the average of the release dates?
print(get_date_avg("game_stat.txt"))
#What properties has a game?
title = str(input("Write the title, what you looking for:"))
print(get_game("game_stat.txt",title))

#print function---give in the list of functs and print in lines