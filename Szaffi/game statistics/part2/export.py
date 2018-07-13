from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game

#What is the title of the most played game (i.e. sold the most copies)?
with open("export.txt","w") as file:
    file.writelines(str(get_most_played("game_stat.txt")))
#How many copies have been sold total?
    file.writelines('\n' + str(sum_sold("game_stat.txt")))
#What is the average selling?
    file.writelines('\n' + str(get_selling_avg("game_stat.txt")))
#How many characters long is the longest title?
    file.writelines('\n' + str(count_longest_title("game_stat.txt")))
#What is the average of the release dates?
    file.writelines('\n' + str(get_date_avg("game_stat.txt")))
#What properties has a game?
    title = str(input("Write the title, what you looking for:"))
    file.writelines('\n' + str(get_game("game_stat.txt",title)))