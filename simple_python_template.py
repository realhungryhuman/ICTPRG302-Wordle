"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal

import random

EMPTY_TUPLE2 = ("", "")

CORRECT = 2
MISPLACED = 1
WRONG = 0

GAME_WIN = (CORRECT, CORRECT, CORRECT, CORRECT, CORRECT)

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


# TODO: ensure guess in VALID_WORDS
def validate_guess(word, words_file):
    for line in words_file:
        if line.strip() == word:
            return True
    return False


# TODO: provide clues for each character in the guess using your scoring algorithm
def score_guess(target, guess):
    hints = [EMPTY_TUPLE2, EMPTY_TUPLE2, EMPTY_TUPLE2, EMPTY_TUPLE2, EMPTY_TUPLE2]

    if guess == target:
        for position in range(len(guess)):
            hints[position] = (guess[position], CORRECT)
    else:
        target_letter_occurrences = count_char_occurrences(target)
        guess_letter_occurrences = count_char_occurrences(guess)
        count = 0
        for letter in guess:
            if target.find(letter, count) == guess.find(letter, count):
                if guess_letter_occurrences[letter] > 1:
                    hint_count = 0
                    for hint in hints:
                        if hint == (letter, MISPLACED):
                            hints[hint_count] = (letter, WRONG)
                        hint_count += 1
                hints[count] = (letter, CORRECT)
            elif target.find(letter) != -1:
                hint_count = 0
                previous_occurrences = 0
                for hint in hints:
                    if hint == (letter, MISPLACED):
                        previous_occurrences += 1
                    hint_count += 1
                if previous_occurrences == target_letter_occurrences[letter]:
                    hints[count] = (letter, WRONG)
                else:
                    hints[count] = (letter, MISPLACED)
            else:
                hints[count] = (letter, WRONG)
            count += 1
    extract_hints(hints)
    return tuple(hints)


def is_correct(hint):
    if hint == GAME_WIN:
        return True
    return False


def format_score(guess, hint):
    """Formats a guess with a given score as output to the terminal.
        The following is an example output:
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
        Hint:  + + + + +"""
    formatted_hint = []
    for index in range(len(hint)):
        if hint[index] == CORRECT:
            formatted_hint.append("+")
        elif hint[index] == MISPLACED:
            formatted_hint.append("?")
        else:
            formatted_hint.append("_")
    formatted_guess = guess.upper()
    print(f"Guess: {formatted_guess[0]} {formatted_guess[1]} {formatted_guess[2]} "
          f"{formatted_guess[3]} {formatted_guess[4]}")
    print(f"Hint:  {formatted_hint[0]} {formatted_hint[1]} {formatted_hint[2]} "
          f"{formatted_hint[3]} {formatted_hint[4]}")


def game_loop():
    # (start loop)
    # TODO: select target word at random from TARGET_WORDS
    target_word = pick_target_word(TARGET_WORDS).strip()

    # TODO: repeat for MAX_TRIES valid attempts
    attempts = 0
    while attempts < MAX_TRIES:
        guess = input(f"Enter guess? (Cheat: {target_word}) ").strip().lower()
        if validate_guess(guess, VALID_WORDS):
            hint = score_guess(target_word, guess)
            if is_correct(hint):
                print(f"Your guess, {guess}, is correct!")
                break
            else:
                print("Your guess is wrong!")
                format_score(guess, hint)
                attempts += 1
                VALID_WORDS.seek(0)
        else:
            print(f"{guess} is not a valid word. Please Try Again")
            VALID_WORDS.seek(0)
    if attempts == MAX_TRIES:
        print(f"The word was {target_word}.")
    print("Game Over")
    # (end loop)


def main():
    game_loop()


main()
# NOTES:
# ======
# - Add your own flair to the project
# - You will be required to add and refine features based on changing requirements
# - Ensure your code passes any tests you have defined for it.

# SNIPPETS
# ========
# A set of helpful snippets that may help you meet the project requirements.
