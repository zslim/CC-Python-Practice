
word = input("Please enter the infinite form of an English verb: ")


def ending(word):
    one = word[-3]
    two = word[-2]
    three = word[-1]
    CONSONANTS = "qwrtzpsdfghjklyxcvbnm"
    VOWELS = "aeiuo"
    if one in CONSONANTS and two in VOWELS and three in CONSONANTS:
        return True
    else:
        return False


def transform(word):
    exception = ['be', 'see', 'flee', 'knee']
    if word.endswith("ie"):
        transformed = word[0:len(word) - 2] + "ying"
    elif word.endswith("e") and word not in exception:
        transformed = word[0:len(word) - 1] + "ing"
    elif ending(word):
        transformed = word + word[-1] + "ing"
    else:
        transformed = word + "ing"
    print(transformed)


transform(word)
