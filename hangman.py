'''
    my implementation of a hangman game
'''

from random import choice
from sys import exit
from PyDictionary import PyDictionary


def main():
    # letters that have been guessed
    guess_list = []
    strikes = 0

    # get word from dictionary
    with open('word_list.txt') as dict:
        words = dict.readlines()
    word = choice(words).strip()
    letters = list(word)
    dict.close()
    
    # game loop
    # TODO: add win state
    while strikes <= 5:
        # lose state
        if strikes == 5:
            print(f"Strikes: {strikes * 'X '}")
            define = input(f"Word was {word} get definition? Y/N ").upper()
            if define == "Y": get_definition(word)
            exit()

        # still playing
        guessed_letters(guess_list)
        print(f"Strikes: {strikes * 'X '}")
        if guessing(guess_list, word) == word:
            define = input(f"Word was {word} get definition? Y/N ").upper()
            if define == "Y": get_definition(word)
            exit()

        # print spaces and correct guesses
        if guess_list == None: print("_" * len(letters))
        else: print(guessing(guess_list, letters))
        try:
            # get and sanitize player input
            guess = input("Please choose a letter: ").lower()
            if len(guess) > 1: raise ValueError
            if guess in guess_list or guess.isalpha() == False: raise ValueError
            if type(guess) != str: raise TypeError
        
        except (ValueError, TypeError):
            print("Invalid guess try again")
        
        # guess is valid guess
        else:
            # append to guess list
            guess_list.append(guess)
            # strike if applicable
            if guess not in letters: strikes += 1

# print out guessed letters
def guessed_letters(guess_list):
    if guess_list:
        guess_list = "".join(guess_list)
        print(f"Guessed: {', '.join(guess_list)}")


# show the correctly guessed letters and blank tiles
def guessing(guess_list, letters):
    new_word = list("_" * len(letters))
    for i in range(len(letters)):
        for letter in guess_list:
            if letters[i] == letter:
                new_word[i] = letter
    return "".join(new_word)


def get_definition(word):
    dictionary = PyDictionary()
    print(dictionary.meaning(word))

if __name__ == "__main__":
    main()