maze1=[['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ','F',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x',' ','x','x','x','x','x','x',' ','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ','x','x',' ',' ',' ','x'],
['x',' ','x','x','x','x','x','x',' ','x','x','x','x','x','x'],
['x',' ','x',' ',' ',' ',' ','x',' ',' ','x',' ',' ',' ','x'],
['x',' ','x',' ','x','x','x','x','x','x','x','x','x',' ','x'],
['x',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ','x',' ','x','x','x','x','x','x','x','x','x'],
['x',' ','x',' ','x',' ','x','x','x','x','x','x','x','x','x'],
['x',' ','x',' ','x',' ',' ',' ',' x',' ',' ',' ',' ',' ','F'],
['x',' ','x',' ','x',' ','x',' ','x','x','x',' ','x','x','x'],
['x',' ','x',' ','x',' ','x',' ','x','x','x',' ','x','x','x'],
['x',' ','x',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x',' ','x',' ','x','x','x','x','x','x','x','x','x'],
['x',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x','x','x','x',' ','x','x','x','x','x','x',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']]   #x=14 y=10

maze2=[['x','x','x','x','x','x','x','x','x','x','f','f','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ','x'],
['x',' ',' ','x','x','x','x',' ',' ','x',' ',' ','x',' ',' ','x',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ','x',' ',' ','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ','x','x','x','x','x','x','x','x','x','x',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ','x',' ',' ','x'],
['x',' ',' ','x','x','x','x','x','x','x',' ',' ','x',' ',' ','x',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x',' ',' ','x',' ',' ','x'],
['x','x','x','x',' ',' ','x',' ',' ','x','x','x','x',' ',' ','x',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']]

x=1
y=1
player = '\u001b[32m@\u001b[0m'

def render(x,y):

 maze[x][y]=player
 for line in maze:
   print(*line)

i=1

def move(x,y):
 original_x = x
 original_y = y
 if u_input == 'w':
     x=x-1
 elif u_input == 's':
     x=x+1
 elif u_input == 'a':
     y=y-1
 elif u_input == 'd':
     y=y+1
 if maze[x][y] == " ":
     return x, y
 if maze[x][y] == "F":
      return x, y
 if maze[x][y] == "f":
      return x, y
 if maze[x][y] == opi:
      return x, y
 else:
     return original_x, original_y

import random

def opponent(op_y,op_x):
    old_op_y= op_y
    old_op_x= op_x
    maze[old_op_y][old_op_x]=" "
    if i % 2 == 0:
        op_x= op_x + random.randrange(-1, 1, 2)
    else:
        op_y= op_y + random.randrange(-1, 1, 2)
    if maze[op_y][op_x] == " ":
        return op_y, op_x
    else:
        return old_op_y, old_op_x

def opponent2(op_x2,op_y2):
    old_op_x2= op_x2
    old_op_y2= op_y2
    maze[old_op_x2][old_op_y2]=" "
    print(i%2)
    if i % 2 == 0:
        op_x2= op_x2 - random.randrange(-1, 1, 2)
    else:
        op_y2= op_y2 - random.randrange(-1, 1, 2)
    if maze[op_x2][op_y2] == " ":
        return op_x2, op_y2
    else:
        return old_op_x2, old_op_y2

opi = '\u001b[31;1m#\u001b[0m'

if input('''\u001b[33;1m Would you like to play? 
         Press Y to play, or any other to quit: \u001b[0m ''') == 'Y':
 maze=maze1
 render(x,y)
 while True:
    print('''\u001b[33;1m Please enter a direction,
w to UP, s to DOWN, a to LEFT, d to RIGHT or q to QUIT: \u001b[0m ''')
    maze[x][y] =" "
    u_input = input()
    if u_input == 'q':
        break
    x, y = move(x,y)
    if maze[x][y] == "F":
          print("\u001b[33;1m You Won! \u001b[0m")
          print("\u001b[33;1m Proceed for the next Level: \u001b[0m")
          maze= maze2
          x=12
          y=1
          op_y=10
          op_x=17
          op_y2=1
          op_x2=1
    if maze[x][y] =="f":
          print("\u001b[33;1m You Won the WHOLE GAME!!! \u001b[0m")
    if maze==maze2:
          op_y, op_x = opponent(op_y,op_x)
          op_x2, op_y2 = opponent2(op_x2,op_y2)
          maze[op_y][op_x]=opi
          maze[op_x2][op_y2]=opi
    if maze[x][y] == opi:
          print("\u001bTHE HASHTAG MONSER CAUGHT YOU! GAME OVER! \u001b[0m")
          break
    render(x,y)
    print("Turn:"+str(i+1))
    i = i+1


else:
 print('I am sad, but see you next time')