"""
Testing for the anagram solver and input function
"""
import unittest
from solve_anagram import solve_anagram
from solve_anagram import validateInput 

class SolveAnagramTests(unittest.TestCase):
    
    def test_string_NOT_in_dict(self):
        output = solve_anagram("antidisestablishmentarianism")
        self.assertEqual(output, None)

    def test_string_in_dict(self):
    	output = solve_anagram("rates")
    	self.assertListEqual(output, ['tares', 'tears', 'aster', 'stare'])
    
    def test_NO_valid_anagrams(self):
        output = solve_anagram("foul")
        self.assertEqual(output, None)

    def test_alphabetical_by_2nd_letter(self):
    	output = solve_anagram("takes")
    	self.assertListEqual(output, ['skate', 'stake', 'steak'])

class ValidateInputTests(unittest.TestCase):

    def test_NON_string_input(self):
    	with self.assertRaises(AttributeError):
    	    nonStringInput = validateInput(9999)

    def test_NON_alphabetic_string_input(self):
    	nonAlphabetInput = validateInput(")(*)*)*&^(*&^(*&^(*&^")
    	self.assertEqual(nonAlphabetInput, None)
    
    def test_max_word_length(self):
    	maxLengthInput = validateInput("antidisestablishmentarianism")
    	self.assertEqual(maxLengthInput, None)

if __name__ == "__main__":
    unittest.main()