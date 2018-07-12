
# Export functions

import printing

read_file = input("Please enter the name of the file that contains your data: ")

count = printing.print_count_games(read_file)
decision = printing.print_decide(read_file)
latest = printing.print_get_latest(read_file)
count_by_genre = printing.print_count_by_genre(read_file)
line_number_by_title = printing.print_get_line_number_by_title(read_file)

with open("exported.txt", "w") as ex:
    ex.write(count + "\n")
    ex.write(decision + "\n")
    ex.write(latest + "\n")
    ex.write(count_by_genre + "\n")
    ex.write(line_number_by_title + "\n")
