
# Report functions
#1: How many games are in the file?
#Expected name of the function: count_games(file_name)
#Expected output of the function: a number

def  count_games(file_name):
    return len(open(file_name).readlines())



#2:
#Is there a game from a given year?
#Expected name of the function: decide(file_name, year)
#Expected output of the function: boolean value


def decide(file_name, year):
    file_name = open(file_name).readlines()
    for line in file_name:
        if str(year) in line:
            return str(year) in line
            break
    if str(year) not in line: #ha 5-ot irsz akkor is true-t dob, szoval barmilyen szamot megtalal a doksiban...
        return False

#3: 
#Which was the latest game?
#Expected name of the function: get_latest(file_name)
#Expected output of the function: the title of the latest gae as a string
#Other expectation: if there is more than one, then return the first from the file


def get_latest(file_name):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        latest = 0
        latest_title = ""
        for game_line in lines:
            game_data = game_line.split('\t')
            if int(game_data[2]) > latest:
                latest = int(game_data[2])
                latest_title = game_data[0]
        return latest_title


#4 Expected name of the function: count_by_genre(file_name, genre)
# Expected output of the function: a number

def count_by_genre(file_name, genre):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        genre_count = 0
        for game_line in lines:
            game_data = game_line.split('\t')
            if game_data[3] == genre:
                genre_count += 1
        return genre_count


#5. What is the line number of the given game (by title)?
#Expected name of the function: get_line_number_by_title(file_name, title)
#Expected output of the function: a number (if there is no game found, then raises ValueError exception)

def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        line_count = 0
        for game_line in lines:
            line_count += 1
            game_data = game_line.split('\t')
            if game_data[0] == title:
                return line_count