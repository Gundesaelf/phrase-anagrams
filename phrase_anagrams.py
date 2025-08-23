# |---------------------------------IMPORTS---------------------------------|

import sys
from colorama import Fore, init
from collections import Counter

init()

# |---------------------------------PROJECT_GOAL---------------------------------|

'''
The goal of this project is to do the following:

    > load a dictionary file
    > accept a name from user
    > set limit = length of name
    > start empty list to hold anagram phrase

    > while length of phrase < limit:
        ->> generate list of dictionary words that fit in name
        ->> present words to user
        ->> present remaining letters to user
        ->> present current phrase to user
        ->> ask user to input word or start over

        ->> if user input can be made from remaining letters:
            ->>>  accept choice of new word or words from user
            ->>> remove letters in choice from letters in name
            ->>> return choice and remaining letters in name

        ->> if choice is not a valid selection:
            ->>> ask user for new choice or let user start over

        ->> add choice to phrase and show to user
        ->> generate new list of words and repeat process

    > when phrase length equals limit value:
        ->> display final phrase
        ->> ask user to start over or to exit
'''

# |---------------------------------FUNCTIONS---------------------------------|

def load_file():
    fname = '2of4brif.txt'
    
    try:
        with open(fname) as file:
            loaded_txt = file.read().strip().split()
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(Fore.LIGHTRED_EX + f'\nError opening {fname}. Terminating program.')
        sys.exit(1)

def find_anagrams(letters, words):
    anagrams = []

    for word in words:
        if not (Counter(word) - letters):
            anagrams.append(word)
    return anagrams

def main():
    words = sorted(load_file() + ['a', 'i'])

    while True:
        print(Fore.LIGHTBLUE_EX)
        name = input('Enter a name or type \'#\' to exit: ').lower().replace(' ', '').replace('-', '')

        if name == '#':
            sys.exit()

        name_count = Counter(name)
        limit = len(name)
        phrase = []

        while sum(name_count.values()) > 0:
            anagrams = find_anagrams(name_count, words)
            remaining_letters = sum(name_count.values())

            print(Fore.LIGHTYELLOW_EX + f'\nAvailable words:', anagrams)

            print(Fore.LIGHTGREEN_EX)
            print('\nRemaining letters:', ''.join(letter * count for letter, count in name_count.items()))
            print(f'Letters left: {remaining_letters}/{limit}')
            print('Current phrase:', ' '.join(phrase))
            
            print(Fore.LIGHTBLUE_EX)
            choice = input('\nPick a word to add or type \'restart\' to start over: ').lower()
            if choice == 'restart':
                break

            if choice in anagrams:
                phrase.append(choice)
                name_count -= Counter(choice)
                final_phrase =  ' '.join(phrase)
            else:
                print(Fore.LIGHTRED_EX + f'\nInvalid choice. Please try again.')

            print(Fore.LIGHTCYAN_EX + f'\n\nFinal phrase: ' + Fore.LIGHTMAGENTA_EX + final_phrase)

# |---------------------------------MAIN_LOOP---------------------------------|
if __name__ == '__main__':
    main()
