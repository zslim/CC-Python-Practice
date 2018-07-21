import sys
import pickle

file = open("/home/doram/Desktop/Python/anagrams.csv", "r")
dictionary = {}
for line in file.readlines():
    word = line.strip().lower()
    sortedLetters = sorted(list(word))
    sortedWord = "".join(sortedLetters)
    if sortedWord in dictionary:
        dictionary[sortedWord].append(word)
    else:
        dictionary[sortedWord] = [word]
with open('words.pickle', 'wb') as file:
    pickle.dump(dictionary, file)

with open('words.pickle', 'rb') as file:
    dictionary = pickle.load(file)


def sort_letters(a):
    return "".join(sorted(list(a)))


def solver(a):
    sorted_a = sort_letters(a)
    if sorted_a in dictionary:
        return dictionary[sorted_a]
    else:
        return []


solver('/home/doram/Desktop/Python/anagrams.csv')
in_word = input("Enter a word: ")
in_word = sorted(list(in_word))
in_word = "".join(in_word)
if in_word in dictionary:
    print("Your word and it's anagrams are the following: ")
    print(*dictionary.get(in_word))
else:
    print("I couldn't find any anagram for your word.")
