
# Report functions


# 1. How many games are in the file?
# file_name = input("Enter a filename: ")
def count_games(file_name):
    with open(file_name, "r") as file:
        return len(file.readlines())


# 2. Is there a game from a given year?
#year = int(input("\nIs there a game from year: "))
def decide(file_name, year):
    with open(file_name, "r") as file:
        lines = file.readlines()

        for line in lines:
            # print(line.split("\t"))
            if str(year) in line:
                return True
                break
        return False

        """if str(year) not in line:  # hmm..?
            return False"""


# 3. Which was the latest game?
def get_latest(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        latest = 0
        latest_title = ""
        for game_line in lines:
            properties = game_line.split("\t")
            title = properties[0]
            date = properties[2]
            if int(date) > latest:
                latest = int(date)
                latest_title = title
        return latest_title


# 4. How many games do we have by genre?
def count_by_genre(file_name, genre):
    with open(file_name, "r") as file:
        lines = file.readlines()
        number_of_games = 0
        for line in lines:
            if str(genre) in line:
                number_of_games += 1
        return number_of_games


# 5. What is the line number of the given game (by title)?
def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as file:
        lines = file.readlines()
        line_number = 1
        for line in lines:
            if str(title) not in line:
                line_number += 1
                #continue
            if str(title) in line:
                return line_number
                #break


# Bonus 1. What is the alphabetical ordered list of the titles? # ... in progress ...
"""def sort_abc(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        #latest = 0
        #latest_title = ""
        for game_line in lines:
            properties = game_line.split("\t")"""


# Bonus 2. What are the genres? # ... in progress ...
"""def get_genres(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        for game_line in lines:
            properties = game_line.split("\t")
            genre = properties[3]
            return genre"""


# Bonus 3. What is the release date of the top sold "First-person shooter" game?
def when_was_top_sold_fps(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        top_sold = 0
        top_sold_year = 0
        for game_line in lines:
            properties = game_line.split("\t")
            #title = properties[0]
            copy = properties[1]
            release_date = properties[2]
            if "First-person shooter" in properties:
                if float(copy) > top_sold:
                    top_sold = float(copy)
                    top_sold_year = int(release_date)
        return top_sold_year
