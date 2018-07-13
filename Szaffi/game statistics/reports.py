
#How many games are in the file?
def count_games(file_name):
    with open(file_name) as file:
        counted_file = file.readlines()   
        count = 0
        for line in counted_file:
            count +=1
    
    return count

#Is there a game from a given year?
def decide(file_name,year):
    year = str(year)
    with open(file_name) as file:
        counted_file = file.readlines()
        for lines in counted_file:
            if year in lines: #need break because it doesn't exit the loop so it prints the last result
                return True
                break
        if year not in lines:
            return False

#Which was the latest game?
def get_latest(file_name):
    with open(file_name) as file:
        lines =file.readlines()
        latest_title = ""
        latest_date = 0
        for i in lines:
            data = i.split('\t')
            game_title = data[0]
            release_date = data[2]
            if int(release_date) > latest_date:
                latest_date = int(release_date)
                latest_title = game_title
        return latest_title

#How many games do we have by genre?
def count_by_genre(file_name,genre):
    genre = str(genre)
    with open(file_name) as file:
        counted_file = file.readlines()   
        count = 0
        for line in counted_file:
            if genre in line:
                count +=1    
    return count

#What is the line number of the given game (by title)?
def get_line_number_by_title(file_name, title):
    title = str(title)
    count = 1
    with open(file_name) as file:
        counted_file = file.readlines()
        for lines in counted_file:
            if title not in lines:
                count +=1
                continue
            if title in lines:#needs a break to quit from the loop again!!
                return count
                break
        
#What is the alphabetical ordered list of the titles?
'''def sort_abc(file_name):
    with open(file_name) as file:
        lines =file.readlines()
        x = 0
        titles = []
        for i in lines:
            data = i.split('\t')
            game_title = data[0]
            titles.append(game_title)
        abc=[]
        alphabet = 'ABCDEFGHIJKLMNOPGRSTUVWXYZ'
        while len(abc)<len(titles):            
            for i in titles:
                if i[x] == alphabet[x]:
                    abc.append(i)
                    x+=1
                    if i[x] == alphabet[0]
        return abc'''

#What are the genres?
def get_genres(file_name):
    with open(file_name) as file:
        lines =file.readlines()
        genres = []
        for i in lines:            
            i = i.replace('\n','')
            i = i.split('\t',-2)
            genre = i[3]                      
            genres.append(genre)
        genres = sorted(set(genres))
        return list(genres)
