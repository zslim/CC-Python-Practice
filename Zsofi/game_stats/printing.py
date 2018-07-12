
# Printing functions
import reports


def print_count_games(file_name = "game_stat.txt"):
    count = reports.count_games(file_name)
    ans = "There are {} games in the file.".format(count)
    print(ans)
    return ans


def print_decide(file_name = "game_stat.txt"):
    year = int(input("Enter a year to see if there are any games from then: "))
    if reports.decide(file_name, year):
        ans = "The file contains at least one game released in {}.".format(year)
    else:
        ans = "The file does not contain any games released in {}.".format(year)
    print(ans)
    return ans


def print_get_latest(file_name = "game_stat.txt"):
    latest_game = reports.get_latest(file_name)
    ans = "{} is among the latest games in the file.".format(latest_game)
    print(ans)
    return ans


def print_count_by_genre(file_name = "game_stat.txt"):
    genre = input("Enter a genre to see how many games of that type there are in the data: ")
    count = reports.count_by_genre(file_name, genre)
    ans = "The file contains {n} games in the genre \'{g}\'.".format(n = count, g = genre)
    print(ans)
    return ans


def print_get_line_number_by_title(file_name = "game_stat.txt"):
    title = input("Enter a game title to find out it's line number: ")
    num = reports.get_line_number_by_title(file_name, title)
    ans = "The game {game} is in line number {n}.".format(game = title, n = num)
    print(ans)
    return ans


if __name__ == "__main__":
    print_count_games()
    print_decide()
    print_get_latest()
    print_count_by_genre()
    print_get_line_number_by_title()
