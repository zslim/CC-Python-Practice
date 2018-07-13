
# Export functions

from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title, when_was_top_sold_fps

file_name = input("Enter a filename: ")
year = int(input("Is there a game from year: "))
genre = input("How many games are there by this genre: ")
title = input("What is the line number of the given game (title): ")

with open("judy.txt", "w") as file:
    file.writelines(str(count_games(file_name)))
    file.writelines("\n" + str(decide(file_name, year)))
    file.writelines("\n" + str(get_latest(file_name)))
    file.writelines("\n" + str(count_by_genre(file_name, genre)))
    file.writelines("\n" + str(get_line_number_by_title(file_name, title)))
    file.writelines("\n" + str(when_was_top_sold_fps(file_name)))

file = open("judy.txt", "r")
print(file.read())
file.close()

def main():
    pass

if __name__ == '__main__':
    main()
