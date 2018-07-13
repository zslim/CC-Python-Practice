def count_games(file_name):
    with open(file_name, 'r') as f:
        games = f.readlines()
        return len(games)


def decide(file_name, year):
    with open(file_name, 'r') as f:
        if str(year) in f.read():
            return True
        else:
            return False


def get_latest(file_name):
    games = []
    with open(file_name, 'r') as f:
        rows = f.readlines()
        for i in rows:
            row = i.split('\t')
            games.append((row[0], row[2]))
    games = dict(games)
    games = sorted(games, key=games.__getitem__, reverse=True)
    return str(games[0])


def count_by_genre(file_name, genre):
    with open(file_name, 'r') as f:
        count = 0
        for i in f:
            if genre in i:
                count += 1
    return count


def get_line_number_by_title(file_name, title):
    with open(file_name, 'r') as f:
        count = 0
        for i in f:
            count += 1
            if title in i:
                return count
        raise ValueError
