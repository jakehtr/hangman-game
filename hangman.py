#!/usr/bin/env python3

"""
hangman.py - Gets a random word/phrase from all_words.txt and uses it to play a game of hangman with the user.
"""

from time import sleep
from string import ascii_uppercase
import random


def game_finished_check(turn, max_turn, word, word_chars):
    game_end = {'win': ''.join(word_chars) == word, 'lose': turn == max_turn}
    for k, v in game_end.items():
        if v:
            print(turn_images[turn])
            print('\n  {}'.format(' '.join(word_chars)))
            if k == 'win':
                print('\nCongratulations! You win.')
            else:
                print('\nGame over! The word was {}.'.format(word))
            return True
    return False


def turn_check(turn, max_turn):
    message = '\nNo match. Wrong guesses left: {}.'.format(max_turn - turn)
    print(message)


def hangman():
    turn = 0
    max_turns = 6
    alphabet_upper = list(ascii_uppercase)  # the letters available to the user for guessing
    print('Let me think of a word...')
    sleep(1.5)
    word = random.choice(open('all_words.txt').readlines()).upper().replace('\n', '')
    print('Aha! Got one. Game on.')
    word_char_replace = [char if char not in alphabet_upper else '_' for char in word]  # hide the word in the console
    
    while True:
        print(turn_images[turn])
        print('\n  {}'.format(' '.join(word_char_replace)))
        print('\n  {}'.format(' '.join(alphabet_upper)))
        user_guess = input(
            'Guess using the letters above, or try to guess the whole word (leave blank to quit): ').upper().strip()
        if len(user_guess) == len(word):
            if user_guess == word:
                word_char_replace = list(word)
                print('\nGreat guess!')
            else:
                turn += 1
                turn_check(turn, max_turns)
        elif user_guess not in alphabet_upper:
            if user_guess == '':
                return
            print('You can\'t use that. Try again.')
        else:
            if user_guess in word:
                print('\nSuccess! The letter {} is in the word.'.format(user_guess))
                for i in range(len(word)):
                    if word[i] == user_guess:
                        word_char_replace[i] = user_guess
            else:
                turn += 1
                turn_check(turn, max_turns)
            alphabet_upper.remove(user_guess)
        if game_finished_check(turn, max_turns, word, word_char_replace):
            play_again = input('Play again? (Y/N) ').lower().strip()
            if play_again == 'y':
                return hangman()
            return

if __name__ == '__main__':
    turn_images = ['    ____\n' +
                   '   |/   |\n' +
                   '   |     \n' +
                   '   |      \n' +
                   '   |      \n' +
                   '  _|__',
                   '    ____\n' +
                   '   |/   |\n' +
                   '   |    o\n' +
                   '   |      \n' +
                   '   |      \n' +
                   '  _|__',
                   '    ____\n' +
                   '   |/   |\n' +
                   '   |    o\n' +
                   '   |    | \n' +
                   '   |      \n' +
                   '  _|__',
                   '    ____\n' +
                   '   |/   |\n' +
                   '   |    o\n' +
                   '   |   /| \n' +
                   '   |      \n' +
                   '  _|__',
                   '    ____\n' +
                   '   |/   |\n' +
                   '   |    o\n' +
                   '   |   /|\\\n' +
                   '   |      \n' +
                   '  _|__',
                   '    ____\n' +
                   '   |/   |\n' +
                   '   |    o\n' +
                   '   |   /|\\\n' +
                   '   |   /  \n' +
                   '  _|__',
                   '    ____\n' +
                   '   |/   |\n' +
                   '   |    o\n' +
                   '   |   /|\\\n' +
                   '   |   / \\\n' +
                   '  _|__'
                   ]

    hangman()
