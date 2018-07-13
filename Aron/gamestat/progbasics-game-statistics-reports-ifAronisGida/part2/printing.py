import reports

f = "part2/game_stat.txt"

print(reports.get_most_played(f))
print(reports.sum_sold(f))
print(reports.get_selling_avg(f))
print(reports.get_date_avg(f))
title = input("title: ")
print(reports.get_game(f, title))
