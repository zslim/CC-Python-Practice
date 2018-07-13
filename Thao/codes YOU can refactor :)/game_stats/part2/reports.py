
# Report functions


# 1. What is the title of the most played game (i.e. sold the most copies)?
def get_most_played(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        top_sold = 0
        top_title = ""
        for game_line in lines:
            properties = game_line.split("\t")
            most_played_title = properties[0]
            copy = properties[1]
            if float(copy) > top_sold:
                top_sold = float(copy)
                top_title = most_played_title
        return top_title


# 2. How many copies have been sold total?
def sum_sold(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        total_sold = 0
        for game_line in lines:
            properties = game_line.split("\t")
            copy = float(properties[1])
            total_sold += copy
        return total_sold


# 3. What is the average selling?
def get_selling_avg(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        total_sold = 0
        for game_line in lines:
            properties = game_line.split("\t")
            copy = float(properties[1])
            total_sold += copy
        return total_sold / len(lines)


# 4. How many characters long is the longest title?
def count_longest_title(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        longest_title = 0
        for game_line in lines:
            properties = game_line.split("\t")
            title = properties[0]
            if len(title) > longest_title:
                longest_title = len(title)
        return longest_title


# 5. What is the average of the release dates?
def get_date_avg(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        release_date = 0
        for game_line in lines:
            properties = game_line.split("\t")
            date = int(properties[2])
            release_date += date
        return round(release_date / len(lines))


# 6. What properties has a game?
def get_game(file_name, title):
    with open(file_name, "r") as file:
        lines = file.readlines()
        for game_line in lines:
            properties = game_line.split("\t")
            if title in game_line:
                for prop in title:
                    properties[1] = float(properties[1])
                    properties[2] = int(properties[2])
                    properties[4] = properties[4].strip('\n')
                return properties
                break


# Bonus 1. How many games are there grouped by genre? ... in progress ...
def count_grouped_by_genre(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

        for game_line in lines:
            properties = game_line.split("\t")
            genre = properties[3]
            print(genre)
