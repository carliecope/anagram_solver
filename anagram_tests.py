"""
Testing for the anagram solver and input functions
"""
import unittest
from solve_anagram import solve_anagram
from solve_anagram import validateInput 
from solve_anagram import askUser 

class SolveAnagramTests(unittest.TestCase):
    
    def test_string_NOT_in_dict(self):
        isNone = solve_anagram("antidisestablishmentarianism")
        self.assertEqual(isNone, None)

    def test_string_in_dict(self):
    	anagram_list = solve_anagram("rates")
    	self.assertListEqual(anagram_list, ['tares', 'tears', 'aster', 'stare'])
    
    def test_NO_valid_anagrams(self):
        noneFound = solve_anagram("foul")
        self.assertEqual(noneFound, None)

class ValidateInputTests(unittest.TestCase):

    def test_numeric_input(self):
    	numericInput = validateInput(9999)
    	self.assertEqual(numericInput, None)

    def test_non-alphabetic_input(self):
    	nonAlphabetInput = validateInput(")(*)*)*&^(*&^(*&^(*&^")
    	self.assertEqual(nonAlphabetInput, None)
    
    def test_max_word_length(self):
    	maxLengthInput = validateInput("antidisestablishmentarianism")
    	self.assertEqual(maxLengthInput, None)

if __name__ == "__main__":
    unittest.main()