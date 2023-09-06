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


def count_char_occurrences(word):
    character_occurrences = {}
    for character in word:
        character_occurrences[character] = character_occurrences.get(character, 0) + 1

    return character_occurrences


def extract_hints(hint_list):
    hint_count = 0
    for hint in hint_list:
        (letter, answer) = hint
        hint_list[hint_count] = answer
        hint_count += 1


def convert_list_to_tuple(list)
    return(*list, )

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
def score_guess(target, guess):
    hints = [("", ""), ("", ""), ("", ""), ("", ""), ("", "")]

    if guess == target:
        print(f"Your guess, {guess}, is correct!")
        for position in range(len(guess)):
            hints[position] = (guess[position], 2)
        extract_hints(hints)
        convert_list_to_tuple(hints)
        return True
    else:
        print("Your guess is wrong!")
        target_letter_occurrences = count_char_occurrences(target)
        guess_letter_occurrences = count_char_occurrences(guess)
        count = 0
        for letter in guess:
            if target.find(letter, count) == guess.find(letter, count):
                if guess_letter_occurrences[letter] > 1:
                    hint_count = 0
                    for hint in hints:
                        if hint == (letter, "?"):
                            hints[hint_count] = (letter, "-")
                        hint_count += 1
                hints[count] = (letter, "+")
            elif target.find(letter) != -1:
                hint_count = 0
                previous_occurrences = 0
                for hint in hints:
                    if hint == (letter, "?"):
                        previous_occurrences += 1
                    hint_count += 1
                if previous_occurrences == target_letter_occurrences[letter]:
                    hints[count] = (letter, "-")
                else:
                    hints[count] = (letter, "?")
            else:
                hints[count] = (letter, "-")
            count += 1
        extract_hints(hints)
        convert_list_to_tuple(hints)
        print(f"Guess: {guess[0]} {guess[1]} {guess[2]} {guess[3]} {guess[4]}")
        print(f"Hint:  {hints[0]} {hints[1]} {hints[2]} {hints[3]} {hints[4]}")


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
print(pick_target_word())
score_guess("world", "hello")

