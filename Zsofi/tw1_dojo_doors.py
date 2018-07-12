# Dojo: 100 doors
# 12.06.2018.

"""
Description:

You have 100 doors in a hallway in a row that are all initially closed. 
You make 100 passes by the doors. The first time through, you visit every door 
and toggle the door (if the door is closed, you open it; if it is open, you 
close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). 
The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only 
visit the 100th door.

Write a script that lists the number (the name) of the open doors after you 
visited all the 100 doors 100 times. This is an individual assignment but of 
course, you can get help from the others.
"""

doors = dict(zip(range(100), [False]*100))
# a value is True if the door is open and False if it is closed

def toggle(index, num):
    return index % (num + 1) == 0

for n in range(100):
    iterator = list(filter(lambda x: toggle(x, n), doors))

    for i in iterator:
        doors[i] = not doors[i]

open_doors = []

for door, is_open in doors.items():
    if is_open == True:
        open_doors.append(door)
    
print("Open doors at the end of the 100th pass:")
print(*open_doors, sep = ", ")