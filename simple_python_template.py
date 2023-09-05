"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal

import random

TARGET_WORDS = open('./word-bank/target_words.txt')
VALID_WORDS = open('./word-bank/all_words.txt')

MAX_TRIES = 6


def pick_target_word(target_words):
    """returns a random item from the list"""
    words = list(target_words)
    return random.choice(words)


# TODO: select target word at random from TARGET_WORDS
target_word = pick_target_word(TARGET_WORDS).strip()


def validate_guess(word, words_file):
    for line in words_file:
        if line.strip() == word:
            return True
    return False


# TODO: repeat for MAX_TRIES valid attempts
# (start loop)
attempts = 0
while attempts < MAX_TRIES:
    guess = input("Enter guess? ").strip().lower()
    print(guess)
    if validate_guess(guess, VALID_WORDS):
        attempts += 1
        VALID_WORDS.seek(0)
    else:
        print(f"{guess} is not a valid word. Please Try Again")
        VALID_WORDS.seek(0)

# TODO: ensure guess in VALID_WORDS

# TODO: provide clues for each character in the guess using your scoring algorithm
if guess == target_word:
    print("Your guess is correct!")
else:
    print("Your guess is wrong!")

# (end loop)
print("Game Over")


# NOTES:
# ======
# - Add your own flair to the project
# - You will be required to add and refine features based on changing requirements
# - Ensure your code passes any tests you have defined for it.

# SNIPPETS
# ========
# A set of helpful snippets that may help you meet the project requirements.

def display_matching_characters(guess='hello', target_word='world'):
    """Get characters in guess that correspond to characters in the target_word"""
    i = 0
    for char in guess:
        print(char, target_word[i])
        i += 1

# Uncomment to run:
# display_matching_characters()
# print(pick_target_word())
