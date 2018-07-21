import random

capitals = [
    "Hanoi",
    "Budapest",
    "Paris",
    "Sofia",
    "Beijing"
]

word = random.choice(capitals)
word = list(word)
dashed_letters = list(word)
dashed_letters[0:len(word)] = "_"*len(word)
print(word)
print(dashed_letters)
turns= len(word)
while turns > 0:
    guess = input("Please guess a letter: ")
    if guess in word:
        print (guess,  " is correct!")
        index = (word.index(guess))
        dashed_letters[index] = guess
        print(dashed_letters)