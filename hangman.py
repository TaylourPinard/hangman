'''
    my implementation of a hangman game
'''

from random import choice
from sys import exit

def main():
    # letters that have been guessed
    guess_list = []
    strikes = 0

    # get word from dictionary
    with open('word_list.txt') as dict:
        words = dict.readlines()
    word = choice(words).strip()
    print(word)
    letters = list(word)
    dict.close()
    
    # game loop
    # TODO: add win state
    # TODO: add dictionary option after win/loss
    while strikes <= 5:
        # lose state
        if strikes == 5:
            print(f"strikes: {strikes * 'X '}")
            exit(f"word was {word}")

        # still playing
        guessed_letters(guess_list)
        print(f"strikes: {strikes * 'X '}")

        # print spaces and correct guesses
        if guess_list == None: print("_" * len(letters))
        else: print(guessing(guess_list, letters))
        try:
            # get and sanitize player input
            guess = input("please choose a letter: ").lower()
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
        print(f"guessed: {', '.join(guess_list)}")


# show the correctly guessed letters and blank tiles
def guessing(guess_list, letters):
    new_word = list("_" * len(letters))
    for i in range(len(letters)):
        for letter in guess_list:
            if letters[i] == letter:
                new_word[i] = letter
    return "".join(new_word)


if __name__ == "__main__":
    main()