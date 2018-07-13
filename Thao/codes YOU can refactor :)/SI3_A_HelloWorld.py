# Create a script file that welcomes the user given to it. If no name was given, then it welcomes the whole world.

import sys

# users = sys.argv
    
for name in sys.argv:
    if len(sys.argv) == 1:
        print('Hello world!')
    elif len(sys.argv) > 1:
        print('Hello ' + name + '!')


#  másik próbálkozás
"""
for name in sys.argv:
    if len(sys.argv) > 1:
        print ('Hello ' + name + '!')  
    else:
        print ('Hello world!')
"""