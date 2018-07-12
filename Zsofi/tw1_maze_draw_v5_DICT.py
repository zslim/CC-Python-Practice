# get ch

import os
from colorama import Fore, Style

vars = {"levels": [], "level": None, "map": [], "x": None, 
"y": None, "px": None, "py": None, "ans": None}

def repl_by_index(string, index, replacement):
    list_of_chars = list(string)
    list_of_chars[index] = replacement
    return("".join(list_of_chars))

def def_mazes():

    maze1 = [
    "+-----+-------+------------+------+",
    "|O    |       |            |      |",
    "|     |     +-+     --+    +--+   |",
    "|   +-+     |       |         |   |",
    "|   |   +---+    +--+---+     |   |",
    "|       |        |      |   --+-  |",
    "|  ---+    --+---+    --+     |    ",
    "|     |      |   |      |     |   |",
    "|   --+  ----+   +---   |   --+-  |",
    "|     |      |   |     -+     |   |",
    "|         ---+   |      |         |",
    "+----------------+------+---------+",
    ]
    vars["levels"].append(maze1)

    maze2 = [
    "+----------------+------------+- --------+---------+",
    "|                |            |          |         |",
    "|   ----+--      |      ------+---       |     ----+",
    "|       |     ---+--+--       |     -----+--+      |",
    "|     --+--+     |  |    -----+--           |  ----+",
    "|  |    |  |     |            |     |    |         |",
    "|  |    +--+---  +---------+  +-----+----+----+    |",
    "|  +--  |        |         |  |          |    |  --+",
    "|       |             |       |  |   ----+-        |",
    "|      O|   |   ------+--  ---+--+-      |    -----+",
    "+-------+---+-        |       |       ---+-        |",
    "|       |   |    +----+-------+ -+--     |   ---+--+",
    "|  |             |               |    -+-+--    |  |",
    "|  +-------------+--  +----------+--   | |    --+  |",
    "|                     |          |          |      |",
    "+---------------------+----------+----------+------+",
    ]
    vars["levels"].append(maze2)

    maze3 = [
    "+--- -+--------+--------+-------------+--------+--------+---+-------+",
    "|O             |        |                      |        |   |       |",
    "+---  +---  +--+--+  ---+------+      |     +--+---+    |       |   |",
    "|     |     |           |      |   ---+-    |      |       |  --+   |",
    "+  +--+--+  +---+---    |   ---+-     |     |   +--+---+   |    |   |",
    "|  |     |      |     --+      |  ----+--   |   |      |  -+--  | --+",
    "+-----+--+  +---+   |   +----  |      |   --+-  |  ----+   |    |   |",
    "|     |     |       |   |        |    |     |      |   |   |  +-+-  |",
    "|  +--+--+  |  -+---+   |  +--+--+----+-- --+---+  |   +---+  |     |",
    "|  |     |      |   |      |          |                |      |  ---+",
    "   |  +--+   +--+     +----+--   |        |   +-----+  |   +--+     |",
    "|     |      |      --+    +--+--+-----+      |     |      |     |  |",
    "|   --+--    |   +----+-               |      |     +----+-+   +-+--+",
    "|     |  +---+-  |        ----+---+-   |   |  +--+   |   |     |    |",
    "+---  |  |       |    |       |   |    +---+     |     |    |    ---+",
    "|     +--+-------+  --+----   +---+--      +-----+  ---+    |       |",
    "|   |                 |       |         |                   |  -----+",
    "+---+-----------------+-------+---------+-------------------+-------+",
    ]
    vars["levels"].append(maze3)

def get_coord():
    row = list(filter(lambda x: "O" in x, vars["map"]))[0]
    vars["x"] = vars["map"].index(row)
    vars["y"] = row.index("O")

def interact():
    vars["ans"] = input("What is your move? ")

def move():
    move_y = {"a": -1, "d": 1}
    move_x = {"w": -1, "s": 1}

    ans = vars["ans"]
    y = vars["y"]
    x = vars["x"]
    prev_y = vars["y"]
    prev_x = vars["x"]
    maze = vars["map"]

    if len(set(ans)) == 1:
        m = list(set(ans))[0]
        steps = len(ans)
    
        if m in move_y:
            for i in range(steps):
                if y not in [0, len(maze[0]) - 1] and maze[x][y + move_y[m]] == " ":
                    y = y + move_y[m]
                else: 
                    break
        elif m in move_x:
            for i in range(steps):
                if x not in [0, len(maze) - 1] and maze[x + move_x[m]][y] == " ":
                    x = x + move_x[m]
                else:
                    break

    vars["x"] = x
    vars["y"] = y
    vars["px"] = prev_x
    vars["py"] = prev_y

#def wrap_cyan(string):
#    return "\x1b[36m" + string + "\x1b[0m"

def appear():
    maze = vars["map"]
    px = vars["px"]
    x = vars["x"]

    maze[px] = repl_by_index(maze[px], vars["py"], " ")
    maze[x] = repl_by_index(maze[x], vars["y"], "O")
    vars["map"] = maze
    
def output():
    os.system('clear')
    print(Fore.LIGHTGREEN_EX + "Move with w-a-s-d keys, exit with q" + Style.RESET_ALL)

    layout = vars["map"]
    #print(Olayout, sep="\n")
    for i in range(len(layout)):
        if "O" in layout[i]:
            p = layout[i].index("O")
            
            print(layout[i][:p] + 
            Fore.CYAN + Style.BRIGHT + "O" + Style.RESET_ALL + 
            layout[i][p + 1:])
        else:
            print(layout[i])        

def winning():

    if vars["x"] in [0, len(vars["map"]) - 1] or vars["y"] in [0, len(vars["map"][1]) - 1]:
        win = True
    else:
        win = False
    
    return win

def_mazes()
vars["level"] = 0

# print(vars["levels"])

while vars["level"] <= len(vars["levels"]) - 1:
    if vars["level"] > 0:
        cont = input("Ready for next level? (y/n) ")
        if cont != "y":
            break
    
    vars["map"] = vars["levels"][vars["level"]]
    get_coord()

    while True:
        output()
       
        if winning():
            print("Level complete :)")
            break

        interact()
        if vars["ans"] == "q":
            break

        move()
        appear()
    
    if vars["ans"] == "q":
        break

    vars["level"] += 1


if vars["level"] > len(vars["levels"]) - 1:
    print(Fore.YELLOW + Style.BRIGHT + "You just won Python!" + Style.RESET_ALL)

print("See you next time, pal \n")

    

    
    


        










