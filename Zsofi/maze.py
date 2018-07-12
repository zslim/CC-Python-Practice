# get ch

import os
import sys
import random
from colorama import Fore, Style
from copy import deepcopy


def def_mazes():

    levels = []

    maze1 = [
        "+-----+-------+------------+------+",
        "|     |       |            |      |",
        "|     |     +-+     --+    +--+   |",
        "|   +-+     |       |         |   |",
        "|   |   +---++   +--+---+     |   |",
        "|       |    |   |      |   --+-  |",
        "|  ---+    --+---+    --+     |   |",
        "|     |      |   |      |     |   |",
        "|   --+  ----+   +---   |   --+-  |",
        "|     |      |   |     -+     |   |",
        "|         ---+   |      |         |",
        "+----------------+------+---------+",
    ]
    maze1_list = list(map(list, maze1))

    levels.append(maze1_list)

    maze2 = [
        "+----------------+------------+----------+---------+",
        "|                |            |          |         |",
        "|   ----+--      |      ------+---       |     ----+",
        "|       |     ---+--+--       |     -----+--+      |",
        "|     --+--+     |  |    -----+--           |  ----+",
        "|  |    |  |     |            |     |    |         |",
        "|  |    +--+---  +---------+  +-----+----+----+    |",
        "|  +--  |        |         |  |          |    |  --+",
        "|       |             |       |  |   ----+-        |",
        "|       |   |   ------+--  ---+--+-      |    -----+",
        "+-------+---+-        |       |       ---+-        |",
        "|       |   |    +----+-------+--+--     |   ---+--+",
        "|  |             |               |    -+-+--    |  |",
        "|  +-------------+--  +----------+--   | |    --+  |",
        "|                     |          |          |      |",
        "+---------------------+----------+----------+------+",
    ]
    maze2_list = list(map(list, maze2))

    levels.append(maze2_list)

    maze3 = [
        "+-----+--------+--------+-------------+--------+--------+---+-------+",
        "|              |        |                      |        |   |       |",
        "+---  +---  +--+--+  ---+------+      |     +--+---+    |       |   |",
        "|     |     |           |      |   ---+-    |      |       |  --+   |",
        "+  +--+--+  +---+---    |   ---+-     |     |   +--+---+   |    |   |",
        "|  |     |      |     --+      |  ----+--   |   |      |  -+--  | --+",
        "+-----+--+  +---+   |   +----  |      |   --+-  |  ----+   |    |   |",
        "|     |     |       |   |        |    |     |      |   |   |  +-+-  |",
        "|  +--+--+  |  -+---+   |  +--+--+----+-----+---+  |   +---+  |     |",
        "|  |     |      |   |      |          |                |      |  ---+",
        "|  |  +--+   +--+     +----+--   |        |   +-----+  |   +--+     |",
        "|     |      |      --+    +--+--+-----+      |     |      |     |  |",
        "|   --+--    |   +----+-               |      |     +----+-+   +-+--+",
        "|     |  +---+-  |        ----+---+-   |   |  +--+   |   |     |    |",
        "+---  |  |       |    |       |   |    +---+     |     |    |    ---+",
        "|     +--+-------+  --+----   +---+--      +-----+  ---+    |       |",
        "|   |                 |       |         |                   |  -----+",
        "+---+-----------------+-------+---------+-------------------+-------+",
    ]
    maze3_list = list(map(list, maze3))

    levels.append(maze3_list)

    return levels


def interact():
    return input("What is your move? ")


def move(ans, y, x, maze, kx, ky, got_xkey, tkx, tky, got_tkey, tx, ty, jx, jy):
    move_y = {"a": -1, "d": 1}
    move_x = {"w": -1, "s": 1}

    xkey_collected = got_xkey
    tkey_collected = got_tkey

    if len(set(ans)) == 1:
        m = list(set(ans))[0]
        steps = len(ans)

        if m in move_y:
            for i in range(steps):
                temp = y + move_y[m]
                if y not in [0, len(maze[0]) - 1] and maze[x][temp] == " ":
                    y = temp
                else:
                    break
        elif m in move_x:
            for i in range(steps):
                temp = x + move_x[m]
                if x not in [0, len(maze) - 1] and maze[temp][y] == " ":
                    x = temp
                else:
                    break

    if x == kx and y == ky:
        xkey_collected = True

    if x == tkx and y == tky:
        tkey_collected = True
    
    if x == tx and y == ty:
        x, y = [jx, jy]

    return x, y, xkey_collected, tkey_collected

