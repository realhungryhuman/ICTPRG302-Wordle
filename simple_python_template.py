"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# Author: Dylan McClarence
# Company: North Metropolitan TAFE
# Year: 2023

import random


CORRECT = 2  # Correct letter in the correct position
MISPLACED = 1  # Correct letter in the wrong position
WRONG = 0  # Letter is not in the target word

GAME_WIN = (CORRECT, CORRECT, CORRECT, CORRECT, CORRECT)  # Required value to win game

TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'

MAX_TRIES = 6


def guess_my_word_help():
    print(f"Welcome to Guess my Word!\n"
          f"You have {MAX_TRIES} attempts to guess the unknown word.\n\n"
          f"Enter a 5 letter and get hints for each letter:\n"
          f"    + = Right Letter, Right Position\n"
          f"    ? = Right Letter, Wrong Position\n"
          f"    _ = Wrong Letter\n\n"
          f"Good Luck!\n")


def open_word_bank(word_bank_file):
    """
    returns a list of words from a file

    :param word_bank_file: string
    :returns: list
    """
    word_bank = open(word_bank_file)
    words = word_bank.read().splitlines()
    word_bank.close()

    return words


def pick_target_word(target_words):
    """
    returns a random word from a list of words

    :param target_words: list
    :returns: string
    """

    return random.choice(target_words)


def validate_guess(guess, word_list):
    """
    Validates user input by checking if the word exists in a file

    :param guess: string
    :param word_list: list
    :returns: bool

    # >>> validate_guess("hello", VALID_WORDS)
    True
    # >>> validate_guess("steal", VALID_WORDS)
    True
    # >>> validate_guess("xxxxx", VALID_WORDS)
    False
    """

    for word in word_list:
        if word == guess:
            return True
    return False


def score_guess(target, guess):
    """
    given two strings of equal length, returns a tuple of ints representing the score of the guess
    against the target word (WRONG, MISPLACED, or CORRECT)

    :param target: string
    :param guess: string
    :returns: tuple

    # >>> score_guess('hello', 'hello')
    (2, 2, 2, 2, 2)
    # >>> score_guess('drain', 'float')
    (0, 0, 0, 1, 0)
    # >>> score_guess('hello', 'spams')
    (0, 0, 0, 0, 0)

    Try and pass the first few tests in the doctest before passing these tests.
    # >>> score_guess('gauge', 'range')
    (0, 2, 0, 2, 2)
    # >>> score_guess('melee', 'erect')
    (1, 0, 1, 0, 0)
    # >>> score_guess('array', 'spray')
    (0, 0, 2, 2, 2)
    # >>> score_guess('train', 'tenor')
    (2, 0, 1, 0, 1)
    # >>> score_guess('outgo', 'motto')
    (0, 1, 2, 0, 2)
    # >>> score_guess('lotto', 'outgo')
    (1, 0, 2, 0, 2)
    """
    guess_as_list = list(guess)
    target_as_list = list(target)
    hints = [WRONG]*5

    for index in range(len(guess_as_list)):
        if guess_as_list[index] == target_as_list[index]:
            hints[index] = CORRECT
            guess_as_list[index] = '-'
            target_as_list[index] = '-'

    for guess_index in range(len(guess_as_list)):
        if guess_as_list[guess_index] != '-':
            for target_index in range(len(target_as_list)):
                if guess_as_list[guess_index] == target_as_list[target_index]:
                    hints[guess_index] = MISPLACED
                    target_as_list[target_index] = '-'
                    break

    return tuple(hints)


def is_correct(hint):
    """Checks if the score is entirely correct and returns True if it is

    :param hint: tuple
    :returns: bool

    Examples:
    # >>> is_correct((1,1,1,1,1))
    False
    # >>> is_correct((2,2,2,2,1))
    False
    # >>> is_correct((0,0,0,0,0))
    False
    # >>> is_correct((2,2,2,2,2))
    True
    """

    if hint == GAME_WIN:
        return True
    return False


def format_score(guess, hint):
    """
    Formats a guess with a given score as output to the terminal.

    :param guess: string
    :param hint: tuple

    # >>> format_score('hello', (0,0,0,0,0))
    Guess: H E L L O
    Hint:  _ _ _ _ _
    # >>> format_score('hello', (0,0,0,1,1))
    Guess: H E L L O
    Hint:  _ _ _ ? ?
    # >>> format_score('hello', (1,0,0,2,1))
    Guess: H E L L O
    Hint:  ? _ _ + ?
    # >>> format_score('hello', (2,2,2,2,2))
    Guess: H E L L O
    Hint:  + + + + +
    """

    formatted_hint = []
    for index in range(len(hint)):
        if hint[index] == CORRECT:
            formatted_hint.append("+")
        elif hint[index] == MISPLACED:
            formatted_hint.append("?")
        else:
            formatted_hint.append("_")
    formatted_guess = guess.upper()

    print(f"Guess: {' '.join(str(letter) for letter in formatted_guess)}\n"
          f"Hint:  {' '.join(str(letter) for letter in formatted_hint)}")


def game_loop():
    target_word_bank = open_word_bank(TARGET_WORDS)
    valid_word_bank = open_word_bank(VALID_WORDS)

    target_word = pick_target_word(target_word_bank)

    attempts = 0  # Count for the players attempts
    while attempts < MAX_TRIES:
        guess = input(f"Enter guess? (Cheat: {target_word})\n").strip().lower()
        if validate_guess(guess, valid_word_bank):
            hint = score_guess(target_word, guess)
            if is_correct(hint):
                print(f"Your guess, {guess.upper()}, is correct!\n")
                break
            else:
                print("Your guess is wrong!")
                format_score(guess, hint)
            attempts += 1
        else:
            print(f"{guess} is not a valid word. Please Try Again\n")
    if attempts == MAX_TRIES:
        print(f"The word was {target_word.upper()}.")
    print("Game Over")


def main(test=False):
    if test:
        import doctest
        doctest.testmod()
    guess_my_word_help()
    game_loop()


if __name__ == '__main__':
    main(test=True)
