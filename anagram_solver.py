"""
Generates anagrams from user input words.

Options optimized for single and multiple, successive user inputs.

Given a word from user input, checks if the word is in our dictionary.txt file.

If found, generates anagrams of the word from our dictionary and returns them
to the user.
"""
import sys

from collections import defaultdict


def parse_dictionary(filename):
    """Reads file and makes dictionary of sorted words"""
    word_anagrams = defaultdict(set)

    with open(filename) as dictionary:
        for word in dictionary:
            word = word.rstrip()
            word_anagrams[''.join(sorted(word))].add(word)

    return word_anagrams


def validate_input(input_word):
    """Checks for valid input words"""

    max_entry_length = 12

    if input_word.isalpha() is False:
        return False
    elif len(input_word) > max_entry_length:
        print("Looks like {} isn't in our dictionary.".format(input_word))
        return False
    elif input_word is None:
        return False
    else:
        return True


def ask_user():
    """Takes input and calls validation function"""

    valid_input = False

    while valid_input is False:
        input_word = input("Enter an English word to find its anagrams: ")
        input_word = input_word.strip().lower()

        valid_input = validate_input(input_word)

    return input_word


def return_results(input_word, valid_anagram):
    """Returns results to user"""

    if valid_anagram:
        print("The anagrams for {} are: {}".format(input_word, valid_anagram))
        return valid_anagram
    else:
        print("There no valid anagrams for {} in our dictionary.".format(input_word))
        return []


def solve_multiple(input_word, word_anagrams):
    """Checks for word in dictionary and if found, outputs valid anagrams"""

    valid_anagram = []
    sorted_word = ''.join(sorted(input_word))

    if word_anagrams[sorted_word]:
        valid_anagram = sorted(list(word_anagrams[sorted_word]), key=lambda n: n[1:])
        valid_anagram.remove(input_word)

        result_list = return_results(input_word, valid_anagram)
        return result_list
    else:
        print("No matches for {} found in our dictionary.".format(input_word))
        return []


def solve_one(input_word):
    """Checks for word in dictionary and if found, outputs valid anagrams"""

    valid_anagram = []

    with open("./dictionary.txt") as dictionary:
        for word in dictionary:
            word = word.rstrip()
            if sorted(list(input_word)) == sorted(list(word)):
                valid_anagram.append(word)

    if valid_anagram:
        valid_anagram = sorted(valid_anagram, key=lambda n: n[1:])
        valid_anagram.remove(input_word)

    result_list = return_results(input_word, valid_anagram)
    return result_list


def run():
    """Runs CLI until user opts to exit"""

    input_count = input("Would you like to solve for more than one word? y or n: ")

    if input_count == "n":
        input_word = ask_user()
        solve_one(input_word)

    elif input_count == "y":
        word_anagrams = parse_dictionary("dictionary.txt")
        run = True

        while run is True:
            input_word = ask_user()
            solve_multiple(input_word, word_anagrams)
            replay_feedback = input("Enter q to quit or press enter to keep playing: ")

            if replay_feedback == "q":
                run = False
        sys.exit()
    else:
        sys.exit()

if __name__ == "__main__":
    run()
