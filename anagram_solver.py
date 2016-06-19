"""
Generates anagrams from user input words. 

Options optimized for single and multiple user inputs. 

Given a word from user input, checks if the word is in our dictionary.txt file. If found, generates anagrams of the word from our dictionary and returns them to the user. 
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

def validateInput(input_word):
   """Checks for valid input words"""

   if not input_word.isalpha():
      return 
   elif len(input_word) > 12:
      print("Looks like {} isn't in our dictionary.".format(input_word))
      return 
   elif input_word == None:
      return
   else:
      return True
        
def askUser():
   """Takes input and calls validation function"""

   isValid = None

   while isValid == None:
      input_word = input("Enter an English word to find its anagrams: ")
      input_word = input_word.strip()
      input_word = input_word.lower()

      isValid = validateInput(input_word)

   return input_word  

def solveMultiple(input_word, word_anagrams):
   """Checks for word in dictionary and if found, outputs a list of valid anagrams"""
   
   valid_anagram = []

   sorted_word = ''.join(sorted(input_word))

   if word_anagrams[sorted_word]:
      for instance in word_anagrams[sorted_word]:
         valid_anagram.append(instance)

      valid_anagram = sorted(valid_anagram, key=lambda n: n[1:])          
      
      if len(valid_anagram) > 1:
         print("The anagrams for {} are: {}".format(input_word, valid_anagram))
         return valid_anagram
      else:
         print("There no valid anagrams for {} in our dictionary.".format(input_word))

   else:
      print("No matches for {} found in our dictionary.".format(input_word))

def solveOne(input_word):
   """Checks for word in dictionary and if found, outputs a list of valid anagrams"""
   
   valid_anagram = []

   with open("./dictionary.txt") as dictionary:
      for word in dictionary:
         word = word.rstrip()
         if sorted(list(input_word)) == sorted(list(word)):
            valid_anagram.append(word)

   valid_anagram = sorted(valid_anagram, key=lambda n: n[1:])          
   
   if len(valid_anagram) > 1:
      print("The anagrams for {} are: {}".format(input_word, valid_anagram))
      return valid_anagram
   elif len(valid_anagram) == 1:
      print("There no valid anagrams for {} in our dictionary.".format(input_word))
   else:
      print("No matches for {} found in our dictionary.".format(input_word))

def run():
   """Runs CLI until user opts to exit"""

   inputCount = input("Would you like to solve for more than one word? y or n: ")

   if inputCount == "n":
      input_word = askUser()
      solveOne(input_word)

   elif inputCount == "y":
      word_anagrams = parse_dictionary("dictionary.txt")
      run = True

      while run == True:
         input_word = askUser()
         solveMultiple(input_word, word_anagrams)
         replay_feedback = input("Enter q to quit or press enter to keep playing: ")

         if replay_feedback == "q":
            run = False 
      sys.exit()
   else: 
      sys.exit() 

if __name__ == "__main__":
   run()


