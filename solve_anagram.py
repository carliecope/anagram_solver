"""Find valid anagrams in a file.

Given a word from user input, check if the word is in the given dictionary file, then generate anagrams of the word and return them to the user. 
"""
import sys
from itertools import permutations

def getInput():
    input_word = input("Enter a word to find its anagrams").strip().lower()
    print(input_word)

    if len(input_word) > 12:
        print("Looks like that word isn't in out dictionary")
        input_word = input("Enter a new word").strip().lower() 
    elif input_word == None:
        input_word = input("Enter a new word")
        input_word = input("Enter a word to find its anagrams").strip().lower()
         
def solve_anagram(input_word):
    """Takes input word, checks for it in dictionary, then outputs a list of anagrams"""
    raw_perm_list = []
    valid_perm_list = []
    
    # Load dictionary.txt file into a dictionary in memory
    max_len = 0
    dictionary = {}

    with open('./dictionary.txt', 'r', encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip()  # remove '\n' at end of line
            dictionary[line] = True
            if len(line) > max_len:
                max_len = len(line)
        print(max_len)

    # Ask for intput
    # my_input = input("Enter something, yo!")

    # Check in input word in dictionary
    inDictionary = dictionary.get(input_word, None)
    if inDictionary is not None:
        print("Looks like {} is in our dictionary.".format(input_word))

        # Generate permutations of input_word
        for i in list(permutations(input_word)):
            raw_perm_list.append("".join(i))
        # print(raw_perm_list)

        # Check and store which permutations are in dictionary
        for perm in raw_perm_list:
            if dictionary.get(perm) != None:
                valid_perm_list.append(perm)

        print(valid_perm_list)

        # Sort permutations by 2nd letter
        sortedList = sorted(valid_perm_list, key=lambda n: n[1:])
        print(sortedList)
        return sortedList
    else:
        print("Looks like {} isn't in out dictionary.".format(input_word))
   
if __name__ == '__main__':
    getInput()


