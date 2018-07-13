import reports

fi = "part2/game_stat.txt"

with open("export.txt", 'w') as f:
    f.write(str(reports.get_most_played(fi)) + '\n')
    f.write(str(reports.sum_sold(fi)) + '\n')
    f.write(str(reports.get_selling_avg(fi)) + '\n')
    f.write(str(reports.get_date_avg(fi)) + '\n')
    title = input("title: ")
    f.write(str(print(reports.get_game(fi, title))) + '\n')