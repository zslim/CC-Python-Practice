# Write a program which prints the top 25 three-digit natural numbers divisible by 7 or by 9.
# Each number should be displayed in a separate line.

i = 0

for x in range(100, 999):
    if i == 25:
        break
    if x % 7 == 0:
        print(x)
        i = i + 1
    elif x % 9 == 0:
        print(x)
        i = i + 1
    else:
        pass


# másik megoldás
"""    
i = 0

for x in range(100, 999):
        if x % 7 == 0 and i != 25:
        print(x)
        i = i + 1
    elif x % 9 == 0 and i != 25:
        print(x)
        i = i + 1
    else:
        pass
"""