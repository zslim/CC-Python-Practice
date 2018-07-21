# Report functions

def get_most_played(file_name):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        sold_title = ""
        sold = 0
        for game_line in lines:
            game_data = game_line.split('\t')
            if float(game_data[1]) > float(sold):
                sold_title = game_data[0]
                sold = game_data[1]
        return sold_title


def sum_sold(file_name):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        total_sold = 0
        for game_line in lines:
            game_data = game_line.split('\t')
            sold = float(game_data[1])
            total_sold = total_sold + sold
        return total_sold


def get_selling_avg(file_name):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        avg = 0
        total_sold = 0
        for game_line in lines:
            game_data = game_line.split('\t')
            sold = float(game_data[1])
            total_sold = total_sold + sold
        avg = float(total_sold/len(lines))
        return avg


def count_longest_title(file_name):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        char_num = 0
        for game_line in lines:
            game_data = game_line.split('\t')
            if char_num < len(game_data[0]):
                char_num = len(game_data[0])
        return char_num


def get_date_avg(file_name):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        date_avg = 0
        date = 0
        total_date = 0
        for game_line in lines:
            game_data = game_line.split('\t')
            date = int(game_data[2])
            total_date = total_date + date
        date_avg = int(total_date/len(lines)) + (total_date%len(lines)>0)
        return date_avg 


def get_game(file_name, title):
    with open(file_name, "r") as stat_file:
        lines = stat_file.readlines()
        details = []
        for game_line in lines:
            game_data = game_line.split('\t')
            if (game_data[0]) == title:
                game_data[1] = float(game_data[1])
                game_data[2] = int(game_data[2])
                details = game_data
                details[4] = details[4].rstrip("\n")
        if details == []:
            details = "No such game found"

        return (details)
