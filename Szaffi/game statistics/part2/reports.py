#What is the title of the most played game (i.e. sold the most copies)?
def get_most_played(file_name):
    with open(file_name) as file:
        lines =file.readlines()
        most_copy_game = ""
        most_copy = 0
        for i in lines:
            data = i.split('\t')
            game_title = data[0]
            copy = data[1]
            if float(copy) > most_copy:
                most_copy = float(copy)
                most_copy_game = game_title
        return most_copy_game

#How many copies have been sold total?
def sum_sold(file_name):
    with open(file_name) as file:
        lines =file.readlines()
        total_sold = 0.0
        for i in lines:
            data = i.split('\t')
            copy = data[1]
            sum_data = total_sold + float(copy)
            total_sold = sum_data

        return total_sold

#What is the average selling?
def get_selling_avg(file_name):
    with open(file_name) as file:
        lines =file.readlines()
        total_sold = 0.0
        for i in lines:
            data = i.split('\t')
            copy = data[1]
            sum_data = total_sold + float(copy)
            total_sold = sum_data
        count = 0
        for line in lines:
            count +=1
        av_sold = total_sold / count
        return av_sold

#How many characters long is the longest title?
def count_longest_title(file_name):
    with open(file_name) as file:
        lines =file.readlines()
        longest_title = 0
        for i in lines:
            data = i.split('\t')
            title = data[0]
            title_lenght = len(title)
            if title_lenght > longest_title:
                longest_title = title_lenght
        return longest_title


#What is the average of the release dates?
def get_date_avg(file_name):
    with open(file_name) as file:
        lines =file.readlines()
        total_years = 0
        count = 0
        for i in lines:
            data = i.split('\t')
            year = data[2]
            sum_years = total_years + float(year)
            total_years = sum_years
            count +=1
        av_years = total_years / count        
        return int("{:.0f}".format(av_years))
#What properties has a game?
def get_game(file_name, title):
    title = str(title)
    with open(file_name) as file:
        lines =file.readlines()
        for i in lines:
            if title in i:
                i = i.replace('\n','')
                i = i.split('\t',-2)
                i[1]= float(i[1])
                i[2]= int(i[2])             
                return i
                break
    

