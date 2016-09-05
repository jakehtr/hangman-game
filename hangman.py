#!/usr/bin/env python3

"""
hangman.py - Gets a random word/phrase from https://www.thegamegal.com/word-generator/
and uses it to play a game of hangman with the user.
"""

from selenium import webdriver
import time
import string


# This is what will be printed to the console in order to hide the word, and reveal
# the user's correct guesses.
def char_replace(word):
    for char in word:
        if char not in alphabet_upper:
            word_list.append(char)
        else:
            word_list.append('_')


def get_random_word():
    browser = webdriver.PhantomJS()
    browser.get('https://www.thegamegal.com/word-generator/')
    element_game = browser.find_element_by_id('game')
    element_cat = browser.find_element_by_id('category')
    new_word_button = browser.find_element_by_id('newword-button')
    element_game.send_keys('Any Game')
    element_cat.send_keys('Any Word Ever!')
    while True:
        new_word_button.click()
        time.sleep(0.35)  # allowing the page to fully load before attempting to find the word
        word = browser.find_element_by_id('gennedword').text
        # making sure the word isn't too short
        if len(word) >= 6:
            chosen_word = word.upper()
            char_replace(chosen_word)
            browser.quit()
            return chosen_word


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
    return message


def hangman():
    turn = 0
    max_turns = 6
    print('Let me think of a word...')
    word = get_random_word()
    print('Aha! Got one. Game on.')
    while True:
        print(turn_images[turn])
        print('\n{}'.format(' '.join(word_list)))
        print('\n{}'.format(' '.join(alphabet_upper)))
        user_guess = input('Take a guess using the letters above, or try to guess the whole word: ').upper()
        if len(user_guess) == len(word):
            if user_guess == word:
                for i in range(len(word)):
                    word_list[i] = word[i]
                print('\nGreat guess!')
            else:
                turn += 1
                print(turn_check(turn, max_turns))
        elif user_guess not in alphabet_upper:
            print('You can\'t use that. Try again.')
        else:
            if user_guess in word:
                print('\nSuccess! The letter {} is in the word.'.format(user_guess))
                for i in range(len(word)):
                    if word[i] == user_guess:
                        word_list[i] = user_guess
            else:
                turn += 1
                print(turn_check(turn, max_turns))
            alphabet_upper.remove(user_guess)
        if game_finished_check(turn, max_turns, word, word_list):
            break

if __name__ == '__main__':
    word_list = list()
    alphabet_upper = list(string.ascii_uppercase)  # the letters available to the user for guessing
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
