#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
hangman.py - Gets a random word/phrase from all_words.txt and uses it to play a game of hangman with the user.
"""

from time import sleep
from string import ascii_uppercase
import random


def game_finished_check(turn, max_turn, word, word_chars):
    # player win condition
    if ''.join(word_chars) == word:
        print('\n{}'.format(' '.join(word_chars)))
        print('\nCongratulations! You win.')
        return True
    # player lose condition
    elif turn == max_turn:
        print(turn_images[turn])
        print('\n{}'.format(' '.join(word_chars)))
        print('\nGame over! The word was {}.'.format(word))
        return True
    return False


def turn_check(turn, max_turn):
    message = '\nNo match. Wrong guesses left: {}.'.format(max_turn - turn)
    print(message)


def hangman():
    turn = 0
    max_turns = 6
    print('Let me think of a word...')
    sleep(1.5)
    word = random.choice(open('all_words.txt').readlines()).upper().replace('\n', '')
    print('Aha! Got one. Game on.')
    word_char_replace = [char if char not in alphabet_upper else '_' for char in word]  # hide the word in the console
    
    while True:
        print(turn_images[turn])
        print('\n{}'.format(' '.join(word_char_replace)))
        print('\n{}'.format(' '.join(alphabet_upper)))
        user_guess = input('Take a guess using the letters above, or try to guess the whole word: ').upper()
        if len(user_guess) == len(word):
            if user_guess == word:
                for i in range(len(word)):
                    word_char_replace[i] = word[i]
                print('\nGreat guess!')
            else:
                turn += 1
                turn_check(turn, max_turns)
        elif user_guess not in alphabet_upper:
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
            break

if __name__ == '__main__':
    alphabet_upper = list(ascii_uppercase)  # the letters available to the user for guessing
    turn_images = ['  ____\n' +
                   ' |/   |\n' +
                   ' |     \n' +
                   ' |      \n' +
                   ' |      \n' +
                   '_|__',
                   '  ____\n' +
                   ' |/   |\n' +
                   ' |    o\n' +
                   ' |      \n' +
                   ' |      \n' +
                   '_|__',
                   '  ____\n' +
                   ' |/   |\n' +
                   ' |    o\n' +
                   ' |    | \n' +
                   ' |      \n' +
                   '_|__',
                   '  ____\n' +
                   ' |/   |\n' +
                   ' |    o\n' +
                   ' |   /| \n' +
                   ' |      \n' +
                   '_|__',
                   '  ____\n' +
                   ' |/   |\n' +
                   ' |    o\n' +
                   ' |   /|\\\n' +
                   ' |      \n' +
                   '_|__',
                   '  ____\n' +
                   ' |/   |\n' +
                   ' |    o\n' +
                   ' |   /|\\\n' +
                   ' |   /  \n' +
                   '_|__',
                   '  ____\n' +
                   ' |/   |\n' +
                   ' |    o\n' +
                   ' |   /|\\\n' +
                   ' |   / \\\n' +
                   '_|__'
                   ]

    hangman()
