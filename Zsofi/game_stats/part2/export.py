
# Export functions

import printing

with open("part2/exported2.txt", "w+") as ex:
    ex.write(printing.get_most_played())
    ex.write(printing.sum_sold())
    ex.write(printing.get_selling_avg())
    ex.write(printing.count_longest_title())
    ex.write(printing.get_date_avg())
    ex.write(printing.get_game())
