
# Printing functions
import reports


def get_most_played(file_name = "game_stat.txt"):
    most_played = reports.get_most_played(file_name)
    ans = "The most played game is {}.\n".format(most_played)
    print(ans)
    return ans


def sum_sold(file_name = "game_stat.txt"):
    total_sold = reports.sum_sold(file_name)
    ans = "{} million copies were sold in total.\n".format(total_sold)
    print(ans)
    return ans


def get_selling_avg(file_name = "game_stat.txt"):
    selling_avg = reports.get_selling_avg(file_name)
    ans = "The average selling is {:.2f} million copies.\n".format(selling_avg)
    print(ans)
    return ans


def count_longest_title(file_name = "game_stat.txt"):
    length_of_longest_title = reports.count_longest_title(file_name)
    ans = "The length of the longest game title in the file is {}.\n".format(length_of_longest_title)
    print(ans)
    return ans


def get_date_avg(file_name = "game_stat.txt"):
    avg = reports.get_date_avg(file_name)
    ans = "The 'average' of the release dates is {}, whatever that means.\n".format(avg)
    print(ans)
    return ans


def get_game(file_name = "game_stat.txt"):
    title = input("Enter a game to see it's properties: ")
    prop = reports.get_game(file_name, title)
    prop_width = max([len(str(x)) for x in prop])
    prop_names = ["Title:", "Total copies sold (million):", "Release date:", "Genre:", "Publisher:"]
    zipped = list(zip(prop_names, prop))

    ans = "Properties of the entered game:\n"
    for row in zipped:
        ans += "{name:<30s} {prop:<{width}}\n".format(name = row[0], prop = row[1], width = prop_width)
    print(ans)
    return(ans)


if __name__ == "__main__":
    get_most_played()
    sum_sold()
    get_selling_avg()
    count_longest_title()
    get_date_avg()
    get_game()
