
# Report functions


def read_games(file_name):
    game_properties = ["title", "total_copies_sold", "release_date", "genre", "publisher"]
    games = []
    with open(file_name) as f:
        for line in f:
            line = line.rstrip()
            row = line.split("\t")
            row[1] = float(row[1])
            row[2] = int(row[2])
            games.append(dict(zip(game_properties, row)))
    return games


def get_most_played(file_name):
    list_of_games = read_games(file_name)
    max_sold = max([game["total_copies_sold"] for game in list_of_games])
    most_played = [game["title"] for game in list_of_games if game["total_copies_sold"] == max_sold]
    return most_played[0]


def sum_sold(file_name):
    list_of_games = read_games(file_name)
    selling = [game["total_copies_sold"] for game in list_of_games]
    return sum(selling)


def get_selling_avg(file_name):
    return sum_sold(file_name) / len(read_games(file_name))


def count_longest_title(file_name):
    list_of_games = read_games(file_name)
    titles = [game["title"] for game in list_of_games]
    return len(max(titles, key = len))


def get_date_avg(file_name):
    list_of_games = read_games(file_name)
    dates = [game["release_date"] for game in list_of_games]
    return round(sum(dates) / len(dates) + 0.5)


def get_game(file_name, title):
    list_of_games = read_games(file_name)
    game_properties = []
    for game in list_of_games:
        if game["title"] == title:
            game_properties = [v for k, v in game.items()]
            break
    if game_properties == []:
        raise ValueError("Game not found")
    else:
        return game_properties
