"""
Testing for the anagram solver and input function
"""
import unittest
import anagram_solver

# Load dictionary for use in tests of anagram_solver.solveMultiple()
dictionary = anagram_solver.parse_dictionary("dictionary.txt")

class SolveMultipleTests(unittest.TestCase):
    
    def test_string_NOT_in_dict(self):
        output = anagram_solver.solveMultiple("antidisestablishmentarianism", dictionary)
        self.assertEqual(output, None)

    def test_string_in_dict(self):
    	output = anagram_solver.solveMultiple("rates", dictionary)
    	self.assertEqual(output, ['tares', 'tarse', 'sater', 'rates', 'tears', 'teras', 'serta', 'tresa', 'artes', 'aster', 'stare', 'strae'])
    
    def test_NO_valid_anagrams(self):
        output = anagram_solver.solveMultiple("foul", dictionary)
        self.assertEqual(output, None)

    def test_alphabetical_by_2nd_letter(self):
    	output = anagram_solver.solveMultiple("takes", dictionary)
    	self.assertEqual(output, ['takes', 'keast', 'skate', 'stake', 'steak'])

    def test_NO_2nd_arg(self):
        with self.assertRaises(TypeError):
            output = anagram_solver.solveMultiple("argument")
class SolveOneTests(unittest.TestCase):

    def test_string_NOT_in_dict(self):
        output = anagram_solver.solveOne("antidisestablishmentarianism")
        self.assertEqual(output, None)

    def test_string_in_dict(self):
        output = anagram_solver.solveOne("rates")
        self.assertEqual(output, ['tares', 'tarse', 'sater', 'rates', 'tears', 'teras', 'serta', 'tresa', 'artes', 'aster', 'stare', 'strae'])
    
    def test_NO_valid_anagrams(self):
        output = anagram_solver.solveOne("foul")
        self.assertEqual(output, None)

    def test_alphabetical_by_2nd_letter(self):
        output = anagram_solver.solveOne("takes")
        self.assertEqual(output, ['takes', 'keast', 'skate', 'stake', 'steak'])

class ValidateInputTests(unittest.TestCase):

    def test_NON_string_input(self):
    	with self.assertRaises(AttributeError):
    	    output = anagram_solver.validateInput(9999)

    def test_NON_alphabetic_string_input(self):
    	output = anagram_solver.validateInput(")(*)*)*&^(*&^(*&^(*&^")
    	self.assertEqual(output, None)
    
    def test_max_word_length(self):
    	output = anagram_solver.validateInput("antidisestablishmentarianism")
    	self.assertEqual(output, None)

class ParseDictionaryTests(unittest.TestCase):

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            output = anagram_solver.parse_dictionary("random.txt")

if __name__ == "__main__":
    unittest.main()



