#dashed word:
word = ["h","e","l","l","o","w","o","r","d"]
dashed_word = []
dashed_word[0:len(word)] = "_"*len(word)

print(dashed_word)
turns = len(word)
failed = 0
char_index = 0
while turns > 0:
    guess = input("Guess a character: ")
    if guess in word:
        char_index = int(word.index(guess))
        dashed_word[char_index] = guess
        try:
            char_index = int(word.index(guess, char_index+1))
        except ValueError:
            pass
        dashed_word[char_index] = guess
        print(dashed_word)
    else:
        print("Wrong")
        turns -=1  
        failed += 1