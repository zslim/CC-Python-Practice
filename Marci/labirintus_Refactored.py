import random
from mazes import *
from os import system


def clear():
    _ = system('clear')


def render(player_row, player_column, player_simbol):
    clear()
    game_field[player_row][player_column] = player_simbol
    for line in game_field:
        print(*line)


def move(player_row, player_column, player_input, oponent_simbol):
    orig_play_x = player_row
    orig_play_y = player_column
    if player_input == 'w':
        player_row -= 1
    elif player_input == 's':
        player_row += 1
    elif player_input == 'a':
        player_column -= 1
    elif player_input == 'd':
        player_column += 1
    if game_field[player_row][player_column] == " ":
        return player_row, player_column
    if game_field[player_row][player_column] == "F":
        return player_row, player_column
    if game_field[player_row][player_column] == "f":
        return player_row, player_column
    if game_field[player_row][player_column] == oponent_simbol:
        return player_row, player_column
    else:
        print("\u001b[33;1m You hit a wall, please enter a different direction! \u001b[0m")
        return orig_play_x, orig_play_y


def opponent(op_y, op_x, turn, x, y):
    old_op_y = op_y
    old_op_x = op_x
    game_field[old_op_y][old_op_x] = " "
    if turn % 2 == 0:
        op_x += random.randint(-1, 1)
    else:
        op_y += random.randint(-1, 1)
    if game_field[op_y][op_x] == " ":
        return op_y, op_x
    else:
        op_x = old_op_x
        op_y = old_op_y
        if turn % 2 == 0:
            op_x -= random.randint(-1, 1)
        else:
            op_y -= random.randint(-1, 1)
        if game_field[op_y][op_x] == " ":
            return op_y, op_x
        else:
            return old_op_y, old_op_x


def opponent2(op_x2, op_y2, turn, x, y):
    old_op_x2 = op_x2
    old_op_y2 = op_y2
    game_field[old_op_x2][old_op_y2] = " "
    if turn % 2 == 0:
        op_x2 = op_x2 - random.randrange(-1, 1, 2)
    else:
        op_y2 = op_y2 - random.randrange(-1, 1, 2)
    if game_field[op_x2][op_y2] == " ":
        return op_x2, op_y2
    else:
        return old_op_x2, old_op_y2


def main():
    player_input = ""
    turn = 1
    player_row = 1
    player_column = 1
    player_simbol = '\u001b[32m@\u001b[0m'
    oponent_simbol = '\u001b[31;1m#\u001b[0m'
    start_answer = input('''\u001b[33;1m Would you like to play?
            Press Y to play, or any other to quit: \u001b[0m ''')
    global game_field
    if start_answer == 'Y' or "y" or "yes" or "Yes":
        game_field = maze_template_1
        render(player_row, player_column, player_simbol)
        while True:
            print('''\u001b[33;1m Please enter a direction,
            w to UP, s to DOWN, a to LEFT, d to RIGHT or q to QUIT: \u001b[0m ''')
            game_field[player_row][player_column] = " "     #This cancels player's last position
            player_input = input()
            if player_input == 'q':
                break
            player_row, player_column = move(player_row, player_column, player_input, oponent_simbol)       # This moves the player
            if game_field[player_row][player_column] == "F":                        # First level victory condition
                print("\u001b[33;1m You Won! \u001b[0m")
                print("\u001b[33;1m Proceed for the next Level: \u001b[0m")
                game_field = maze_template_2
                player_row = 12
                player_column = 1
                op_y = 1
                op_x = 8
                op_y2 = 1
                op_x2 = 1
            if game_field[player_row][player_column] == "f":              # Second level victory condition
                print("\u001b[33;1m You Won the WHOLE GAME!!! \u001b[0m")
                break
            if game_field == maze_template_2:                                          # Second level's initialization
                op_y, op_x = opponent(op_y, op_x, turn, player_row, player_column)
                op_x2, op_y2 = opponent2(op_x2, op_y2, turn, player_row, player_column)
                game_field[op_y][op_x] = oponent_simbol
                game_field[op_x2][op_y2] = oponent_simbol
            if game_field[player_row][player_column] == oponent_simbol:
                print("\u001bTHE HASHTAG MONSER CAUGHT YOU! GAME OVER! \u001b[0m")
                break
            render(player_row, player_column, player_simbol)
            print("Turn: "+str(turn))
            turn += 1
        else:
            print('I am sad, but see you next time')


if __name__ == '__main__':
    main()