# def wrap_cyan(string):
#    return "\x1b[36m" + string + "\x1b[0m"


def output(layout, x, y, kx, ky, got_xkey, tkx, tky, got_tkey, tx, ty):
    os.system('clear')
    print(Fore.LIGHTGREEN_EX + "Move with w-a-s-d keys, exit with q" + Style.RESET_ALL)

    #if got_xkey:
    #    layout[exit_x][exit_y] = " "

    maze = deepcopy(layout)
    if not got_xkey:
        maze[kx][ky] = chr(128477)
    if not got_tkey:
        maze[tkx][tky] = Fore.YELLOW + chr(9765) + Style.RESET_ALL
    else:
        maze[tx][ty] = chr(127786)
    maze[x][y] = Fore.CYAN + Style.BRIGHT + "O" + Style.RESET_ALL
    for row in maze:
        print(*row, sep="")


def winning(x, y, map):

    if x in [0, len(map) - 1] or y in [0, len(map[1]) - 1]:
        win = True
    else:
        win = False

    return win


def main():
    vars = {"maps": [], "level": 0, "map": [], "x": 1, "y": 1, "px": 1, "py": 1,
            "ans": None, "seen": [], "xkey_x": [1, 10, 11], "xkey_y": [29, 49, 48],
            "exit_x": [6, 0, 10], "exit_y": [34, 32, 0], "tkey_x": [7, 4, 12], 
            "tkey_y": [3, 18, 10], "tel_x": [1, 11, 7], "tel_y": [11, 2, 30],
            "jumpto_x": [5, 7, 16], "jumpto_y": [15, 39, 20],}

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    vars["maps"] = def_mazes()

    play_game = True
    win_game = False

# print(vars["maps"])

    while play_game:
        if vars["level"] > 0:
            wait = True
            while wait:
                cont = input("Press 'y' if ready for next level: ")

                sys.stdout.write(CURSOR_UP_ONE)
                sys.stdout.write(ERASE_LINE)
                if cont == "y":
                    wait = False

        vars["map"] = vars["maps"][vars["level"]]

        vars["x"], vars["y"] = [1, 1]
        play_level = True
        win_level = False
        got_xkey = False
        got_tkey = False
        key_x = vars["xkey_x"][vars["level"]]
        key_y = vars["xkey_y"][vars["level"]]
        exit_x = vars["exit_x"][vars["level"]]
        exit_y = vars["exit_y"][vars["level"]]
        tkey_x = vars["tkey_x"][vars["level"]]
        tkey_y = vars["tkey_y"][vars["level"]]
        tel_x = vars["tel_x"][vars["level"]]
        tel_y = vars["tel_y"][vars["level"]]
        jumpto_x = vars["jumpto_x"][vars["level"]]
        jumpto_y = vars["jumpto_y"][vars["level"]]

        while play_level:

            output(vars["map"], vars["x"], vars["y"], key_x, key_y, got_xkey, tkey_x, tkey_y, got_tkey, tel_x, tel_y)
            if winning(vars["x"], vars["y"], vars["map"]):
                print("Level complete :)")
                win_level = True
                play_level = False
                continue

            vars["ans"] = interact()
            if vars["ans"] == "q":
                play_game = False
                play_level = False
                continue

            vars["x"], vars["y"], got_xkey, got_tkey = move(vars["ans"], vars["y"], vars["x"],
                                                  vars["map"], key_x, key_y, got_xkey, tkey_x, 
                                                  tkey_y, got_tkey, tel_x, tel_y, jumpto_x, jumpto_y)
            
            if got_xkey:
                vars["map"][exit_x][exit_y] = " "
            
        if win_level:
            vars["level"] += 1

        if vars["level"] > len(vars["maps"]) - 1:
            play_game = False
            win_game = True

    if win_game:
        print(Fore.YELLOW + Style.BRIGHT + "You just won Python!" + Style.RESET_ALL)

    print("See you next time, pal \n")


main()
