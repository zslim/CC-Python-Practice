
# Report functions


def read_games(file_name):
    game_properties = ["title", "total_copies_sold", "release_date", "genre", "publisher"]
    games = []
    with open(file_name) as f:
        for line in f:
            line = line.rstrip()
            row = line.split("\t")
            games.append(dict(zip(game_properties, row)))
    return games


def count_games(file_name):
    games = read_games(file_name)
    return len(games)


def decide(file_name, year):
    games = read_games(file_name)
    dates = [int(line["release_date"]) for line in games]
    return year in dates


def get_latest(file_name):
    games = read_games(file_name)
    latest_year = max([int(line["release_date"]) for line in games])
    games_from_latest = [line["title"] for line in games if line["release_date"] == str(latest_year)]
    return games_from_latest[0]


def count_by_genre(file_name, genre):
    games = read_games(file_name)
    game_types = [line["genre"] for line in games]
    return game_types.count(genre)


def get_line_number_by_title(file_name, title):
    with open(file_name) as f:
        file_content = list(f)
    file_content = [elem.split("\t") for elem in file_content]
    list_of_titles = [row[0] for row in file_content]
    return list_of_titles.index(title) + 1

# bonus functions


def sort_abc(file_name):
    pass
    # returns a list of strings
    # without using the built-in sort() and sorted()


def get_genres(file_name):
    pass
    # returns a list without duplicates, in alphabetical order


def when_was_top_sold_fps(file_name):
    pass
    # returns a year as an integer, or ValueError if no fps found
