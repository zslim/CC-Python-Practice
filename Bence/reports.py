def read_from_file(file_name):
    with open(file_name, 'r') as f:
        list_from_file = []
        for line in f:
            list_of_lines = [properties.strip() for properties in line.split('\t')]
            list_from_file.append(list_of_lines)
    return list_from_file


def count_games(file_name):
    list_from_file = read_from_file(file_name)
    game_counter = 0
    for line in list_from_file:
        game_counter += 1
    return game_counter


def decide(file_name, year):
    list_from_file = read_from_file(file_name)
    i = 0
    year_check = 0
    while i < len(list_from_file):
        year = str(year)
        if year == list_from_file[i][2]:
            year_check = 1
        i += 1
    if year_check == 1:
        return True
    else:
        return False


def get_latest(file_name):
    list_from_file = read_from_file(file_name)
    i = 1
    latest_year = int(list_from_file[0][2])
    latest_game = list_from_file[0][0]
    while i < len(list_from_file):
        if int(list_from_file[i][2]) > latest_year:
            latest_year = int(list_from_file[i][2])
            latest_game = list_from_file[i][0]
        i += 1
    return latest_game


def count_by_genre(file_name, genre):
    list_from_file = read_from_file(file_name)
    i = 0
    game_counter = 0
    while i < len(list_from_file):
        if genre == list_from_file[i][3]:
            game_counter += 1
        i += 1
    return game_counter


def get_line_number_by_title(file_name, title):
    list_from_file = read_from_file(file_name)
    i = 0
    line_number = -1
    while i < len(list_from_file):
        if title == list_from_file[i][0]:
            line_number = i + 1
            break
        i += 1
    if line_number == -1:
        raise ValueError('could not find {} in the file.'.format(title))
    return line_number


def sort_abc(file_name):
    list_from_file = read_from_file(file_name)
    list_of_titles = []
    i = 0
    while i < len(list_from_file):
        list_of_titles.append(list_from_file[i][0])
        i += 1
    j = 0
    temp = ''
    while j < len(list_of_titles):
        k = 0
        while k <= len(list_of_titles)-2:
            if list_of_titles[k] > list_of_titles[k+1]:
                temp = list_of_titles[k+1]
                list_of_titles[k+1] = list_of_titles[k]
                list_of_titles[k] = temp
            else:
                k += 1
        else:
            j += 1
    return list_of_titles


def get_genres(file_name):
    list_from_file = read_from_file(file_name)
    list_of_genres = []
    i = 0
    while i < len(list_from_file):
        if list_from_file[i][3] not in list_of_genres:
            list_of_genres.append(list_from_file[i][3])
        i += 1
    j = 0
    temp = ''
    while j < len(list_of_genres):
        k = 0
        while k <= len(list_of_genres)-2:
            if list_of_genres[k] > list_of_genres[k+1]:
                temp = list_of_genres[k+1]
                list_of_genres[k+1] = list_of_genres[k]
                list_of_genres[k] = temp
            else:
                k += 1
        else:
            j += 1
    return list_of_genres


def when_was_top_sold_fps(file_name):
    list_from_file = read_from_file(file_name)
    list_of_fps = []
    i = 0
    while i < len(list_from_file):
        if list_from_file[i][3] == 'First-person shooter':
            list_of_fps.append(list_from_file[i])
        i += 1
    if list_of_fps == []:
        raise ValueError('could not find a game with the genre "First-person shooter"')
    j = 1
    copies_sold = float(list_of_fps[0][1])
    year = int(list_of_fps[0][2])
    while j < len(list_of_fps):
        if float(list_of_fps[j][1]) > copies_sold:
            copies_sold = float(list_of_fps[j][1])
            year = int(list_of_fps[j][2])
        j += 1
    return year


print(count_games('game_stat.txt'))
print(decide('game_stat.txt', 2010))
print(get_latest('game_stat.txt'))
print(count_by_genre('game_stat.txt', 'RPG'))
print(get_line_number_by_title('game_stat.txt', 'Guild Wars'))
print(sort_abc('game_stat.txt'))
print(get_genres('game_stat.txt'))
print(when_was_top_sold_fps('game_stat.txt'))
