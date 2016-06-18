"""
Generate anagrams for a given word.

Given a word from user input, check if the word is in our dictionary.txt file, generate anagrams of the word that are in valid US English and return them to the user. 
"""

from itertools import permutations
import enchant

US_Dict = enchant.Dict("en_US")

def solve_anagram(input_word):
    """Checks for word in dictionary and if found, outputs a list of anagrams"""
    
    raw_perm_list = []
    valid_perm_list = []
    
    # Load dictionary.txt file into a dictionary in memory
    dictionary = {}
    with open('./dictionary.txt', 'r', encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip()  # remove '\n' at end of line
            dictionary[line] = True

    # Check in input word in dictionary
    inDictionary = dictionary.get(input_word, None)
    if inDictionary is not None:
        print("Looks like {} is in our dictionary.".format(input_word))

        # Generate raw permutations of input_word
        for i in list(permutations(input_word)):
            raw_perm = "".join(i)
            if raw_perm not in raw_perm_list and raw_perm != input_word:
                raw_perm_list.append(raw_perm) 

        # Check for permutations in dictionary
        for perm in raw_perm_list:
            if dictionary.get(perm) != None and US_Dict.check(perm) != False:
                valid_perm_list.append(perm) 

        # Sort permutations by 2nd letter
        sortedList = sorted(valid_perm_list, key=lambda n: n[1:])

        if len(sortedList) != 0:
            print("The anagrams of {} are: {}".format(input_word, sortedList))
            return sortedList
        else:
            print("However, there are no anagrams for {}".format(input_word))
            return None
    else:
        print("Looks like {} isn't in our dictionary.".format(input_word))
        return None

def validateInput(input_word):
    """Checks for valid input words"""

    if not input_word.isalpha():
        return 
    elif len(input_word) > 12:
        print("Looks like {} isn't in our dictionary.".format(input_word))
        return 
    elif input_word == None:
        return
    elif US_Dict.check(input_word) == False:
        return 
    else:
        return True
        
def askUser():
    """Takes input word and calls the solve_anagram function"""

    isValid = None

    while isValid == None:
        input_word = input("Enter a word to find its anagrams: ")
        input_word.strip().lower()
        print(input_word)
    
        isValid = validateInput(input_word)

    solve_anagram(input_word)

if __name__ == '__main__':
    askUser()


