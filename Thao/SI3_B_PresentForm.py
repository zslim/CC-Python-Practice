# A simple set of heuristic rules can be given as follows:
# If the verb ends in e, drop the e and add -ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, replace ie with y and add -ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding -ing
# By default just add -ing

# Write the script which takes infinitive verbs separated by one space as the command line arguments and displays their present participle form in separated lines.

import sys

# users = sys.argv

for verb in sys.argv:
    if verb[-2:] == 'ie':
        print(verb[:-2] + 'ying')
    elif verb[-1] == 'e':
        print(verb[:-1] + 'ing')
    # elif :
    else:
        print(verb + 'ing')
        

"""
vowels = "aeiou"

consonants = "bcdfghjklmnpqrstvwxyz"

print(2*verb[-1] + 'ing')
"""